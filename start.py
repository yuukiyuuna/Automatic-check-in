# -*- coding:utf-8 -*-
from auto_login import *
from maindef import *
import datetime

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '程序开始执行')
#初始化脚本运行状态参数（默认为0，不执行该子脚本）
iyunv_status = 0
cdtkdw_status = 0
mmy_status = 0

#获取是否签到状态与用户名密码表
users = get_init()

#获取每日一句
try:
    say_something = getNews()
except EnvironmentError:
    print('获取每日一句失败，想说的话设置成为默认值')
    print('获取每日一句失败的错误详情：' + EnvironmentError)
    say_something = "隔壁超市薯片半价啊！快去买啊！"

#======================================================================================================================================
'''
备注：为了防止以后忘记规则
网站的顺序是固定的，不可以随意更改网站的顺序
if后面的users[0][0]是返回状态码（也就是maindef.py中的get_init()函数中每一项的第一个值）的签到状态。             #是否签到，值为0/1
这一行从规则上讲，有多个网站变动的只有第一个方括号里面的值，详情请看下面代码

for后面的users[0][1]是返回用户名和密码列表（也就是maindef.py中的get_init()函数中每一项的第二个值）。
这一行从规则上讲，有多个网站变动的只有第一个方括号里面的值，详情请看下面代码

函数里面的users[0][1][a]是返回对应用户名的密码（也就是每一个网站中所有账户名对应的该密码）
这一行从规则上讲，有多个网站变动的只有第一个方括号里面的值，详情请看下面代码
'''
#执行爱运维签到程序
if users[0][0]:
    for a in users[0][1]:
        try:
            iyunv(a, users[0][1][a])
        except EnvironmentError:
            print('爱运维网站签到错误，用户 ' + a + ' 签到未成功')
            print('爱运维网站签到的错误详请：' + EnvironmentError)
            continue
else:
    print('爱运维网站，用户跳过签到该网站')

#执行电玩网签到程序
if users[1][0]:
    for a in users[1][1]:
        try:
            cdtkdw(a, users[1][1][a], say_something)
        except EnvironmentError:
            print('成都电玩网网站签到错误，用户 ' + a + ' 签到未成功')
            print('成都电玩网网站签到的错误详请：' + EnvironmentError)
            continue
else:
    print('电玩网网站，用户跳过签到该网站')

if users[2][0]:
    for a in users[2][1]:
        try:
            mmy(a, users[2][1][a], say_something)
        except EnvironmentError:
            print('慢慢游网站签到错误，用户 ' + a + ' 签到未成功')
            print('慢慢游网站签到的错误详请：' + EnvironmentError)
            continue
else:
    print('慢慢游网站，用户跳过签到该网站')

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '程序运行结束')
