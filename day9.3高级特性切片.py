#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
sentence = input('请输入一句要切的话：')
def trim(sentence):
    a = 0
    while a < len(sentence) and sentence[a] == ' ' :
        a += 1

    b = len(sentence) - 1
    while b >= len(sentence) and sentence[b] == ' ':
        b -= 1

    if  a > b :
        return ''
    return sentence[a:b+1]
print(trim(sentence))