#！/usr/bin/python
#!-*- coding:utf-8 -*-
"""
@Author : Alfa
@File : PythonTools_验证码识别.py
@Time : 2020/6/10 23:15
"""

from selenium import  webdriver
from PIL import Image
from aip import AipOcr

# 验证码的获取和处理
def get_captcha():
    brow = webdriver.Chrome()
    url = 'https://cloudmeeting.189.cn/landing.html'

    brow.get(url)
    png = brow.find_element_by_id('captureImg')
    png.screenshot('capt.png')  #将图片截屏并保存

    # 处理验证码
    img = Image.open('capt.png')
    img = img.convert('L') # P模式转换为L模式(灰度模式默认阈值127)
    count = 170  # 设定阈值
    table = []
    for i in range(256):
        if i < count:
            table.append(0)
        else:
            table.append(1)

    img = img.point(table, '1')
    img.save('captcha.png')  #保存处理后的验证码


# 验证码的识别
def discern_captcha():
    # 百度提供
    """ 你的 APPID AK SK """
    APP_ID = '20321881'
    API_KEY = 'kGf5zuzdy9FFxDSikzM9li0y'
    SECRET_KEY = 'HGaFLTY7e3Z1hxmmtOBlLTlMPNWQK7fK'
    # 初始化对象
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # 读取图片
    def get_file_content(file_path):
        with open(file_path, 'rb') as f:
            return f.read()

    image = get_file_content('captcha.png')
    # 定义参数变量
    options = {'language_type': 'ENG', }  # 识别语言类型，默认为'CHN_ENG'中英文混合
    #  调用通用文字识别
    result = client.basicAccurate(image, options)  # 高精度接口 basicAccurate
    for word in result['words_result']:
        captcha = (word['words'])

        print('识别结果：' + captcha)

        return captcha

if __name__ == '__main__':
    get_captcha()
    captcha = discern_captcha()