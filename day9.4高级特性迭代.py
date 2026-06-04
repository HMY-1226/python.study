#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
#请使用迭代查找一个list中最小和最大值，并返回一个tuple
from collections.abc import Iterable #判断是否可迭代

print(isinstance(10,Iterable))
print(isinstance('abc',Iterable))
print(isinstance([123],Iterable))
def findMinandMax():
    l = []
    while True:
        a = input('请输入数字(q退出):')
        if a == 'q':
            break
        l.append(int(a))
    return (min(l),max(l))
print(findMinandMax())
#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()