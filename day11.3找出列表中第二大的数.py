#任务：在一个数字列表中，找出第二大的数字。不能用 max() 和 sort()，自己用循环和条件判断实现。
l = [1,1,2,2,3,3,5,6,1,3,4,2,1,1,9,]
a = 0
b = -1
for i in l:
    if i > a:
        b = a
        a = i
    else:
        if i > b:
            b = i
        else:
            continue

print(a)
print(b)

