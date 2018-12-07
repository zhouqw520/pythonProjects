#字符串的使用

name = "aDa lovelace"

#首字母大写
print(name.title())
#全部大写
print(name.upper())
#全部小写
print(name.lower())

#字符串拼接
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

#制表符或换行符
#\t  四个空格
#\n  换行
print("Python")
print("\tPython")
print("Language:\nPython\nC\nJavaScript")
print("Language:\n\tPython\n\tC\n\tJavaScript")

#删除字符串中空格
favorite_language = '  python  '
print(favorite_language)
#去掉左边空格
print(favorite_language.lstrip())
#去掉右边空格
print(favorite_language.rstrip())
#去掉左右两边空格
print(favorite_language.strip())
