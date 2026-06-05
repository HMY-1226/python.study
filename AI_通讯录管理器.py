import os
import json
from os import system

import requests


DATA_FILE  = "contacts.json"
API_KEY = "sk-4da8a85fa41549acb658c91cc7eccd12"
URL = "https://api.deepseek.com/v1/chat/completions"



def load_contacts():   #加载通讯录
    if os.path.exists("DATA_FILE"):
        with open("DATA_FILE","r",encoding="utf-8") as f:
            return json.load(f)  # 返回json文本加载被赋值的f
    return [] #如果是空的则返回一个空列表

def save_contacts(contacts): #保存数据到通讯录
    with open("DATA_FILE","w",encoding="utf-8") as f:
        json.dump(contacts,f,ensure_ascii=False,indent=2) #ensure_ascii=False:不把中文转成 \uxxxx 编码，直接写中文    indent=2每个层级缩进2个空格，让文件内容好看，方便人阅读


def add_contacts(contacts,name,phone,emile): #添加联系人 姓名 电话  邮箱
    contacts.append({"name":name,"phone":phone,"mile":emile})  #添加姓名  电话  邮箱到 contacts列表里
    save_contacts(contacts)  #保存
    return f"已添加联系人:{name},电话:{phone}" #返回已添加信息

def search_contacts(contacts,name): #搜索功能   参数只加name就行
    results = [c for c in contacts if name in c["name"]]  #一个函数式  添加c这个参数 遍历contacts 如果name在c的这个值里 然后保存
    if not results: #未找到就写not
        return f"未找到联系人:{name}"
    reply = "找到以下联系人:\n"#找到了就遍历信息
    for i in results: # 把信息加到results里
        reply += f"姓名:{i['name']},电话：{i['phone']}，邮箱：{i.get('email', '无')}"
    return reply.strip()#去掉字符串首尾的空白字符

def update_contacts(contacts,name,new_phone,new_emile):
    for i in contacts:
        if i["name"] == name:
            if new_phone:
                i["phone"] = new_phone
            if new_emile:
                i["mile"] = new_emile
            save_contacts(contacts)
            return f"已更新{name}内容"
    return f"未找到姓名为:{name}的联系人"

def delete_contacts(contacts,name):
    for i in contacts:
        if i["name"] == "":
            contacts.remove(i)
            save_contacts(contacts)
            return f"已删除联系人:{name}"
    return f"未找到姓名为:{name}的联系人"

def show_all(contacts):
    if not contacts:
        return '通讯录为空'
    reply = f"共有{len(contacts)}个联系人."
    for i,c in enumerate(contacts,1):
        reply += f"{i},{c['name']},{c['phone']}"
    return reply.strip()


def main():
    contacts = load_contacts()

    print("===== AI 通讯录助手 =====")
    print("你可以直接对我说话，比如：")
    print("  - 帮我查一下张三的电话")
    print("  - 添加联系人李四，电话139")
    print("  - 把张三删了")
    print("  - 显示所有联系人")
    print("输入 quit 退出")
    print("==========================")

    # 构建系统提示词
    system_prompt = f"""你是一个通讯录管理助手。当前通讯录数据如下：
{json.dumps(contacts, ensure_ascii=False)}

用户会用自然语言让你操作通讯录。请判断用户意图，从以下操作中选择一个，并提取参数：

1. search  - 查询联系人（需要参数：name）
2. add    - 添加联系人（需要参数：name, phone, email）
3. update - 修改联系人（需要参数：name, new_phone, new_email）
4. delete - 删除联系人（需要参数：name）
5. show   - 查看所有联系人（无需参数）

重要规则：
- 如果用户指令明确，直接返回 JSON。
- 如果用户想做某个操作但**缺少必要参数**（比如只说"添加联系人"但没说名字和电话），**不要直接执行**，而是用自然语言追问，直到信息齐全。
- 添加操作必须至少有 name 和 phone，缺少任何一个都必须追问。

当信息齐全时，返回 JSON。当缺少必要参数时，用自然语言追问用户。
格式：{{"action": "操作名", "params": {{...}}}}

示例：
- 用户说"查张三的电话" → {{"action": "search", "params": {{"name": "张三"}}}}
- 用户说"添加王五电话139" → {{"action": "add", "params": {{"name": "王五", "phone": "139", "email": ""}}}}
- 用户说"显示所有联系人" → {{"action": "show", "params": {{}}}}"""

    messages = [{"role": "system", "content": system_prompt}]

    while True:
        user_input = input("\n你：")
        if user_input.lower() == "quit":
            print("再见！")
            break

        # 把用户指令发给 AI
        messages.append({"role": "user", "content": user_input})

        response = requests.post(
            URL,
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"model": "deepseek-chat", "messages": messages}
        )

        ai_reply = response.json()["choices"][0]["message"]["content"]

        # 解析 AI 返回的 JSON
        try:
            action_data = json.loads(ai_reply)
            action = action_data["action"]
            params = action_data["params"]
        except:
            print(ai_reply)
            continue

        # 根据 AI 判断的操作执行对应函数
        if action == "search":
            result = search_contacts(contacts, params.get("name", ""))
        elif action == "add":
            result = add_contacts(contacts, params.get("name", ""), params.get("phone", ""), params.get("email", ""))
        elif action == "update":
            result = update_contacts(contacts, params.get("name", ""), params.get("new_phone", ""),
                                    params.get("new_email", ""))
        elif action == "delete":
            result = delete_contacts(contacts, params.get("name", ""))
        elif action == "show":
            result = show_all(contacts)
        else:
            result = f"未知操作：{action}"

        print(result)

        # 如果修改了数据，更新系统提示词里的通讯录信息
        if action in ["add", "update", "delete"]:
            system_prompt = f"""你是一个通讯录管理助手。当前通讯录数据如下：
{json.dumps(contacts, ensure_ascii=False)}

用户会用自然语言让你操作通讯录。请判断用户意图，从以下操作中选择一个，并提取参数：

1. search  - 查询联系人（需要参数：name）
2. add    - 添加联系人（需要参数：name, phone, email）
3. update - 修改联系人（需要参数：name, new_phone, new_email）
4. delete - 删除联系人（需要参数：name）
5. show   - 查看所有联系人（无需参数）

请用 JSON 格式回复，只回复 JSON，不要其他内容。
格式：{{"action": "操作名", "params": {{...}}}}"""
            messages = [{"role": "system", "content": system_prompt}]



if __name__ == "__main__":
    main()


