# !/usr/bin/python3
# !-*- coding:utf-8 -*-
# Author : Alfa
# Time : 2018/6/24 22:11

"""
装饰器函数练习
"""

"""装饰器函数，三大条件"""
"""
1.作用域
2.函数即对象
3.函数的嵌套、闭包函数
"""


# 函数对象，1.可以赋值给其他变量
def foo():
    print("foo")
bar = foo
bar()  #foo
foo()  #foo
print(id(bar), id(foo))  #2214895921488 2214895921488

#2.可以被定义在另一个函数内，做为参数或者做为返回值
def foo1(func):
    print("hahaha")
    func()
def bar1():
    print("hehehe")

foo1(bar1)  # hahaha   hehehe

#做为返回值
def foo2():
    print("aaaaa")
    return bar2

def bar2():
    print("bbbbb")

a = foo2()  # aaaaa  a = bar2
a()  # bbbbb  a() 等于  bar2()



# 函数的嵌套 , 闭包

def out():
    a = 10
    def inner():
        print(a)

    return inner
#inner()  报错,找不到inner引用
inner_new = out()  #这里就是变量赋值,把out()返回的inner的引用,赋值给 inner_new变量
                   #这里无法直接inner_new = inner,inner还没有被引用,无法找到
inner_new()  # 打印 10 就是执行了inner()

# 这里inner() 就是闭包函数
# 如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure).
# 如上实例,inner就是内部函数,inner中引用了外部作用域的变量x,
# X是在out函数中,对于inner来说是外部作用域,不是全局作用域,所以inner就是一个闭包
# 如果X是在out中的参数比如(def out(X)),inner也是引用了,也算外部作用域,inner也算一个闭包

# 装饰器,装饰器本身就是一个函数,该函数用来处理其他函数,可以在不修改其他函数代码的前提下,增加额外的功能.
# 装饰器的返回值也是一个函数对象,总的来说,装饰器的作用就是为已存在的对象函数添加额外的功能.
""""
def old_func():
    print("hello")
"""
# 新需求,old_func需要知道执行函数的时间
import time
""""
def old_func():
    start_time = time.time()
    print("hello")
    end_time = time.time()
    print("执行了%s秒" % (end_time-start_time))
"""

#需求是实现了,但是如果多个函数都需要添加执行时间,这个时候会想到,定义一个计算执行时间的函数
"""""
def run_time(fu):
    start_time = time.time()
    fu()
    end_time = time.time()
    print("执行了%s秒" % (end_time-start_time))

def old_func():
    print("hello")
    time.sleep(3)

run_time(old_func)
"""

# 业务逻辑上实现了,但是如果old_func函数已经被多个业务线调用,这样其他业务线都需要修改调用方法,如果需要不改变执行调用的方法
# 还是执行old_func() 这样来调用,这时我们就可以使用装饰器
# 当 old_func()== run_time(fu) 这样就可以解决上面的问题
"""
def run_time(fu):
    def inn():
        start_time = time.time()
        fu()
        end_time = time.time()
        print("执行了%s" % (end_time-start_time))
    return inn

def old_func():
    print("hello")
    time.sleep(2)

old_func = run_time(old_func)
old_func()
"""


# 上面就实现了装饰器 run_time(fu) 就是一个装饰器函数了
# 装饰器函数的语法,使用@符号,定义函数的时候使用,避免赋值的操作.
"""
def run_time(fu):
    def inn():
        start_time = time.time()
        fu()
        end_time = time.time()
        print("执行了%s" % (end_time-start_time))
    return inn

@run_time
def old_func():
    print("hello")
    time.sleep(2)

old_func()
"""

# 装饰器也可以添加参数,来更好的控制功能的实现
# 需求在已知函数中,添加日志内容,并且根据传入的值来控制是否添加日志.

def logger_record(flag=0):
    def run_time(fu):
        def inn(*args, **kwargs):
            start_time = time.time()
            fu(*args, **kwargs)
            end_time = time.time()
            print("执行了%s" %(end_time-start_time))
            if flag == 0:
                print("日志已经被记录.")
        return inn
    return run_time

@logger_record(0)
def add(*args, **kwargs):
    sums = 0
    for i in args:
        sums += i
    print(sums)
    time.sleep(1.5)

add(1, 2, 3, 4, 5)

@logger_record(1)
def aoo(*args, **kwargs):
    aee = 0
    for i in args:
        aee -= i
    print(aee)
    time.sleep(0.5)

aoo(6, 7, 8, 9, 10)


@logger_record(0)
def factor(*args, **kwargs):
    num = args[0]
    for i in range(1, num):
        print(i)
        num *= i
    print(num)
    time.sleep(3)

factor(6)



# def show_time(func):
#
#     def wrapper(n):
#         ret=func(n)
#         print("hello,world")
#         return ret
#     return wrapper
#
# @show_time# foo=show_time(foo)
# def foo(n):
#     if n==1:
#         return 1
#     return n*foo(n-1)
# print(foo(6))
# def show_time(func):
#
#     def wrapper(n):
#         ret=func(n)
#         print("hello,world")
#         return ret
#     return wrapper
#
# @show_time# foo=show_time(foo)
# def foo(n):
#     def _foo(n):
#         if n==1:
#             return 1
#         return n*_foo(n-1)
#     return _foo(n)
# print(foo(6))


































































