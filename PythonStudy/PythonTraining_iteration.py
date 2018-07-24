# !/usr/bin/python3
# !-*- coding:utf-8 -*-
# Author : Alfa
# Time : 2018/7/24 22:09


"""
迭代器练习
"""

# 满足迭代器协议 1,内部有next()方法  2,内部有iter() 方法


l = [1,2,3,4] # list是一个可迭代对象Iterable
i = iter(l) # 调用可迭代对象的iter方法,可以生成一个可迭代器

# 迭代器方法
next(i)


# for 循环内部三件事
# 1.调用对象的iter()方法,返回一个迭代器对象
# 2.使用while循环调用next()方法
# 3.使用try except 捕获 StopIteration错误,跳出while循环






















