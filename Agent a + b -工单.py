import json
import os           # 新增：用于读取环境变量 os.getenv()
import requests
from datetime import datetime
from AItools import (
    read_staff_config, find_best_handler, update_task_count,
    log_ticket, check_punishment
)

# ============================================================
# 旧代码：API Key 直接写在代码里 —— 不安全！
#   别人看到代码就能偷用你的额度，甚至盗刷你的 API 账单。
#   API_KEY = "sk-4da8a85fa41549acb658c91cc7eccd12"
#
# 优化后：从系统环境变量读取，代码里只留变量名，不暴露密钥。
#   os.getenv("变量名", "默认值")  —— 去系统环境变量里找，
#   找不到就用 ""（空字符串）兜底，避免报 None 错误。
# ============================================================
API_KEY = os.getenv("DEEPSEEK_API_KEY", "")   # 从环境变量取 API Key
if not API_KEY:                                 # 如果没设置环境变量
    raise ValueError("请设置环境变量 DEEPSEEK_API_KEY")  # 直接报错提醒用户

URL = "https://api.deepseek.com/v1/chat/completions"


def agent_a_classify(user_input, clarify_count=0):
    """Agent A：分类 + 紧急程度判断 + 多轮确认"""

    system_prompt = f"""你是IT工单分类助手。根据工单内容判断：

    1. 工单类别及常见关键词：
       - 打印机：打印机卡纸、没墨、脱机、无法打印
       - 网络故障：网断了、上不了网、网络慢、WiFi连不上、ping不通、内网访问异常
       - 服务器：服务器宕机、重启、连接超时、数据库异常、业务系统无法访问
       - 软件安装：重装系统、装软件、装PS、装Office、系统重装、Windows安装
       - 账号权限：开通账号、权限不够、密码重置、登录不了
       - 硬件故障：电脑开不了机、蓝屏、鼠标键盘坏了、屏幕坏了
       - 其他：以上都不匹配的情况

    2. 紧急程度（1-5级）：
       - 5级：需要1小时内处理（关键词：宕机、影响生产、急、业务停摆、无法工作）
       - 4级：1-3小时内处理（影响部分功能）
       - 3级：3-6小时内处理（可控范围内）
       - 2级：半天内处理
       - 1级：一天内处理

    3. confidence：你对分类的确定程度（0-1）

    重要规则：
    - 如果用户说"没了"、"没有"、"不处理了"、"下次再说"、"先这样"等表示没有新工单的意思，返回：
      {{"action": "exit", "message": "退出系统"}}
    - 如果用户询问有哪些类别、或问"分类"、"类型是啥"、"都有啥类型"，返回：
      {{"action": "help", "message": "📋 当前支持的工单类别：\\n  ● 打印机 - 例如：打印机卡纸、无法打印\\n  ● 网络故障 - 例如：无法上网、网络很慢、ping不通\\n  ● 服务器 - 例如：服务器宕机、数据库异常\\n  ● 软件安装 - 例如：重装系统、安装软件\\n  ● 账号权限 - 例如：密码重置、账号申请\\n  ● 硬件故障 - 例如：电脑蓝屏、键盘失灵\\n请告诉我您遇到的问题属于哪一类，或者直接描述您的问题。"}}
    - 如果用户直接说出类别名（如"打印机"、"网络故障"），直接使用该类别，confidence 设为 1.0，urgency 设为 3 并追问一句确认紧急程度。
    - 如果 confidence < 0.7 且追问次数 < 3，追问用户确认。

    返回 JSON：
    {{"category": "类别", "urgency": 数字, "confidence": 0.0-1.0}}
    或 {{"action": "help", "message": "帮助信息"}}
    或 {{"action": "clarify", "message": "追问内容"}}

    当前是第{clarify_count + 1}次追问，如果已追问3次仍不确定，直接返回置信度最高的判断。"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    response = requests.post(
        URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"model": "deepseek-chat", "messages": messages}
    )

    return response.json()["choices"][0]["message"]["content"]


def main():
    print("===== IT 工单分派系统 =====")
    print("（Agent A 分类 + Agent B 分配）")
    print("输入 quit 退出")
    print("===========================")

    ticket_counter = 1

    while True:
        user_input = input("\n工单内容：").strip()
        # 检测退出意图（精确匹配，避免编码问题）
        if user_input.lower() in ("quit", "exit", "q", "0"):
            print("系统已退出。")
            break
        if user_input in ("没了", "没有", "没有了", "没", "没工单"):
            print("系统已退出。")
            break

        # === Agent A：分类 + 多轮确认 ===
        clarify_count = 0
        while clarify_count < 3:
            result = agent_a_classify(user_input, clarify_count)

            try:
                data = json.loads(result)

                if "action" in data and data["action"] == "clarify":
                    print(f"🤔 {data['message']}")
                    clarify_count += 1
                    user_input = input("补充信息：")
                    continue

                if "action" in data and data["action"] == "exit":
                    print("系统已退出。")
                    return

                if "action" in data and data["action"] == "help":
                    print(data["message"])
                    user_input = input("\n请输入工单内容：")
                    continue

                category = data["category"]
                urgency = data["urgency"]
                confidence = data["confidence"]

                if confidence < 0.7:
                    print(f"⚠️ 分类不确定（confidence={confidence}），已追问{clarify_count}次")
                    # 最后一次追问
                    clarify_count += 1
                    user_input = input("请补充更多信息：")
                    continue

                # 分类成功
                print(f"✅ 类别：{category}，紧急程度：{urgency}级，置信度：{confidence}")
                break

            except json.JSONDecodeError:
                print(f"⚠️ Agent A 返回格式异常：{result}")
                # 兜底：直接问用户
                category = input("无法自动分类，请手动输入类别：")
                urgency = int(input("请输入紧急程度（1-5）："))
                break

        # === Agent B：分配处理人 ===
        handler, msg = find_best_handler(category, urgency)

        if handler:
            print(f"✅ {msg}")
            update_task_count(handler['name'], 1)
            log_ticket(ticket_counter, category, urgency, handler['name'], "已分配")
        else:
            print(f"⚠️ {msg}")
            log_ticket(ticket_counter, category, urgency, "未分配", "待人工处理")

        ticket_counter += 1


if __name__ == "__main__":
    main()
