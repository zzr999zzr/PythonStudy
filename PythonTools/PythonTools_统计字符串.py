#!/usr/bin/python3
#!-*- coding:utf-8 -*-
#Author:Alfa
#Time   : 2018/4/13 16:15

# -*- coding:utf8 -*-
# -*- coding:utf8 -*-
import string
from collections import namedtuple

def str_count(s):
    '''找出字符串中的中英文、空格、数字、标点符号个数'''
    count_en = count_dg = count_sp = count_zh = count_pu = 0

    s_len = len(s)
    for c in s:
        # 英文
        if c in string.ascii_letters:
            count_en += 1
        # 数字
        elif c.isdigit():
            count_dg += 1
        # 空格
        elif c.isspace():
            count_sp += 1
        # 中文
        elif c.isalpha():
            count_zh += 1
        # 特殊字符
        else:
            count_pu += 1

    total_chars = count_zh + count_en + count_sp + count_dg + count_pu
    if total_chars == s_len:
        return namedtuple('Count', ['total', 'zh', 'en', 'space', 'digit', 'punc'])(s_len, count_zh, count_en,count_sp, count_dg, count_pu)
    else:
        print('Something is wrong!')
        return None

if __name__ == '__main__':
    str_l = "这是一个test字符串"
    count = str_count(str_l)
    print(str_l, end='\n\n')
    print('该字符串共有 {} 个字符，其中有 {} 个汉字，{} 个英文，{} 个空格，{} 个数字，{} 个标点符号。'.format(count.total, count.zh, count.en, count.space,
                                                                           count.digit, count.punc))




