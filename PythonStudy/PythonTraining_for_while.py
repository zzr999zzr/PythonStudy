#!/usr/bin/python3
#!-*- coding:utf-8 -*-
#Author:Alfa
#Time   : 2018/3/30 15:43

"""
练习for循环
"""



for i in range(3):
    print(i)



for i in range(1,30,2):
    print(i, end=" ")
print()


uname = 'alfa'
upassword = 'abc123'

for i in  range(1,4):
    name = input("输入姓名:")
    password = input("输入密码:")

    if name == uname and password == upassword:
        print("输入姓名密码正确！")
        break
    elif name != uname or password != upassword:
        if 3-i == 0:
            print("输入的姓名或密码错误，请重新输入！所有机会使用完账户冻结！")
        else:
            print("输入的姓名或密码错误，请重新输入！还有%d次机会" %(3-i))



'''
练习打印99乘法表
'''
a = 1
while a <= 9 :
    # c = 9
    # while c > a:
    #
    #     print(end=' ')
    #     c -= 1
    b = 1
    while b <= a :
        print("%d*%d=%d" %(a,b,a*b) ,end=" ")
        b += 1
    print("")
    a += 1

'''
练习打印左对齐、中对齐、右对齐三角形
'''

num = 1
while num <= 9:
    num1 = 1
    while num1 <= num :
        print("*", end="")
        num1 += 1
    print("")
    num += 1



rows = int(input('输入列数： '))
i = j = k = 1  # 声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
# 等腰直角三角形1
print("等腰直角三角形1")
for i in range(0, rows):
    for k in range(0, rows - i):
        print(" * ", end="")  # 注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print("\n")

# 打印实心等边三角形
print("打印空心等边三角形，这里去掉if-else条件判断就是实心的")
for i in range(0, rows + 1):  # 变量i控制行数
    for j in range(0, rows - i):  # (1,rows-i)
        print(" ", end="")
        j += 1
    for k in range(0, 2 * i - 1):  # (1,2*i)
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
                if k % 2 == 0:  # 因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                    print("*", end="")
                else:
                    print(" ", end="")  # 注意这里的","，一定不能省略，可以起到不换行的作用
            else:
                print("*", end="")
        else:
            print(" ", end="")
        k += 1
    print("\n")
    i += 1

# 打印菱形
print("打印空心等菱形，这里去掉if-else条件判断就是实心的")
for i in range(rows):  # 变量i控制行数
    for j in range(rows - i):  # (1,rows-i)
        print(" ", end="")
        j += 1
    for k in range(2 * i - 1):  # (1,2*i)
        if k == 0 or k == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
        k += 1
    print("\n")

    i += 1
    # 菱形的下半部分
for i in range(rows):
    for j in range(i):  # (1,rows-i)
        print(" ",end="")
        j += 1
    for k in range(2 * (rows - i) - 1):  # (1,2*i)
        if k == 0 or k == 2 * (rows - i) - 2:
            print("*", end="")

        else:
            print(" ", end="")
        k += 1
    print("\n")
    i += 1
# 实心正方形
print("实心正方形")
for i in range(0, rows):
    for k in range(0, rows):
        print(" * ", end="")  # 注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print("\n")

# 空心正方形
print("空心正方形")
for i in range(0, rows):
    for k in range(0, rows):
        if i != 0 and i != rows - 1:
            if k == 0 or k == rows - 1:
                # 由于视觉效果看起来更像正方形，所以这里*两侧加了空格，增大距离
                print(" * ", end="")  # 注意这里的","，一定不能省略，可以起到不换行的作用
            else:
                print("   ", end="")  # 该处有三个空格
        else:
            print(" * ", end="")  # 这里*两侧加了空格
        k += 1
    i += 1
    print("\n")