''''-------*---------'''
''''------***---------'''
''''-----*****----------'''
''''----*******-----------'''
''''----------------'''
''''----------------'''

for i in range(1,6):    #倒三角形
    for j in range(1,6-i):
        print(' ',end='')    #单引号之间是空格
    for l in range(1,i*2):
      print('*',end='')
    print('')  #换行操作





