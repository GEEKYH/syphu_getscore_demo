from selenium import webdriver
import time
import getpass
#import pyfiglet
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
# coding=utf-8
import urllib
import urllib.request

import http.cookiejar
import random
from http import cookiejar
from bs4 import BeautifulSoup
import sys
import os
from PIL import Image, ImageFilter, ImageEnhance


def login2():
    ####################浏览器初始化####################
    print("Started")
    browser = webdriver.Chrome()
    #browser=webdriver.Chrome()
        #browser=webdriver.PhantomJS(executable_path='E:/Youxun/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    url="http://sso-syphu-edu-cn.vpn.syphu.edu.cn:8118/"
        
    browser.get(url)
    
    time.sleep(2)
    url1=browser.current_url
    url0=url1[0:-10]
    
    time.sleep(5)
    #模拟登陆
    browser.find_element_by_name("username").send_keys(1905020312)
    browser.find_element_by_name("username").send_keys(Keys.TAB)
    browser.find_element_by_name("password").send_keys(1380013800)
    #browser.find_element_by_id("txt_sdertfgsadscxcadsads").send_keys(code)
    browser.find_element_by_id("save").click()
    time.sleep(1)
    print("\n=========== 智慧校园登录成功 ===========\n")
    login(browser)
    
def login(b):
    ##############登录教务处###############
    url="http://192-168-7-3.vpn.syphu.edu.cn:8118/"
    browser.get(url)
    time.sleep(5)
    
    #拿到验证码
    print("\n[*]正在下载验证码...")
    element = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div[1]/div[3]/img')
    
    ###############验证码处理###############
    
    #print("success")
    browser.set_window_size(1200, 800)
    left = int(element.location['x'])
    top = int(element.location['y'])
    right = int(element.location['x'] + element.size['width'])
    bottom = int(element.location['y'] + element.size['height'])
    #print(left)                                        
    
    
    #通过Image处理图像
    browser.get_screenshot_as_file('E:/Youxun/screenshot.png')
    im = Image.open('E:/Youxun/screenshot.png')
    im = im.crop((left, top, right, bottom))
    im.save('E:\Youxun\code.png')

    code=input("\n[*]请输入验证码：")
    ##继续登录
    browser.find_element_by_id("WebUserNO").send_keys(1905020312)
    browser.find_element_by_id("WebUserNO").send_keys(Keys.TAB)
    browser.find_element_by_id("Password").send_keys(1905020312)
    browser.find_element_by_id("Agnomen").send_keys(code)
    browser.find_element_by_class_name("login-button").click()
    time.sleep(1)
    print("\n=========== 教务处登录成功 ===========\n")
    
    ###########获取分数#############
    url="http://192-168-7-3.vpn.syphu.edu.cn:8118/ACTIONQUERYGRADUATESCHOOLREPORTBYSELF.APPPROCESS"
        
    browser.get(url)
    time.sleep(1)
    ALLscore = BeautifulSoup(browser.page_source,'html.parser')
    scoreTRList = ALLscore.find_all('tr')
    data_list = []
    for trTag in scoreTRList:
        tds = trTag.find_all('td')
        a = len(tds)
        if a == 8:
                data_list.append({
                    '科目': tds[2].contents[0].string.replace('\xa0',''),
                    '成绩': tds[6].contents[0].string.replace('\xa0',''),
                    '时间': tds[0].contents[0].string.replace('\xa0',''),
                    '学分': tds[5].contents[0].string.replace('\xa0',''),
                    '绩点': tds[7].contents[0].string.replace('\xa0','')
                    })
        else:
                continue

    for item in data_list:
        d = item.get("时间")
        if d == '2020-2021学年上学期':
            for key,value in item.items():
                print(str(key)+": "+str(value),end='  ')
            print('||')
    pass
if __name__ == '__main__':
    login2()

    






