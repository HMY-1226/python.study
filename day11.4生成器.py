#在Python中，这种一边循环一边计算的机制，称为生成器：generator
#斐波那契数列(后一个数使前两个数的相加)


def fib(i):
    n , a , b = 0 , 0 , 1
    while n < i :
        print(b)
        a , b = b , b + a
        n += 1
    return ''
print(fib(10))
