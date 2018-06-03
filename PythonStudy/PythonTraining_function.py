#!/usr/bin/python3
#!-*- coding:utf-8 -*-
#Author:Alfa
#Time   : 2018/5/31 11:04

'''
函数练习

'''


# 函数的特效
# 1.代码的重用
# 2.可扩展性
# 3.保持一致性

def fun1(n):
    print("this is function 1")

    with open("函数练习文件", "a", encoding='utf-8') as f:
        f.write("这是方法%s\n" %n)

def fun2(n):
    print("this is function 2")

    with open("函数练习文件", "a", encoding='utf-8') as f:
        f.write("这是方法%s\n" %n)

def fun3(n):
    print("this is function 3")

    with open("函数练习文件", "a", encoding='utf-8') as f:
        f.write("这是方法%s\n" %n)


# fun1(1)
# fun2(2)
# fun3(3)

# 以上很多重复代码，重复写入文件
# 代码重用

def write_file(n):
    print("this is function %s" %n)
    with open("函数练习文件", "a", encoding='utf-8') as f:
        f.write("这是方法%s\n" %n)



def func1(n):
    write_file(n)

# func1(1)
# func1(2)
# func1(3)

# 可扩展性
# 保持一致性
# 文件输入时，需要添加当前时间内容

import time
def logger(n):
    time_format = "%Y-%m-%d %X"
    current_time = time.strftime(time_format)
    with open("函数练习文件", "a", encoding='utf-8') as f:
        f.write("end time is %s, function is %s" %(current_time, n))


def func2(n):
    logger(n)

# func2(1)


# 函数的参数
# 1.必须参数
# 2.关键字参数
# 3.默认参数
# 4.不定长参数


# 必须参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

def a(name,age):
    print("name:%s,age:%s" %(name, age))

a("哈哈",23)
a(23,"哈哈哈") #实参传入时，就按照形参的顺序位置赋值
# a(23,"哈哈哈",11) # 报错，对应不上形参


# 关键参数
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致
# python解释器可以按照参数关键字匹配参数值

def b(age, name):
    print("age:%d,name:%s" % (age, name))

# b("呵呵", 16) #对应形参age需要int，name需要str 报错
b(16, "ww")
b(name="PP", age=23)


# 默认参数
# 调用函数时，默认参数的值如果没有传入，则被认为是默认值

def c(name, age, sex='male'):
    print("name is %s" %name)
    print("age is %s" %age)
    print("sex is %s" %sex)

c('hehe', 20, 'female')
c('hehe', 20)


# 不定长参数
# 一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数
# 加了星号（*）的变量名会存放所有未命名的变量参数。而加(**)的变量名会存放命名的变量参数
# （*）加了一个星号的，会把传入的参数都放在一个元组中（'bb',13,14,'aa',61,72）
# (**)加了二个星号的，会把传入的参数都放在一个字典中

def add(x,y):
    print(x+y)

add(5,11)


def add_big(*num):
    print(num)
    sum = 0
    for i in num:
        sum += i
    return sum

print(add_big(1,2,3))
print(add_big(1,2,3,4,5,6))



def print_info(**info):
    print(info)
    for i in info:
        print(i+":"+info[i])


print_info(name='alex',age=18,sex='female')





















