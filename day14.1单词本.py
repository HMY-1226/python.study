#功能需求：
#添加单词（英文 + 中文释义）
#查看所有单词（分页显示，每页5个）
#背单词模式：随机显示一个英文，用户输入中文，判断对错并记录答对次数
#按答错次数排序（错最多的优先复习）
#用生成器 yield 实现批量导出单词
import random


words = []
def add_word():
    while True:
        word = input('请输入单词（q退出）：')
        if word == 'q':
            break
        chinese = input('请输入中文释义：')
        s = {
            '单词':word,
            '中文':chinese,
            '正确':0,
            '错误':0
        }
        words.append(s)
    return words

def show_page(page):
    if len(words) == 0:
        print('无单词')
        return
    start = (page - 1) * 5
    end = start + 5
    page_words = words[start:end]
    for s in page_words:
        print(s['英文'],'-',s['中文'])

def study(words):
    if len(words) == 0:
        print('无单词')
        return
    while True:
        w = random.choice(words)
        answer = input(f'\n{w["单词"]}的中文是：（q退出）')
        if answer == 'q':
            break
        if answer == w['中文']:
            print('正确')
            w['正确'] += 1
        else:
            print(f'错误,正确答案是{["中文"]}')
            w['错误'] += 1

def sort_by_wrong(words):
    if len(words) == 0:
        print('无单词')
        return
    sorted_words = sorted(words,key=lambda w : w['wrong'],reverse=True)
    print('\n错误最多的单词：')
    print('英文\t中文\t错误次数')
    for w in sorted_words:
        if w['wrong'] > 0:
            print(f'{w["english"]}\t{w["chinese"]}\t{["wrong"]}')
    pass

def exports_words(words,batch_size=5):
    for i in range (0,len(words),batch_size):
        yield words[i:i+batch_size]
    if len(words) == 0:
        print('无单词')
        return
