import pandas as pd
import os
from datetime import datetime

# ============================================================
# 旧代码（硬编码绝对路径，换电脑就得改）：
#   EXCEL_PATH = "D:/工单管理.xlsx"
#   LOG_PATH = "D:/工单日志.xlsx"
#
# 优化后：用 __file__ 拿到当前脚本所在的文件夹路径，
#         再把 Excel 文件放同目录下，整个文件夹随便复制到哪都能跑。
# ============================================================

# __file__ 是当前 .py 文件的完整路径（如 D:/xxx/AItools.py）
# os.path.abspath() 确保它是绝对路径
# os.path.dirname()  提取出目录部分（去掉文件名）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在文件夹路径

# os.path.join() 把路径和文件名拼接起来，自动处理斜杠方向
EXCEL_PATH = os.path.join(BASE_DIR, "工单.xlsx")       # 人员配置表
LOG_PATH = os.path.join(BASE_DIR, "工单日志.xlsx")      # 分配记录日志


# ========== 人员配置读取 ==========

def read_staff_config():
    """读取所有部门的人员配置，返回可读摘要"""
    if not os.path.exists(EXCEL_PATH):
        return f"文件不存在：{EXCEL_PATH}"
    all_sheets = pd.read_excel(EXCEL_PATH, sheet_name=None)
    summary = "当前人员配置：\n"
    for sheet_name, df in all_sheets.items():
        summary += f"\n【{sheet_name}】\n"
        for _, row in df.iterrows():
            if row['黑名单'] == '否':
                summary += f"  {row['姓名']} - 负责：{row['负责大类']} - 当前工单数：{row['当前工单数']}\n"
    return summary


def find_best_handler(category, urgency_level):
    """根据类别和紧急程度找最佳处理人"""
    all_sheets = pd.read_excel(EXCEL_PATH, sheet_name=None)
    candidates = []

    for sheet_name, df in all_sheets.items():
        for _, row in df.iterrows():
            if row['黑名单'] == '是':
                continue
            if category in str(row['负责大类']):
                task_count = int(row['当前工单数'])

                # 规则1：已有3个任务的不考虑
                if task_count >= 3:
                    continue
                # 规则2：五级任务独占，已有五级任务的不考虑
                if urgency_level == 5 and task_count >= 1:
                    continue

                candidates.append({
                    "name": row['姓名'],
                    "department": sheet_name,
                    "task_count": task_count
                })

    if not candidates:
        # 没人可用，找任务最少的人（放宽限制）
        for sheet_name, df in all_sheets.items():
            for _, row in df.iterrows():
                if row['黑名单'] == '是':
                    continue
                candidates.append({
                    "name": row['姓名'],
                    "department": sheet_name,
                    "task_count": int(row['当前工单数'])
                })

    if not candidates:
        return None, "无可用处理人"

    best = min(candidates, key=lambda x: x['task_count'])
    return best, f"分派给{best['department']}的{best['name']}（当前工单数：{best['task_count']}）"


def update_task_count(name, delta=1):
    """更新某人的工单计数"""
    all_sheets = pd.read_excel(EXCEL_PATH, sheet_name=None)
    for sheet_name, df in all_sheets.items():
        for i, row in df.iterrows():
            if row['姓名'] == name:
                all_sheets[sheet_name].at[i, '当前工单数'] = int(row['当前工单数']) + delta
                break
    with pd.ExcelWriter(EXCEL_PATH, engine='openpyxl') as writer:
        for sheet_name, df in all_sheets.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    return f"已更新{name}的工单计数（{'+' if delta > 0 else ''}{delta}）"


# ========== 日志记录 ==========

def log_ticket(ticket_id, category, urgency, handler, status, timestamp=None):
    """记录工单处理日志"""
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_data = {
        "工单ID": [ticket_id],
        "类别": [category],
        "紧急程度": [urgency],
        "处理人": [handler],
        "状态": [status],
        "分配时间": [timestamp],
        "完成时间": [""]
    }

    if os.path.exists(LOG_PATH):
        existing = pd.read_excel(LOG_PATH)
        new_log = pd.DataFrame(log_data)
        combined = pd.concat([existing, new_log], ignore_index=True)
    else:
        combined = pd.DataFrame(log_data)

    combined.to_excel(LOG_PATH, index=False)
    return f"已记录工单{ticket_id}"


# ========== 惩罚机制 ==========

def punish_handler(name, reason):
    """将处理人加入黑名单"""
    all_sheets = pd.read_excel(EXCEL_PATH, sheet_name=None)
    for sheet_name, df in all_sheets.items():
        for i, row in df.iterrows():
            if row['姓名'] == name:
                all_sheets[sheet_name].at[i, '黑名单'] = '是'
                break
    with pd.ExcelWriter(EXCEL_PATH, engine='openpyxl') as writer:
        for sheet_name, df in all_sheets.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    return f"已将{name}加入黑名单，原因：{reason}"


def check_punishment(ticket_id, actual_urgency):
    """检查是否需要惩罚：实际紧急程度与上报差两级以上则惩罚"""
    if not os.path.exists(LOG_PATH):
        return "无历史记录"

    logs = pd.read_excel(LOG_PATH)
    match = logs[logs['工单ID'] == ticket_id]
    if match.empty:
        return "未找到工单记录"

    reported_urgency = int(match.iloc[0]['紧急程度'])
    handler = match.iloc[0]['处理人']

    if abs(reported_urgency - actual_urgency) >= 2:
        return punish_handler(handler, f"误报：上报{reported_urgency}级，实际{actual_urgency}级")
    return f"评估通过，上报{reported_urgency}级，实际{actual_urgency}级，误差在允许范围内"
