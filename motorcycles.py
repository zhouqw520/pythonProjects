#列表
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

#修改列表元素
motorcycles[0] = 'ducati'
print(motorcycles)

#添加列表元素
motorcycles.append('aima')
print(motorcycles)

motorcycles.insert(1,'huangma')
print(motorcycles)

#删除列表元素
del motorcycles[0]
print(motorcycles)

#pop删除列表元素
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(motorcycles)
print(motorcycles.pop(1))
print(motorcycles)

#remove删除列表元素
motorcycles.remove('huangma');
print(motorcycles)


