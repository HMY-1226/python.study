#做一个命令行通讯录，支持以下功能：
from urllib.request import install_opener

from pip._internal.resolution.resolvelib import found_candidates

#添加联系人（姓名、电话）
#查看所有联系人
#搜索联系人（按姓名）
#删除联系人（按姓名）
#退出程序

contacts = []
while True:
    print('\n1.添加联系人')
    print('2.查看所有联系人')
    print('3,搜索联系人')
    print('4.退出')
    choice = input('请选择:')
    if choice == '1':
        name = input('请输入姓名(q退出):')
        if name == 'q':
            break
        phone = input('请输入电话:')
        contact = {"name":name,"phone":phone}
        contacts.append(contact)
        print('添加成功')
    elif choice == '2':
        if len(contacts) == 0:
            print('空')
            break
        else:
            for c in contacts:
                print(f'姓名：{c["name"]}，电话：{c["phone"]}')
    elif choice == '3':
        c = input('请输入联系人:')
        Found = False
        for contact in contacts:
            if contact['name'] == c:
                contact["phone"] = input('请输入新手机号') #这里的[]表示 从字典里按键名取/改值  很诡异
                print('修改成功')
                Found = True
                break
            if not Found:
                print('联系人不存在')
    elif choice == '4':
        print('再见')
        break