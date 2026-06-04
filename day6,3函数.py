def power(x):
    return x*x
print(power(5))

def power1(x):
    return x*x*x
print(power(5))

def power2(x,n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s

print(power2(5,10))

#定义默认参数要牢记一点：默认参数必须指向不变对象
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    return name, gender, age, city
print(enroll('胡英俊','Famle',))

def add_end(L = []):
    L.append("END")
    return L
print(add_end())
print(add_end())#默认参数必须指向不变对象
print('---------------------------------------------------------------')
#要修改上面的例子，我们可以用None这个不变对象来实现
def add_end1(l = None):
    if l is None:
        l = []
    l.append("END")
    return l
print(add_end1())
print(add_end1())
print('---------------------------------------------------------------')
#可变参数
def calc(*numbers):#星号 * 的核心意思是：把多个参数“打包”成一个元组 (tuple),就是为了让你能传入任意多个参数
    sum1 = 0
    for n in numbers:# 为什么不能写一个数字  因为for in  不接受不能循环之物
        sum1 += n * n
    return sum1
print(calc(range(5)))#调用的时候给一个list或者tuple  或者range
print('---------------------------------------------------------------')
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    return name
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))
print('---------------------------------------------------------------')
#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
def mul(x,y):
    return x * y

def mul1(*numbers):#星号表示可变参数，会把传入的所有参数打包成一个元组
    if len(numbers) == 0:
        return None
    result  = 1
    for n in numbers:
        result = result * n
    return result
