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

# TotalMoney = int(input("请输入您的购物预算金额:"))
# print('您的购物预算金额为%d元' % TotalMoney)
#
# GoodsList = ['1.iphone6s ￥5888', '2.MacBook ￥12000', '3.小米空气净化器 ￥799', '4.小米电视50寸 ￥2999', '5.小米手机 ￥1500', '6.pythonbook ￥85', '7.python ￥3500']
# print("为您展示我们的商品列表，请您选购！")
# for a in range(7):
#     print(GoodsList[a])
# GoodsPrice = [5888, 12000, 700, 2999, 1500, 80, 3500]
# ShoppingCat = []
# ShoppingCat_index = 0
# ChoiceGoods = []
# BalanceMoney = TotalMoney
# Quit = True
# while Quit:
#     Goodsindex = input("请输入选购的商品编号或输入Quit退出:")
#     if Goodsindex == 'Quit':
#         Quit = False
#         continue
#     BalanceMoney = BalanceMoney - GoodsPrice[int(Goodsindex)-1]
#     if BalanceMoney < 0:
#         print("余额不足，无法选购该商品！")
#     elif BalanceMoney == 0:
#         print("您的余额已经为0元，无法继续购买！")
#         Quit = False
#     else:
#         print("您选择的商品已经加入购物车，您的余额为:%d元" % BalanceMoney)
#         ShoppingCat.append(GoodsList[int(Goodsindex)-1])
#         ShoppingCat_index += 1
# print("您的购物车商品列表,欢迎下次再来！")
# for c in range(ShoppingCat_index):
#     print(ShoppingCat[c])


"""------------------------优化程序----------------------------"""
"""
1.使用列表嵌套，使商品数据可变
2.使用enumerate方法，可以在一个大的列表中显示序号，并且显示对应的小列表数据
3.所有代码避免HardCode形式
4.优化添加库存情况，每次选择购买后扣减库存
5.购物车中商品去重，并计算数量后，显示
"""

#创建商品列表
Goods_list = [
    ['Mac', 12000, 99],
    ['iphone6s', 5888, 99],
    ['Bike', 1500, 99],
    ['Kindle', 900, 99],
    ['Python', 350, 99],
    ['coffee', 50, 99]
]


#屏幕输入用户的预算总金额,并转换成int类型
while True:
    MoneyAll = input('请输入您的购买商品预算总金额:')
    #使用isdigit()方法判断输入的是纯数字内容，是数字就转int类型，不是就继续输入
    if MoneyAll.isdigit():
        MoneyAll = int(MoneyAll)
        break
    else:
        print('请输入正确的金额数字。')
        continue

shopping_car = []
Q = True
#choiceNo = 0
while Q:
    # 展示商品
    for i, v in enumerate(Goods_list, 1):
        print(i, v[0], '￥%d 库存%d' % (v[1], v[2]))

    choice_goodsNo = input('请输入您要购买的商品编号或者输入exit退出:')
    if choice_goodsNo.isdigit():
        choice_goodsNo = int(choice_goodsNo)
        if choice_goodsNo > 0 and choice_goodsNo <= len(Goods_list):
            if MoneyAll - Goods_list[choice_goodsNo-1][1] > 0:
                shopping_car.append(Goods_list[choice_goodsNo - 1])
                Goods_list[choice_goodsNo - 1][2] -= 1
                #shopping_car[choiceNo][2] = 1  使用append扩展的list修改一个会覆盖另一个，待解决
                MoneyAll = MoneyAll - Goods_list[choice_goodsNo - 1][1]
                print('您选购的商品%s，已经加入购物车，您的余额还剩%d元。' % (Goods_list[choice_goodsNo - 1][0], MoneyAll))
                #choiceNo += 1
            elif MoneyAll - Goods_list[choice_goodsNo-1][1] == 0:
                shopping_car.append(Goods_list[choice_goodsNo - 1])
                Goods_list[choice_goodsNo - 1][2] -= 1
                MoneyAll = MoneyAll - Goods_list[choice_goodsNo - 1][1]
                print('余额已经为%d元，无法继续购买' % MoneyAll)
                print('您的购物车已购商品列表如下:')
                for x, y, k in enumerate(shopping_car, 1):
                    print(x, y[0], '￥%d 件数%d' % (y[1], y[2]))
                Q = False
            else:
                print('余额不足，无法购买该商品')
        else:
            print('请输入正确的商品编号')
    elif choice_goodsNo == 'exit':
        print('----您的购物车已购商品列表如下:----')

        #------查找shopping_car中重复数据，并显示重复次数
        #------使用字典，后续还是无法正确打印，待解决
        #Todo
        # MyGoodsCar = {}
        # for i2 in shopping_car:
        #     i2 = str(i2)
        #     if i2 not in MyGoodsCar:
        #         MyGoodsCar[i2] = 1
        #     else:
        #         MyGoodsCar[i2] += 1
        #
        # print(MyGoodsCar)


        #------去掉shopping_car中重复的数据
        Mycar = []
        temp_car = shopping_car
        i1 = 0
        print(temp_car)
        while i1 < len(temp_car):
            if not temp_car[i1] in Mycar:
                Mycar.append(temp_car[i1])
            else:
                i1 += 1
        print(Mycar)
        '''---------------------------------'''
        # for x, y in MyGoodsCar:
        #     print(y[0], '￥%s 件数%s' %(y[1], MyGoodsCar[y]))
        for x, y in enumerate(Mycar, 1):
            print(x, y[0], '￥%d' % y[1])
        Q = False
    else:
        print('您输入的格式有误请重新输入。')
