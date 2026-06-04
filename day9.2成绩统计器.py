#成绩统计器
#任务：用户不断输入学生分数，输入q结束。然后输出：最高分、最低分、平均分、及格人数（60分及以上）
from dis import show_code

list1 = []
while True:
    score = input('请输入成绩(输入q退出)')
    if  score == 'q':#先判断   再改成int   添加在判断以后添加
        break

    score = int(score)
    if score > 100:
        print('错误最高分为100')
        continue
    if score < 0:
        print('不能小于0')
        continue
    list1.append(score)
if len(list1) > 0 :
    print('最高分：',max(list1))
    print('最低分',min(list1))
    print('平均分',sum(list1)/len(list1))

    county = 0
    for c in list1:
        if c >= 60:
            county += 1
    print('及格人数',county)
else:
    print('没有任何分数')

