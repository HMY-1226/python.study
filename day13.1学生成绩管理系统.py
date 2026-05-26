#功能需求：
#添加学生（姓名 + 语文/数学/英语三科成绩）
#查看所有学生及平均分
#按平均分排序显示（升序或降序）
#找出最高分/最低分的学生
#统计各科平均分、及格率
#成绩数据存到文件里

student = []
def student_app():
    while True:
        name = input('请输入学生姓名(q退出):')
        if name == 'q':
            break
        chinese = float(input('请输入语文成绩:'))
        if chinese > 150 or chinese < 0:
            print('请输入正确的分数(0-150)')
            continue
        math = float(input('请输入数学成绩:'))
        if math > 150 or math < 0:
            print('请输入正确的分数(0-150)')
            continue
        english = float(input('请输入英语成绩:'))
        if english > 150 or english < 0:
            print('请输入正确的分数(0-150)')
            continue
        s = {
            'name':name,
            'english':english,
            'math':math,
            'chinese':chinese
        }
        student.append(s)
    return ''

def show_student(student):
    if len(student) == 0:
        print('无信息')
        return ''
    print('姓名\t语文\t英语\t数学\t平均分')
    print('-' * 40)
    for s in student:
        avg = (s['chinese'] + s['math'] + s['english']) / 3
        print(f"{s['name']}\t{s['chinese']}\t{s['math']}\t{s['english']}\t{avg:.1f}")  #问题   1f  保留一位小数   f'{变量}'  s['name'] 取出s字典里name的值
    return ''

def avg_sort(student):
    order = input('升序（1） or 降序（2） ：')
    if order == '1':
        reverse = False
    elif order == '2':
        reverse = True
    elif order != '1' and order != '2':
        print('请输入正确的排序方式')
    sorted_list = sorted(student , key=lambda s:(s['chinese'] + s['math'] + s['english'])/3, reverse = reverse) #问题  sorted 是排序用的    lamda 是一个匿名函数计算平均数 s 是列表里每个学生的字典
    show_student(sorted_list)
    return ''

def find(student):
    if len(student) == 0:
        print('无信息')
        return
    choice = input('请选择要查询的方向（1、总分）（2、单科成绩）：')
    if choice == '1':
        z_best = max(student, key = lambda s: s['math'] + s['english'] +s['chinese'])
        total_best = z_best['math'] + z_best['english'] + z_best['chinese']
        print(f'最高分：{z_best["name"]}总分：{total_best}')
        z_worst = min(student, key = lambda s: s['english'] +s['chinese'] +s['math'])
        total_worst = z_worst['math'] + z_worst['english'] + z_worst['chinese']
        print(f'最低分：{z_worst["name"]}总分：{total_worst}')
    elif choice == '2':
        for subject in ['chinese', 'math', 'english']:
            best = max(student,key = lambda  s: s[subject]) # 问题
            worst = min(student,key = lambda s: s[subject])
            print(f'{subject}最高分：{best["name"]}({best[subject]})最低分:{worst["name"]}({worst[subject]}))')#问题
    return ''

def statistics(student):
    if len(student) == 0:
        print('无信息')
        return
    for subject in ['math', 'english' , 'chinese']:
        scores = [s[subject] for s in student]
        avg = sum(scores) / len(scores)
        pass_count = sum(1 for s in scores if s >= 60)
        pass_rate = pass_count / len(scores) *100
        print(f'{subject} , 平均分= {avg:.1f} ,及格率= {pass_rate:.1f}%') # 问题
    return ''

while True:
    j = (input('a、添加学生\nb、查看所有学生及平均分\nc、按平均分排序显示\nd、统计各科平均分、及格率\ne、成绩数据存到文件里\nf、找出最高分/最低分的学生\n请选择功能(q退出)：'))
    if j == 'a':
        student_app()
        continue
    elif j == 'b':
        show_student(student)
    elif j == 'c':
        avg_sort(student)
    elif j == 'd':
        find(student)
    elif j == 'e':
        statistics(student)
    elif j == 'q':
        break


