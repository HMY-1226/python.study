l = []
while True:
    num = input('请输入要添加排序的数字：')
    if num == 'q':
        break
    l.append(num)
print('你输入的数字是',l)

n = len(l)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if  l[j] > l[j + 1]:
            l[j],l[j + 1] = l[j + 1],l[j]

print([l])