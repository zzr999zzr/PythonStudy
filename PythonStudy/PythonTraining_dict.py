# !/usr/bin/python3
# !-*- coding:utf-8 -*-
# Author: Alfa
# Time   : 2018/4/9 15:01

"""
字典dictionary练习
增删改查
"""

# 创建字典
dict1 = {'test': 3, '缓缓': 'yyyy', 1: 'gggg'}
print(dict1)  # {'test': 3, '缓缓': 'yyyy', 1: 'gggg'}

dict2 = dict((('a', 'b'),))
print(dict2)  # {'a': 'b'},当只有一个键值对时，最后要添加一个逗号“，”


# 增加
dict3 = {}
dict3['name'] = 'Alfa'
dict3['Age'] = 35
print(dict3)  # {'name':'Alfa','Age':35} 直接给键赋值就可以增加字典中键值对

a = dict3.setdefault('Weight', '偏重')
b = dict3.setdefault('High', 180)
c = dict3.setdefault('name', 'shine')
print(a, b, c)  # a = '偏重' b = 180 c = 'Alfa'
# 使用setdefault方法，当键不存在原来字典中时，就新增该键值对，并返回新增的值
# 使用setdefault方法，当键存在原来的字典中时，就不做任何修改，并且返回现有的键对应的值
print(dict3)  # {'name': 'Alfa', 'Age': 35, 'Weight': '偏重', 'High': 180}


# 查询
print(dict3['name'])
# print(dict3['names'])

print(dict3.get('Age', True))
print(dict3.get('Ages'))
print(dict3.get('Ages', False))  # get方法，当查找到键时，返回键的值，没有查找到时，返回后面的True、False,如果没有参数，返回None


print(dict3.items())  # dict_items([('name', 'Alfa'), ('Age', 35), ('Weight', '偏重'), ('High', 180)])
print(dict3.keys())  # dict_keys(['name', 'Age', 'Weight', 'High'])
print(dict3.values())  # dict_values(['Alfa', 35, '偏重', 180])


print('name' in dict3)
print(list(dict3.items()))
print(list(dict3.keys()))
print(list(dict3.values()))


# 修改
dict3['name'] = 'shine'
dict4 = {'sex': 'male', 'hoppy': 'money', 'Age': 31}
dict5 = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
dict3.update(dict4)
dict3.update(dict5)
print(dict3)
print(dict4)
print(dict5)


# 删除

dict4.clear()
print(dict4)

del dict3['hoppy']
print(dict3)

a = dict3.popitem()
print(a, dict3)


dict3.pop('Age')
print(dict3)

del dict5
# print(dict5)


# 其他方法
# dict.fromkeys()   sorted(dict)
# dict.fromkeys() 可以初始化第一个参数作为键，使用第二个参数为值
dict6 = dict.fromkeys(['a', 'b', 'c', 'd'], 'test')
print(dict6)  # {'a': 'test', 'b': 'test', 'c': 'test', 'd': 'test'}

dict7 = dict.fromkeys(['a', 'b', 'c', 'd'], ['test', 'abcd'])
print(dict7)

# 修改了一个值，所有都修改了
dict7['a'][0] = 'TEST'
print(dict7)  # {'a': ['TEST', 'abcd'], 'b': ['TEST', 'abcd'], 'c': ['TEST', 'abcd'], 'd': ['TEST', 'abcd']}


# 返回包含字典所有键的有序列表 sorted(dict)

dict8 = {3: '111', 5: '222', 1: '333', 4: '444', 2: '555'}
a = sorted(dict8)
b = sorted(dict8.values())
c = sorted(dict8.keys())
print(a)  # [1, 2, 3, 4, 5]
print(b)  # ['111', '222', '333', '444', '555']
print(c)  # [1, 2, 3, 4, 5]








