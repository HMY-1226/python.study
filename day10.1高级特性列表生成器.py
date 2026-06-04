#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
#如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
#方法一
from operator import index

l = []
for x in range(1,11):
    l.append(x * x)

print(l)
#方法二
print([x*x for x in range(1,11)])
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
print([x * x * x for x in range(1,11)])
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x * x  for x in range(1,11) if x % 2 == 0])
#还可以使用两层循环，可以生成全排列
print([a + b for a in 'ABC' for b in 'XYZ'])
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4'}
for k,v in d.items():
    print(k,v)
#方法二
d = {'a' : '1', 'b' : '2', 'c' : '3', 'd' : '4'}
print([k +'='+ v for k,v in d.items() if v == '1']) # 因为 + 是字符串拼接，两边必须都是字符串
#一、[表达式 for 变量 in 可迭代对象 if 条件]
# 选出偶数
nums = [1, 2, 3, 4, 5, 6]
result = [x for x in nums if x % 2 == 0]
print(result)   # [2, 4, 6]
#二、[表达式1 if 条件 else 表达式2 for 变量 in 可迭代对象]
# 偶数不变，奇数变成 0
nums = [1, 2, 3, 4, 5, 6]
result = [x if x % 2 == 0 else 0 for x in nums]
print(result)   # [0, 2, 0, 4, 0, 6]
#三、[表达式1 if 条件1 else 表达式2 for 变量 in 可迭代对象 if 条件2]
# 选出偶数，偶数 > 4 的变成 '大'，其他偶数保持不变
nums = [1, 2, 3, 4, 5, 6]
result = ['大' if x > 4 else x for x in nums if x % 2 == 0]
print(result)   # [2, 4, '大']