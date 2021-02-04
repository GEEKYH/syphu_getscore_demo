from selenium import webdriver
import time
import getpass
import _thread,threading
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
import os,chaojiying,re
num = 0
list=[]
list2=[]
a = 0
xuhao = 0
waitlist = 0
qing = True
mutex = threading.Lock()
def captcha_discern(chaojicode):
    client = chaojiying.Chaojiying_Client('geekyh','1380013800','911387')     #依次输入超级鹰平台的 用户名，密码，软件ID
    with open(chaojicode, 'rb') as f:
        image = f.read()
        #print(chaojicode)
        captcha = client.PostPic(image,1902)['pic_str']
    print('captcha discerned: '+captcha)
    return captcha



def login2():
    try:
        ####################浏览器初始化####################
        
        # 创建chrome参数对象
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
        options.add_argument('window-size=1600x900') # 指定浏览器分辨率
        options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
        options.add_argument('--hide-scrollbars') # 隐藏滚动条, 应对一些特殊页面
        options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片, 提升速度
        options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    except:
       return "初始化异常"
    else:
        pass
    browser = webdriver.Chrome(options=options)
    #browser=webdriver.Chrome()
        #browser=webdriver.PhantomJS(executable_path='E:/Youxun/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    url="http://sso-syphu-edu-cn.vpn.syphu.edu.cn:8118/"
    print("开始登陆")    
    browser.get(url)
    
    
    
    url1=browser.current_url
    url0=url1[0:-10]
    print("服务正常")
    #time.sleep(5)
    #time.sleep(5)
    try:
        #模拟登陆
        browser.find_element_by_name("username").send_keys(1905020312)
        browser.find_element_by_name("username").send_keys(Keys.TAB)
        browser.find_element_by_name("password").send_keys(1380013800)
        #browser.find_element_by_id("txt_sdertfgsadscxcadsads").send_keys(code)
        browser.find_element_by_id("save").click()
        time.sleep(1)
        print("\n=========== 智慧校园登录成功 ===========\n")
    except:
        return "智慧校园登录异常"

    else:
        pass
    return browser
def login(username,password,num):
    browser = login2()
    mutex.acquire()
    #print(num)
    global qing
    global waitlist
    qingnum = 0
    anqiu = 0
    tupian = 0
    tup = 0
    waitlist = num 
    #while 1:
        #if qing:
            #qing = False
            #break
        #else:
            #qing = True
            #time.sleep(5)
            #_thread.start_new_thread(driverweb.login,(username,password,browser,xuhao))
            #qingnum = qingnum + 1
            #time.sleep(1)
            #if qingnum > 20:
                #setscore("查询失败，请联系管理员",num)
                #qing = True
                #return
        
    ##############登录教务处###############
    url="http://192-168-7-3.vpn.syphu.edu.cn:8118/"
    browser.get(url)
    time.sleep(1)
    
    #拿到验证码
    print("\n[*]正在下载验证码...")
    while 1:
        #start = time.clock()
        try:
            time.sleep(2)
            element = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div[1]/div[3]/img')
            print('已定位到元素')
            #end=time.clock()
            break
        except:
            print("还未定位到元素!")
            #time.sleep(1)
            #tup = tup + 1
            #time.sleep(0.5)
            #if tup > 3:
            setscore("网络拥挤，请重试或联系管理员微信geekyh_syphu",num)
            mutex.release()
            return
            
            

    
    ###############验证码处理###############
    while 1:
    #start = time.clock()
        try:
            #time.sleep(0.5)
            browser.set_window_size(1200, 800)
            #time.sleep(5)
            left = int(element.location['x'])
            top = int(element.location['y'])
            right = int(element.location['x'] + element.size['width'])
            bottom = int(element.location['y'] + element.size['height'])
            print("已获取到图片!")
            break
        except:
            print("还未获取到图片!")
            #time.sleep(1)
            #tupian = tupian + 1
            #time.sleep(0.5)
            #if tupian > 3:
            setscore("网络拥挤，请重试或联系管理员微信geekyh_syphu",num)
            mutex.release()
            return
            
    #print("success")

    #print(left)                                        
    
    

    
    #通过Image处理图像
    ranum = random.randint(1,100)
    
    filename = './screenshot' + str(ranum) + '.png'
    codename = './code' + str(ranum) + '.png'
    browser.get_screenshot_as_file(filename)
    im = Image.open(filename)
    im = im.crop((left, top, right, bottom))
    im.save(codename)
    #print(codename)
    chaojicode = 'code' + str(ranum) + '.png'

    code=captcha_discern(chaojicode)
    #print(code)
    os.remove(filename)
    os.remove(codename)
    ##继续登录
    #time.sleep(0.5)
    while 1:
        #start = time.clock()
        try:
            browser.find_element_by_id("WebUserNO").send_keys(username)
            browser.find_element_by_id("WebUserNO").send_keys(Keys.TAB)
            browser.find_element_by_id("Password").send_keys(password)
            browser.find_element_by_id("Agnomen").send_keys(code)
            browser.find_element_by_class_name("login-button").click()
            #print(username,password)
            #end=time.clock()
            break
        except:
            print("还未定位到按钮!")
            #time.sleep(1)
            #anqiu = anqiu + 1
            #time.sleep(0.5)
            #if anqiu > 3:
            setscore("网络拥挤，请重试或联系管理员微信geekyh_syphu",num)
            mutex.release()
            return
                

    
    
    

    #time.sleep(7)
    ###########获取分数#############
    url="http://192-168-7-3.vpn.syphu.edu.cn:8118/ACTIONQUERYGRADUATESCHOOLREPORTBYSELF.APPPROCESS"    
    browser.get(url)
    time.sleep(1)
    ALLscore = BeautifulSoup(browser.page_source,'html.parser')
    #print(ALLscore.title.string)
    #print(ALLscore)
    strscore = str(ALLscore)
    try:
        if strscore == '<html><head></head><body></body></html>':
            setscore('登录成功，但是毕业成绩单一片空白，老师还没有录入成绩',num)
            mutex.release()
            return
            
        elif ALLscore.title.string == u'毕业成绩表查询':
            print("\n=========== 教务处登录成功 ===========\n")

        else:
            #print(ALLscore)
            setscore('教务处登录失败，请检查账号密码',num)
            mutex.release()
            return
    except:
        #print(ALLscore)
        setscore('教务处登录失败，请检查账号密码',num)
        mutex.release()
        return
    scoreTRList = ALLscore.find_all('tr')
    #print(scoreTRList)
    try:
        reg = re.compile('.*?名：.*?')
        tag = ALLscore.find(text=reg)
        #print("tag")
        #print(tag)
        name = tag.split("：")
        named = name[1] + '同学，你的成绩如下：'
    except:
        name = ""
        
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
    ################输出成绩单####################
    ALLscore = ''
    ALLscore2 = ''
    datalen = 0
    for item in data_list:
        d = item.get("时间")
        if d == '2020-2021学年上学期':
            if datalen < 17:
                for key,value in item.items():
                    score2 =  str(key) + ":" + str(value) + ' '
                    ALLscore = ALLscore + score2
                ALLscore = ALLscore + "\n——————————\n"
                datalen = datalen + 1
            else:
                for key,value in item.items():
                    score2 =  str(key) + ":" + str(value) + ' '
                    ALLscore2 = ALLscore2 + score2
                ALLscore2 = ALLscore2 + "\n——————————\n"
                datalen = datalen + 1
    if datalen > 17:
        ALLscore = ALLscore + "已达到微信回复字数限制，剩余成绩请回复数字 " + str((num * 59) + 1) + " 获取。"
    #print(ALLscore)
    if ALLscore == '':
        ALLscore = '您的成绩还没出，请耐心等待'
    ALLscore = named + "\n——————————\n" + ALLscore
    
    setscore(ALLscore,num)
    setscore2(ALLscore2,num)
    mutex.release()
    
def setscore(ALLscore,num):
    
    #if num != 0 and ALLscore == list[num - 1]:
        
        #list[num] = "教务处登录失败，请检查账号密码。\n相同账号请不要频繁查询"
    #else:
    list[num] = ALLscore
    
    #qing = True
def setscore2(ALLscore2,num):
    list2[num] = ALLscore2


def qscore(num):
    try:
        
        #print(qfour)
        
        if int(num) % 59 == 0:
            qfour = int(num) // 59
            a = list[qfour]
            #print(a)
            if qfour != 0 and a[0:3] == str(list[qfour - 1])[0:3]:
                return "密码错误。"
            else:
                return a
        elif (int(num) - 1) % 59 == 0:
            qfour = (int(num) - 1) // 59
            b = list2[qfour]
            
            return b
        else:
            return "请输入正确的排队码"
    except:
        return '出错了，再试一次或者联系管理员'
    else:
        return "恭喜，出Bug了"
def lenlist():
    global num
    global waitlist
    global xuhao
    #num = len(list)
    four = num * 59
    wait = (num - waitlist + 1) * 10
    b = "加入查询队列成功，您的排队码为 " + str(four) + " ,请等待" + str(wait) + "秒后回复排队码（数字）获取成绩\n"
    num = num + 1
    xuhao = num
    list.append("")
    list2.append("")
    return b
    

def get_xuhao():
    global xuhao
    a = xuhao
    #print(xuhao)
    return xuhao




