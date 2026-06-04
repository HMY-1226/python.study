#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-20))
#如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）

#空函数
def nop():
    pass

import math

def move(x,y,step,angle=0):#step  距离  angle=移动的角度
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
print(move(-20,20,step=math.pi/2))#pi=3.1415926

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程ax*2+bx+c=0 的两个解
#math.sqrt   计算平方根公式
def quadratic(a, b, c):
    delta = b * b - 4 * a * c
    if  delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return [x1, x2]
    elif  delta < 0:
        return "方程式无解"
    return None#此代码作用是编辑器害怕有特殊情况  但是骑士没有别的情况了  无用

print(quadratic(5,10,3))




