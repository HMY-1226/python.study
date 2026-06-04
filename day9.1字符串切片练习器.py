#字符串切片练习器
#任务：让用户输入一句话和一个数字n，程序输出这句话的前n个字、后n个字，以及从第2个字到倒数第2个字中间的部分
sentence = input('请输入一句话：')
while True:
    choice = input('请选择从前向后还是从后向前或者中间或者退出1/2/3/4：')
    if choice == '1':
        n = int(input('请输入数字：'))
        print(sentence[0:n])
        continue
    elif choice == '2':
        n = int(input('请输入数字：'))
        print(sentence[-n:])
        continue
    elif choice == '3':
        n1 = int(input("请输入第一个数字："))
        n2 = int(input('请输入第二个数字:'))
        print(sentence[n1:-n2])
        continue
    elif choice == '4':
        break