#杨辉三角
def func1(n):
    row = [1]
    for i  in range(n):
        print(row)
        row = [row[j] + row[j+1] for j in range(len(row)-1)]
        row = [1] + row + [1]
    return ""
print(func1(5))