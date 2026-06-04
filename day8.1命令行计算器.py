#1. 命令行计算器
#别看它简单，这是检验你是否真的能独立写代码的试金石。
#你的任务：写一个程序，运行时让用户输入两个数字和运算符号（+、-、*、/），然后输出结果。
from operator import truediv
#进阶要求：
#处理异常：用户输入字母而非数字怎么办？除法时输入0怎么办？（这是try...except的实战）
#持续运行：计算完一次后，程序不退出，而是问用户“是否继续？（y/n）”，这练习了while循环。
#关键点：这个项目做好了，你对input、if分支、while循环和基本错误处理的理解会非常扎实。
from urllib.request import install_opener

#a = int(input('请输入第一个数字：'))
#b = int(input('请输入第二个数字：'))
#c = input('请选择符号（+、-、*、/）：')
#if c == '+':
    #print('答案是：',a+b)
#elif c == '-':
   # print('答案是：',a-b)
#elif c == '*':
    #print('答案是：',a*b)
#elif c == '/':
    #print('答案是：',a/b)

#d = input('您是否还要继续：y/n')

while True:
    while True:
        try:
            a = float(input('请输入第一个数字：'))
            break
        except ValueError:
            print('输入错误')

    while True:
        try:
            b =float(input('请输入第二个数字：'))
            break
        except ValueError:
            print('输入错误')

    while True:
        c = input('请选择符号（+、-、*、/）：')
        if c in ['+','-','*','/']:
            break
        else:
            print('输入错误')

    if c == '+':
        print('答案是：', a + b)
    elif c == '-':
        print('答案是：', a - b)
    elif c == '*':
        print('答案是：', a * b)
    elif c == '/':
        if b == 0:
            print('除数不为0')
        else:
            print('答案是：', a / b)

    choice = input('是否继续：y/n')
    if choice == 'y':
        continue
    else:
        print('感谢')
        break