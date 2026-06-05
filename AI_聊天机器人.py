
import requests  #引入网络请求库，用来给api服务器发消息

API_KEY = '填你的api就行'
URL = "https://api.deepseek.com/v1/chat/completions"

response  = requests.post(URL, headers={'Authorization': f"Bearer {API_KEY}"},json = {"model":"deepseek-chat","messages":[{"role":"user","content":"你好"}]})
#上面这一行除了后面的content能变 还有前面的response这个是变量名随便写， 其他的都是固定的 背过就行  下面解释这一行
#1、requests.post(URL..) 这个是向服务器发送请求的固定搭配   2、headers={'Authorization': f"Bearer {API_KEY}"}  请求信息的”身份证“ ，Authorization固定写法 表示这是验证信息,f"Bearer {API_KEY} 这个Bearer是认证方式，后面是密钥也是固定的，抄就行。
#3、json = {"model":"deepseek-chat","messages":[{"role":"user","content":"你好"}]}  json就是纯文本格式的数据转化， 模型 、发给AI的消息列表  角色是"用户" 内容是“你好”
print(response.json()["choices"][0]["message"]["content"])
#层层挖掘  不好看懂  背过就行  可能不同的模型  choices这个地方要变一下

message = [{"role":"system","content":"你是一个友好的AI助手"}]
print('=========AI聊天机器人==========')
print('输入quit退出对话')
print("=============================")
while True:
    user_input = input("\n你：")
    if user_input.lower() == "quit":  #lower 转化成小写
        print('AI:再见！')
        timestamp = datetime.now().strftime("%Y-%m-%d %H_%M_%S")   #获取当前时间    后面乱码是格式化成20260604_153022 这种格式  切记windows系统的时间不能用冒号  得用下划线
        filename = f"chat_{timestamp}.txt" #这就是文件名  就是chat_20260604_153022
        with open(filename,'w',encoding="utf-8") as f:   #  “w”表示写入模式（write）   with-as f   就是启动一个上下文管理器来管理这个文件  open是打开文件  as-f  是把打开文件赋值给f  所以后面都是f.write
            for i in message:   #遍历message列表 根据角色写入不同的前缀
                role = i["role"]
                content = i["content"]
                if role == "system":
                    f.write(f"[系统设定]{content}\n")
                elif role == "user":
                    f.write(f"[用户]{content}\n]")
                elif role == "assistant":
                    f.write(f"[AI]{content}\n")
        print(f"对话保存在{filename}")

    message.append({"role":"user","content":user_input})
    response = requests.post(URL,headers= {'Authorization': f"Bearer {API_KEY}"},json={"model":"deepseek-chat","messages":message})
    ai_reply = response.json()["choices"][0]["message"]["content"] #这条我看不明白  懂的 可以给我解释一下
    message.append({"role":"assistant","content":ai_reply})
    print(f"AI:{ai_reply}")

