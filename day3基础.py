#insert键改变光标模式
classmates=['胡文雨','胡英俊','胡图图']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[:2])
classmates.append('烟头叔叔')#list中追加元素到末尾
print(classmates)
classmates.insert(1,'围裙妈妈')#可以把元素插入到指定的位置
print(classmates)
classmates.pop(0)#删除指定位置的元素
print(classmates)
#list里面的元素的数据类型也可以不同
x=['Apple','123',True]
print(x)
y=['Python','java',['asp','php',['胡文雨']]]
print(y)
print(len(y))
print(y[0])
print(y[1])
print(y[2])
print('------------------------------------------------------')
#tuple和list非常类似，但是tuple一旦初始化就不能修改
age=(23,54,38)
print(age)
t1=()
print(t1)
t2=(1)
print(t2)
t3=(1,)
print(t3)#t2和t3有区别   2是一个数字 3是tuple  因为小括号算数学公式里的符号  所以产生歧义 用逗号隔开
t4=('a','b',['A','B'])
t4[2][0]='x'
t4[2][1]='y'
print(t4)
print('------------------------------------------------------')
#请用索引取出下面list的指定元素
L = [['Apple', 'Google', 'Microsoft'],['Java', 'Python', 'Ruby', 'PHP'],['Adam', 'Bart', 'Bob']]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Bob:
print(L[2][2])