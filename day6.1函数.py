#%%
x = float(input('请输入圆的半径：'))
def area_of_circle(x):
    return 3.14 * x * x
print(area_of_circle(x))
#%%
print('----------------------------------------------------')
#%%
print(abs(-20))#绝对值函数
print(max(1,2,3,4,5,0))#输出最大值
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(bool(1))
print(bool(''))
#%%
#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
x1 = input('输入转化的数字：')
result = hex(int(x1))
print(result)