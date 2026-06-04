#任务：让用户输入一个字符串，统计其中每个字符（不包括空格）出现的次数，结果存到字典里，最后打印出来。

a = input('请输入要统计的字符串：')
c = {}
for i in a:
    if i == '':
        continue
    if i in c:
        c[i] += 1  #使 value +1
    else:
        c[i] = 1  #像字典里添加  i : 1
print(c)
