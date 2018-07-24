# !/usr/bin/python3
# !-*- coding:utf-8 -*-
# Author : Alfa
# Time : 2018/7/12 22:05

"""
生成器练习
"""

# 创建生成器的方式
a = (x*2 for x in range(10))  # a就是生成器对象 generator object

def f():
    print('有yield,就是创建了一个生成器对象')
    b = yield 3
# f() 就是一个生成器 generator object

# 生成器在创建的时候,已经决定了能计算出的值得个数,调用方法next()时,超过范围,报错stopIteration

# 生成器的2个方法
# next()   send()
next(f())
next(a)

f().send(None) # 等价于 next(f())
# send方法 第一次不能传值
a.send(None)













































