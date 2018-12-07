#排序
#永久性排序
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#反序排序
cars.sort(reverse=True)
print(cars)


#临时性排序
cars=['bmw','audi','toyota','subaru']
print(sorted(cars))
print(cars)

#反序排序
print(sorted(cars,reverse=True))
print(cars)

#倒着打印列表
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print(cars)

#长度
cars=['bmw','audi','toyota','subaru']
print(len(cars))
