# !usr/bin/env python3  
# -*- coding:utf-8 _*-  
# author: Alfa
# file: PythonTraining_HomeWork_threemeun.py 
# time: 2018/04/14 0:16

"""
三级菜单作业
1.主菜单，显示北京，上海，广州
2.用户输入北京，上海，广州，对应显示下级内容，对应城市的区县
3.用户输入对应的区县，显示对应的下级乡镇
4.2级 3级子菜单，可以返回上一级
5.用户可以任意退出，返回主菜单页面
"""

Meun_dict = {
    '北京': {'A区': {'a镇': '小a街道'}, 'B区': {'b镇': '小b街道'}, 'C区': {'c镇': '小c街道'}},
    '上海': {'D区': {'d镇': '小d街道'}, 'E区': {'e镇': '小e街道'}, 'F区': {'f镇': '小f街道'}},
    '广州': {'G区': {'g镇': '小g街道'}, 'H区': {'h镇': '小h街道'}, 'I区': {'i镇': '小i街道'}}
}

startKey = True
while startKey:
# print(Meun_dict)
    print('主菜单'.center(16, ' '))
    for i in Meun_dict:
        print(i ,'>')

    print()
    oneMeunNo = input('请输入您选择的主菜单名称:')
# oneMeunNo = '北京'

    for i in Meun_dict[oneMeunNo]:
        print(i,'>')

    twoMeunNo = input('请输入您选择的二级菜单名称:')
# twoMeunNo = 'B区'

    for i in Meun_dict[oneMeunNo][twoMeunNo]:
        print(i,'>')
    threeMeunNO = input('请输入您选择的三级菜单名称:')
# threeMeunNO = 'b镇'

    print(Meun_dict[oneMeunNo][twoMeunNo][threeMeunNO])













