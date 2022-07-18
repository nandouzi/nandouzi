lit=['print','sql','zcy']
print ('原列表：',lit,id(lit))

#列表中新增元素的操作
lit.append('stt')
print ('新增元素之后:',lit,id(lit))

#使用insert函数在指定位置上插入元素
lit.insert(3,'admire')
print ('新增元素后：',lit,id(lit))

#列表元素的删除操作
lit.remove('sql')
print('删除后:',lit,id(lit))

#使用pop（）函数先将元素取出，在删除
print(lit.pop(0))
print(lit)

#使用clear（）清除元素
lit.clear()
print(lit,id(lit))

#列表反向
lit1=['i','a','u']
lit1.reverse()
print(lit1,id(lit1))

#列表的拷贝，将产生一个新的列表对象
new_lit=lit1.copy()
print(new_lit,id(new_lit))
print(lit1,id(lit1))

#根据索引修改元素
lit1[1]='admire'
print(lit1,id(lit1))


print(lit2)