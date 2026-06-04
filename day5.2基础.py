#Python内置了字典：dict的支持，dict全称dictionary，
#在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
from os import popen

from 学习 import day3基础

names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

d = {'Michael':95, 'Bob':86, 'Tracy':92}
print(d['Michael'])
print(d['Bob'])
print(d['Tracy'])
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['adam'] = 67
print(d['adam'])
#由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print('Jack' in d)
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(d)
d.pop('Jack')
print(d)
#在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key
#key = [1, 2, 3]
#d[key] = 'a list'
#Traceback (most recent call last):
  #File "<stdin>", line 1, in <module>
#TypeError: unhashable type: 'list'
print('--------------------------------------------------------------------------------------------')
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
s = {1,2,3}
print(s)
s1 = set([1,2,3])
print(s1)
s2 = {1,1,2,2,3,3}#重复元素在set中自动被过滤
print(s2)
s2.add(4)#一次加一个
print(s2)
s2.update([4, 5])#update 加一批
print(s2)
s2.remove(4)
print(s2)
print('--------------------------------------------------------------------------------------------')
#tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果
d1 = {}
d1[(1,2,3)] = 'a tuple'
print(d)

s = set()
s.add((1,2,3))
print(s)

d2 = {}
d2[(1,[2,3])] = '有问题'
print(d2)

s2 = ()
s.add((1,[2,3]))
print(s2)
