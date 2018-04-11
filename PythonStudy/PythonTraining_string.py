# !usr/bin/env python3  
# -*- coding:utf-8 _*-  
# author: Alfa
# file: PythonTraining_string.py 
# time: 2018/04/11 23:06

"""
练习字符串的各种方法
"""

# join 拼接方法
a = ''
a1 = '---'
b = '3456'
c = 'abcd'
d = 'ttee3344'
e = 'a is A b is {name}'
f = 'a is A b is {name} c is {age}'
print(a.join([b, c]))  # 3456abcd
print(a1.join([b, c]))  # 3456---abcd
print(a1.join([b, c, d]))  # 3456---abcd---ttee3344

# count() 返回字符串中相同的字符个数
print(d.count('t'))  # 2

# capitalize() 把字符串首字母大写
print(d.capitalize())  # Ttee3344

# center() 一共打印多少个字符，除了居中显示字符串内容后，其他用后面的字符串内容补充
print(d.center(30, '*'))  # ***********ttee3344***********

# endswith()  # 以指定字符串结尾，返回true 否则返回false
print(d.endswith('4'))  # True
print(d.endswith('44'))
print(d.endswith('5'))  # False

# find() 查找到第一个指定的字符，并返回索引值
print(d.find('3'))  # 4

# format() 格式化输出的另一种方法
print(e.format(name='Y'))  # a is A b is Y
print(f.format(name='Y', age=99))  # a is A b is Y c is 99
print(e.format_map({'name': "Q"}))  # a is A b is Q
print(f.format_map({'name': "Q", 'age': 88}))  # a is A b is Q c is 88






































