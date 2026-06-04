from xml.dom.minidom import ProcessingInstruction

from Tools.scripts.verify_ensurepip_wheels import print_notice

print(100+200)
print(5>3 or 3<1)
print(5>3 and  3<1)
print(5>3 and  not 3<1)
print(not True)
print('==========================================')
a='ABC'
b=a
a='XYZ'
print(b)
a='ABC'
a='XYZ'
b=a
print(b)
print('==========================================')
print('我是\n胡文雨')
print('==========================================')
n=123
f=456.789
s1='Hello world'
s2='hello \'Adam\''
s3=r'Hello,"Bart"'
s4=r'''Hello,
Bob!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)