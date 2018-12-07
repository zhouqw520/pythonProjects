#创建一个列表，其中包含前10个整数（即1~10）的平方
squares = []
for value in range(1,11):
	square = value **2
	squares.append(square)
	
print(squares)

print(repr(max(squares))+" "+repr(min(squares))+" "+repr(sum(squares)))

#数值转换为字符串
a = 5
print(a)
print("转换为字符串："+str(a))
print("转换为字符串："+repr(a))


