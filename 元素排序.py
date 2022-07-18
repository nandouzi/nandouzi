#元素排序

"--------------元素升序(先大写后小写)------------------"
lit=['F','W','H','c','e','a']
lit.sort()
print(lit)

#或

lit.sort(reverse=False)
print(lit)

"----------------元素降序（先小写后大写）----------------"
lit.reverse()
print(lit)

"----------------忽略大小写进行排序---------------------"
lit.sort(key=str.lower)
print(lit)