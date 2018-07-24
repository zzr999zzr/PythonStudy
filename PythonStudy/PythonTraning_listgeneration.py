# !/usr/bin/python3
# !-*- coding:utf-8 -*-
# Author : Alfa
# Time : 2018/7/12 21:55


"""
列表生成式练习
"""


# 创建一个列表
[1,2,'123','test']


# 列表生成式创建列表
a = [x for x in range(10)]

print(a)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 列表生成式中,可以对前面的变量进行操作
b = [i*i for i in range(5)]
print(b) # [0, 1, 4, 9, 16]

# 列表生成式前面的参数,也可以是一个函数
def f(n):
    return n**3

c = [f(k) for k in range(5)]
print(c) # [0, 1, 8, 27, 64]

























