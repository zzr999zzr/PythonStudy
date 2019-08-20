#!/usr/bin/python3
# !-*- coding:utf-8 -*-
#Author = 'Alfa'
#Time = '2019/3/19 16:43'


"""
使用正则开发一个简单的python计算器
1.实现加减乘除和括号的优先级判断
2.用户输入：
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
类似的公式，可以正确运算出结果
"""

"""
1.首先去掉输入可能的空格
2.然后匹配输入可能的++\+-;**、//这些重复输入的符号
3.优先匹配出最里面的括号内容，循环找出最里面的括号内容，并按照加减乘除计算整理新的字符串
4.循环整理出所有括号内的计算内容，再按照最后的加减乘除顺序计算出总的结果
"""
import  re

def mult_divi(sr):  #传入类似字符串'(1+2*3+3/4)'

    strs = re.search('\d+[.]?\d*[*/]\d+[.]?\d*',sr).group() #获取类型'3*4' 这样的字符串
    x,y = re.split('[*/]',strs)
    x = float(x)
    y = float(y)
    if re.search('\*',strs):
        strs1 = str(x*y)  #'4'
    else:
        strs1 = str(x/y)
    stra = sr.replace(strs,strs1)  #替换成(1+6+3/4)
    return stra


def add_sub(sr):
    strs = re.search('\d+[.]?\d*[+-]\d+[.]?\d*', sr).group()  # 获取类型'3+4' 这样的字符串
    x, y = re.split('[+-]', strs)
    x = float(x)
    y = float(y)
    if re.search('\+', strs):
        strs1 = str(x+y)  # '4'

    else:
        strs1 = str(x-y)

    stra = sr.replace(strs, strs1)  # 替换成(1+6+8)
    return stra


s = input("请输入计算的内容:")
#print(s)

def format(s):
    #判断括号对称、输入符号格式
    while s.count('++') != 0 or s.count('+-') != 0 or s.count('+*') != 0 or s.count('+/') != 0 \
        or s.count('--') != 0 or s.count('-+') != 0 or s.count('-*') != 0 or s.count('-/') != 0 \
        or s.count('**') != 0 or s.count('*/') != 0 or s.count('*+') != 0 or s.count('*-') != 0\
        or s.count('//') != 0 or s.count('/*') != 0 or s.count('/+') != 0 or s.count('/-') != 0\
        or s.count('(') != s.count(')'):
        s = input("计算内容格式错误，请重新输入正确的计算内容:")
    s = s.replace(' ', '')  # 去掉输入的空格
    return s

#print(ret)

ret = format(s)
print(ret)


while re.search('\(',ret):
    ret1 = re.search('\([^()]+\)',ret).group()
    #print(ret1)
    while re.search('[*/]',ret1):
        ret1 = mult_divi(ret1)
    while re.search('[+-]',ret1):
        result = add_sub(ret1)


# '1+9+3-4+2-5'
else:
    while re.search('[*/]',ret):
        ret = mult_divi(ret)
    print(ret)
    while re.search('[+-]',ret):
        ret = add_sub(ret)

print(ret)













