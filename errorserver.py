import werobot
import re
import time
import _thread,threading
# coding=utf-8
robot = werobot.WeRoBot(token='tokenhere')


@robot.handler
def hello(message):
    #return "同学们，现在是选课的高峰期，查分系统暂时关闭。想查询期末成绩的同学，请明天再来访问，谢谢理解。"
    #return "现在是程序维护时间\n明早8点开放。\n感谢大家的支持\n大家晚安~"
    #return "断线重连中...请5分钟后再试"
    #return "邮局打烊啦，明早再来吧~"
    return "查成绩服务已于18号关闭\n下次开放时间待定\n一路相伴，感谢有你！"
# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
