'''-------------模拟实现登录---------------'''
i=0
while i<3:
    zh = input("请输入账号")
    mm = input("请输入密码")
    if zh=='zcy' and mm=='111':
        print("密码正确")
        break
    else:
        if i<2:
            print('密码错误,你还有',2-i,'次机会')
        i+=1
if i==3:
    print('对不起，三次均输入错误')
