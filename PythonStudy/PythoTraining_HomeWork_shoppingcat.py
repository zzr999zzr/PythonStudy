#!/usr/bin/python3
#!-*- coding:utf-8 -*-
#Author:Alfa
#Time   : 2018/4/3 14:32

"""
作业-购物车
1.用户开始输入购物总金额
2.展示商品列表，格式如下
    1.iphone6s 6000
    2.Macbook  12000
    3.小米空气净化器 799
    4.小米电视50寸 2999
    5.小米手机 1500
    6.pythonbook 85
    7.python 3500
3.用户可以选择编号，选购对应商品
4.用户选择后，判断商品价格是否小于等于总金额
    1.小于，提示用户选购的商品信息，并告知已加入用户的购物车，显示余额
    2.等于，提示用户选购的商品信息，并告知已加入用户的购物车，显示余额为0，
        提示用户无法再选购商品，显示用户购物车商品信息，提示结束信息
    3.大于，提示用户余额不足，无法添加该商品
5.用户可以一直选购商品添加购物车，直到输入Quit或者用户余额为0，给出提示用户的购物车商品信息列表，结束语句“欢迎下次光临”

"""

TotalMoney = int(input("请输入您的购物预算金额:"))
print('您的购物预算金额为%d元' % TotalMoney)

GoodsList = ['1.iphone6s ￥5888', '2.MacBook ￥12000', '3.小米空气净化器 ￥799', '4.小米电视50寸 ￥2999', '5.小米手机 ￥1500', '6.pythonbook ￥85', '7.python ￥3500']
print("为您展示我们的商品列表，请您选购！")
for a in range(7):
    print(GoodsList[a])
GoodsPrice = [5888, 12000, 700, 2999, 1500, 80, 3500]
ShoppingCat = []
ShoppingCat_index = 0
ChoiceGoods = []
BalanceMoney = TotalMoney
Quit = True
while Quit:
    Goodsindex = input("请输入选购的商品编号或输入Quit退出:")
    if Goodsindex == 'Quit':
        Quit = False
        continue
    BalanceMoney = BalanceMoney - GoodsPrice[int(Goodsindex)-1]
    if BalanceMoney < 0:
        print("余额不足，无法选购该商品！")
    elif BalanceMoney == 0:
        print("您的余额已经为0元，无法继续购买！")
        Quit = False
    else:
        print("您选择的商品已经加入购物车，您的余额为:%d元" % BalanceMoney)
        ShoppingCat.append(GoodsList[int(Goodsindex)-1])
        ShoppingCat_index += 1
print("您的购物车商品列表,欢迎下次再来！")
for c in range(ShoppingCat_index):
    print(ShoppingCat[c])

















