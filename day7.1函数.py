#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
#举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：
#fact(n)=n!=1×2×3×⋅⋅⋅×(n−1)×n=(n−1)!×n=fact(n−1)×n
#所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理
import numbers


def fact(x):
    if x == 1:
        return 1
    return x * fact(x-1)
print(fact(5))
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
#栈（一摞盘子）      栈帧（每个盘子）
#─────────────────────────────
#│  fact(1)   │ ← 最上面（最后调用）
#│  fact(2)   │
#│  fact(3)   │ ← 最下面（最先调用）
#└────────────┘
print('-----------------------------------------------------')
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
   # while num > 1:
        product *= num
        num -= 1
    #return product # while 版本
    return fact_iter(num - 1, num * product)
print('-----------------------------------------------------')
def move(n, a, b, c):
    if n == 1:
        print(a, "->", c)
    else:
        move(n-1, a, c, b)
        print(a, "->", c)
        move(n-1, b, a, c)

print(move(5,'A起点','B辅助','C终点'))
