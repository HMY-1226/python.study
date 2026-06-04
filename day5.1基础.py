#Python的循环有两种，一种是for...in循环
name = ['胡英俊','胡图图','烟头叔叔']
for i in name:#所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
    print(i)
sum = 0
for x in [1,2,3,4,5]:
    sum += x #同等与sum = sum + x
print(sum)
print(list(range(1,6)))
print(list(range(101)))
sum1 = 0
for i in range(101):
    sum1 += i
print(sum1)
print('------------------------------------------------------------')
#第二种循环是while循环
sum2 = 0
n = 99
while n > 0:
    if  n % 2 == 1:
        sum2 += n
    n -= 2
print(sum2)
print('------------------------------------------------------------')
L = ['bart','lisa','adam']
for x in L:
    print('hello',x)
print('------------------------------------------------------------')
#死循环
#while True:
    #print("停不下来了...")
