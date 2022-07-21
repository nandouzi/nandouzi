import random

lit=[i for i in range(1,10)]
print(lit)

#随机生成10个1~100内的数
lit1=[random.randint(1,100) for _ in range (10)]
print(lit1)

#生成0~10以内的偶数
lit2=[i for i in range(10) if i%2==0]
print(lit2)