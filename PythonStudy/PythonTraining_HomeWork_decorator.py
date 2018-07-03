#!/usr/bin/python3
#!-*- coding:utf-8 -*-
#Author:Alfa
#Time   : 2018/7/2 15:12

"""
装饰器练习
1.程序启动显示3个页面，1.home首页页面、2.finance金融页面、3.book图书页面
2.用户选择可以进入任意一个页面
3.用户选择后，进行页面登录验证，选择1、3时，进行京东账户验证，账户保存在京东文件中；
    选2时，进行weixin账户验证，账户保存在weixin文件中
4.登录验证成功，进入该页面，并且可以再次选择页面进入
5.如果已经登录了，再选择页面进入时，不需要再登录验证，直接进入页面

"""



isLogin = False
def login_type(type='jd'):
    def login_check(func):
        def login():
            global isLogin
            if isLogin == False:

                username = input("input username:")
                password = input("input password:")
                if type == 'wx':
                    true_username = 'shine'
                    true_password = '111111'
                    while username != true_username and password != true_password:
                        print("username or password input error")
                        username = input("username input again:")
                        password = input("password input again:")
                    isLogin = True
                else:
                    true_username = 'alfa'
                    true_password = '123456'
                    while username != true_username and password != true_password:
                        print("username or password input error")
                        username = input("username input again:")
                        password = input("password input again:")
                    isLogin = True
            else:
                pass
            func()
        return login
    return login_check

@login_type('jd')
def home_page():
    print("welcome to HomePage!")


@login_type('wx')
def finance_page():
    print("welcome to FinancePage!")

@login_type('jd')
def book_page():
    print("welcome to BookPage!")


finance_page()
home_page()
book_page()


































