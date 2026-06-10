import os
import json
import requests
import shutil

API_KEY = 'sk-。。。。。'
URL = "https://api.deepseek.com/v1/chat/completions"


CATEGORIES = {
    ".jpg": "图片", ".jpeg": "图片", ".png": "图片",
    ".gif": "图片", ".bmp": "图片", ".svg": "图片",
    ".pdf": "文档", ".docx": "文档", ".doc": "文档",
    ".txt": "文档", ".xlsx": "文档", ".pptx": "文档", ".md": "文档",
    ".mp3": "音频", ".wav": "音频", ".flac": "音频", ".aac": "音频",
    ".mp4": "视频", ".avi": "视频", ".mkv": "视频", ".mov": "视频",
    ".zip": "压缩包", ".rar": "压缩包", ".7z": "压缩包",
    ".py": "代码", ".js": "代码", ".html": "代码", ".css": "代码",
}

# ========== 核心功能 ==========

response  = requests.post(URL, headers={'Authorization': f"Bearer {API_KEY}"},json = {"model":"deepseek-chat","messages":[{"role":"user","content":"你好"}]})
print(response.json()["choices"][0]["message"]["content"])

message = [{"role":"system","content":"你是一个友好的AI助手"}]
print('=========AI聊天机器人==========')
print('输入quit退出对话')
print("=============================")

def organize_folder(folder_path):
    if not os.path.exists(folder_path):  #判断是否存在   os.path  是python用来记录文件路径专用的  exists是存不存在     isdir是不是文件夹    join把路径和文件名拼在一起，自动用正确的斜杠
        return  f"文件不存在：{folder_path}"

    moved = 0
    skipped = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            skipped += 1
            continue
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        category = CATEGORIES.get(ext,"其他")

        category_path = os.path.join(folder_path, category)
        if not(os.path.exists(category_path)):
            os.makedirs(category_path)
        destination_path = os.path.join(category_path, filename)
        shutil.move(file_path , destination_path)
        moved += 1
    return f"整理完成！共移动{moved}个文件到对应分类，跳过{skipped}个文件夹"
def main():
    print("===== AI 文件归类助手 =====")
    print("告诉我你要整理哪个文件夹，比如：")
    print("  - 帮我整理 D:/Downloads")
    print("  - 把 C:/Users/我的/Desktop 的文件归一下类")
    print("输入 quit 退出")
    print("===========================")

    system_prompt = f"""你是一个文件归类助手。你可以帮用户整理文件夹，把文件按后缀名自动分类。

你可以执行的操作：
1. organize - 整理文件夹（需要参数：path，即文件夹路径）

当前支持的文件类别：
{json.dumps(CATEGORIES, ensure_ascii=False)}

重要规则：
- 如果用户给出了明确的文件夹路径，直接返回 JSON。
- 如果用户只说"整理一下"但没有指定路径，就追问用户。
- 路径可以是绝对路径（如 D:/Downloads）或相对路径（如 ./test）。

当信息齐全时返回 JSON：{{"action": "organize", "params": {{"path": "文件夹路径"}}}}
需要追问时，用自然语言回复。"""
    messages = [{"role": "system", "content": system_prompt}]

    while True:
        user_input = input("\n你：")
        if user_input.lower() == "quit":
            print("再见！")
            break

        messages.append({"role": "user", "content": user_input})

        response = requests.post(
            URL,
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={"model": "deepseek-chat", "messages": messages}
        )

        ai_reply = response.json()["choices"][0]["message"]["content"]

        try:
            action_data = json.loads(ai_reply)
            action = action_data["action"]
            params = action_data["params"]

            if action == "organize":
                result = organize_folder(params.get("path", ""))
                print(result)
            else:
                print(f"未知操作：{action}")

        except:
            # 不是 JSON，直接显示 AI 回复（追问或闲聊）
            print(ai_reply)

if __name__ == "__main__":
    main()
