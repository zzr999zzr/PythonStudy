# !/usr/bin/python3
# !-*- coding:utf-8 -*-
# Author:Alfa
# Time   : 2018/5/31 11:04

'''
函数练习

'''


# 函数的特性
# 1.代码的重用
# 2.可扩展性
# 3.保持一致性

def fun1(n):
    print("this is function 1")

    with open("函数练习文件", "a", encoding='utf-8') as f:
        f.write("这是方法%s\n" % n)

def fun2(n):
    print("this is function 2")

    with open("函数练习文件", "a", encoding='utf-8') as f:
        f.write("这是方法%s\n" % n)

def fun3(n):
    print("this is function 3")

    with open("函数练习文件", "a", encoding='utf-8') as f:
        f.write("这是方法%s\n" % n)


# fun1(1)
# fun2(2)
# fun3(3)

# 以上很多重复代码，重复写入文件
# 代码重用

def write_file(n):
    print("this is function %s" % n)
    with open("函数练习文件", "a", encoding='utf-8') as f:
        f.write("这是方法%s\n" % n)



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
        f.write("end time is %s, function is %s" % (current_time, n))


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

def a(name, age):
    print("name:%s,age:%s" % (name, age))

a("哈哈", 23)
a(23, "哈哈哈")  #实参传入时，就按照形参的顺序位置赋值
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
    print("name is %s" % name)
    print("age is %s" % age)
    print("sex is %s" % sex)

c('hehe', 20, 'female')
c('hehe', 20)


# 不定长参数
# 一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数
# 加了星号（*）的变量名会存放所有未命名的变量参数。而加(**)的变量名会存放命名的变量参数
# （*）加了一个星号的，会把传入的参数都放在一个元组中（'bb',13,14,'aa',61,72）
# (**)加了二个星号的，会把传入的参数都放在一个字典中

def add(x, y):
    print(x + y)

add(5,11)


def add_big(*num):
    print(num)
    sums = 0
    for i in num:
        sums += i
    return sums

print(add_big(1,2,3))
print(add_big(1, 2, 3, 4, 5, 6))



def print_info(**info):
    print(info)
    for i in info:
        print('%s : %s' % (i, info[i]))


print_info(name='alex',age=18,sex='female')


# 函数参数的位置
# 必须参数>默认参数>没有命名的不定长参数（*）>有命名的不定长参数（**）

def print_info_one(name, *args, **kwargs):   #def print_info_one(name, **kwargs, *args) 报错
    print("name : %s" % name)
    print("args : %s" % args)
    print("kwargs : %s" % kwargs)

print_info_one('alex',18,hobby='girl',nationality='Chinese',ability='Python')
# print_info_one(hobby='girl','alex',18,nationality='Chinese',ability='Python')   #报错
# print_info_one('alex',hobby='girl',18,nationality='Chinese',ability='Python')   #报错


# 函数不定长参数，传参另一种方式
# 可以传一个整体，一个元祖，一个列表，一个字典，整体传参

def print_info_two(*args):
    print(args)

print_info_two(*[1, 2, 'aa', 3, 'cc'])

def print_info_three(**kwargs):
    print(kwargs)

print_info_three(**{'name': 'alfa', 'age': '35', 'sex': 'male'})


# 高阶函数
# 1.接受一个或者多个函数作为参数输入
# 2.返回输入一个函数


def abc(a, b, f1):
    print(f1)  # 打印f1传入的是一个取绝对值的内置函数abs，<built-in function abs>
    return f1(a) + f1(b)

res1 = abc(10, -12 ,abs)
print(res1)


def ab_cd():
    x = 3
    def bar():
        return x
    return bar

print(ab_cd())  # 打印函数bar的内存地址 <function ab_cd.<locals>.bar at 0x000002AADEF09510>



# 函数的作用域
# L：local，局部作用域，即函数中定义的变量；
# E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的；
# G：global，全局变量，就是模块级别定义的变量；
# B：built-in，系统固定模块里面的变量，比如int, byte, array等。
# 搜索变量的优先级顺序依次是：作用域局部>外层作用域>当前模块中的全局>python内置作用域，也就是LEGB。



# （1）变量查找顺序：LEGB，作用域局部>外层作用域>当前模块中的全局>python内置作用域；
# （2）只有模块、类、及函数才能引入新作用域；
# （3）对于一个变量，内部作用域先声明就会覆盖外部变量，不声明直接使用，就会使用外部作用域的变量；
# （4）内部作用域要修改外部作用域变量的值时，全局变量要使用global关键字，
# 嵌套作用域变量要使用nonlocal关键字。nonlocal是python3新增的关键字，有了这个 关键字，就能完美的实现闭包了。



# 递归函数
# 定义：在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

# 普通阶乘函数实现
def factorial(n):
    a = n
    for i in range(1, n):
        print(i)
        a *= i
    return a

print(factorial(4))

# 递归函数阶乘实现

def factorial_new(n):

    if n == 1:
        return 1
    resl = n * factorial_new(n-1)
    return resl

print(factorial_new(4))



# 普通菲波那切数列
def fibo(n):
    one_num = 0
    two_num = 1
    three_num = 0
    for i in range(n):
        print(two_num, end=',')
        three_num = one_num + two_num
        one_num = two_num
        two_num = three_num
    return three_num

print(fibo(6))


# 递归斐波那契数列
def fibo_new(n):

    if n == 0 or n == 1:
        return 1
    else:
        return fibo_new(n-2) + fibo_new(n-1)

print(fibo_new(2))



