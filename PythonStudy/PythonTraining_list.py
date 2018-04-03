#!/usr/bin/python3
#!-*- coding:utf-8 -*-
#Author:Alfa
#Time   : 2018/3/30 15:46

"""
list的增删改查

type(a) is list  判断 a 是否是 list
"""

a = ['2', '1', '3', '4', '5', '3', '0', '8', '7']

#查询
"""count  查询某个元素的出现次数 a.count("alfa")
index  根据元素内容获取对应元素位置下标值 a.index()
in     判断元素是否在列表里"alfa" in a[.....]
"""

print(a.count('3'))
print(a.index('5'))

print('9' in a)
print('0' in a)

#增加
"""
append 追加元素到列表最后  a.append("alfa")
insert 指定位置插入列表元素 a.insert(index, "alfa"）
extend 扩展列表，把一个列表内容插入到另一个列表 a.extend()
"""
a.append("6")
print(a)

a.insert(0, '12')
print(a)
a.insert(6, '21')
print(a)

b = ['a', 'b', 'c', 'd']
a.extend(b)
print(a)
print(b)
b.extend(a)
print(a)
print(b)


#删除、排序
"""
remove 删除指定元素内容 a.remove("alfa")
pop    删除指定下标元素 a.pop(index)，如果没有下标默认删除列表最后一位元素内容 a.pop()
del    删除列表，删除指定下标元素  del a  del a[index]
clear  清空列表 a.clear()

sort() 排序，按照ask码顺序 从小到大，sort方法中可以添加参数reverse=True 直接从小到大排序后再从大到小排序显示
reverse() 排序，按照之前的列表内容顺序，从后面到前面排序显示，最后面的变成第一位显示
"""

a.remove('21')
print(a)

a.pop(0)
print(a)

a.sort()
print(a)
a.sort(reverse=True)
print(a)

print(b)
b.reverse()
print(b)













