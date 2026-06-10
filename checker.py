from AItools import check_punishment, read_staff_config
import pandas as pd
import os
from datetime import datetime

# ============================================================
# 旧代码（硬编码绝对路径）：
#   LOG_PATH = "D:/工单日志.xlsx"
#
# 优化后：和 AItools.py 一样，用脚本所在目录定位文件，
#         整个文件夹移动不影响运行。
# ============================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在文件夹路径
LOG_PATH = os.path.join(BASE_DIR, "工单日志.xlsx")      # 日志文件和脚本放一起


def main():
    print("===== 工单事后检查（Agent C）=====")

    if not os.path.exists(LOG_PATH):
        print("暂无工单日志。")
        return

    logs = pd.read_excel(LOG_PATH)
    pending = logs[logs['完成时间'].isna() | (logs['完成时间'] == '')]

    if pending.empty:
        print("所有工单已完成。")
        return

    print(f"待检查工单数：{len(pending)}\n")

    for _, row in pending.iterrows():
        print(f"工单{row['工单ID']}：{row['类别']}，上报紧急程度：{row['紧急程度']}级")
        actual = input("请输入实际紧急程度（1-5，回车跳过）：")

        if actual.strip():
            result = check_punishment(int(row['工单ID']), int(actual))
            print(f"  {result}")

            # 更新完成时间
            logs.loc[logs['工单ID'] == row['工单ID'], '完成时间'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logs.to_excel(LOG_PATH, index=False)

    print("\n检查完成。")


if __name__ == "__main__":
    main()
