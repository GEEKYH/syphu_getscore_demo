import werobot
import re
import time
import _thread,threading
# coding=utf-8
import driverweb
robot = werobot.WeRoBot(token='tokenhere')
#browser = driverweb.login2()
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
@robot.subscribe
def subscribe(message):
    return "欢迎关注四季邮局沈药分局。\n四季邮局沈药分局一家四季常开的邮局，一个有趣青年的聚集地。\n查询个人期末成绩请回复”查成绩“。\n注：系统由沈药分局工作人员研发\n有问题请联系工作人员微信号：yangmhong964"
#@robot.UnSubscribe
#def unsubscribe():
    #return ""
@robot.filter(re.compile("^[0-9]\w{7,10}\s[0-9A-Za-z]\w{1,20}.*?$"))
def username(message):
    content = str(message.content)
    try:
        userpass = content.split(' ')
        username = userpass[0]
        password = userpass[1]
    except:
        return("查询格式错了，学号加空格加密码，不要换行")
    #time.sleep(0.1)
    xuhao = driverweb.get_xuhao()
    mutex = threading.Lock()
    #_thread.start_new_thread(driverweb.login,(username,password,browser,xuhao))
    #thread1 = threading.Thread(target=driverweb.login,name='thread1',args=(username,password,browser,xuhao,))
    thread1 = threading.Thread(target=driverweb.login,name='thread1',args=(username,password,xuhao,))
    thread1.start()
    #urn "加入查询队列成功，您的排队码为"'请等待5秒后回复排队码获取成绩'
    return driverweb.lenlist()
    #return driverweb.login(username,password,browser)
    

@robot.filter(re.compile("[\u4e00-\u9fa5]\w{1,10}.*?"))
def chinese(message):
    content = str(message.content)
    if content == '排队码':
        return "排队码是那串数字朋友"
    elif content == '查成绩':
        return "请回复“学号+空格+密码”\n（例如：xxxxx xxxxx）\n中间不用换行,密码是登陆教务处的密码\n输入排队码没有回复说明系统正在查询，请稍作等待后再发一次排队码\n为保障服务质量，请不要频繁查询"
    else:
        return "没理解您的意思，查成绩请回复“查成绩”"
    
@robot.handler
def hello(message):
    
    chang = len(str(message.content))
    content = str(message.content)
    

    if is_number(content) and chang <= 6 :
        #reply = ImageReply(message=message,media_id=message.MediaId)
        #return reply
        a = driverweb.qscore(int(content))
        a = a.replace('时间:2020-2021学年上学期 ','')
        a = a.replace(" 成绩","\n成绩")
        return a
    #elif content == '1'  :
        #content = '2'
        #score = driverweb.login2()
        #return score
    else:
        return "没理解您的意思，查成绩请回复“查成绩”"
    
    

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
