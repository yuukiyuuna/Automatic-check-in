# -*- coding=utf-8 -*-

import requests

def getNews():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    #获取英文文本
    # content = r.json()['content']
    #获取中文文本
    note = r.json()['note']

    #判断长度（过长会导致签到失败）
    changdu = len(note)
    if changdu > 50:
        note = note[:50]
    return note

#得到网站的具体内容
def get_content(label, list):
    content_list = list.split('\n')

    users = []
    for a in content_list:
        if a == '' or a == label:
            continue
        elif a.startswith('#'):
            continue
        elif a == 'status=1':
            status = 1
        elif a == 'status=0':
            status = 0
        else:
            users.append(a)

    user = {}
    try:
        for a in users:
            b = a.split('|')
            user[b[0]] = b[1]
    except EnvironmentError:
        print('init文件中' + label + '格式有误，请检查文件格式后再次运行此程序')

    return status, user

#定义签到网站
def get_init():
    #从init文件中获取内容，后面对其过滤
    rules = open('init', 'r', encoding='UTF-8').read()
    rule = rules.split('----------------------------------')

    #定义labels中存放所有需要签到的网站名称
    labels=['[iyunv]', '[cdtkdw]', '[mmy]']
    for a in labels:
        if a == '[iyunv]':
            list = rule[1]
            iyunv_content = get_content(a, list)
        elif a == '[cdtkdw]':
            list = rule[2]
            cdtkdw_content = get_content(a, list)
        elif a == '[mmy]':
            list = rule[3]
            mmy_content = get_content(a, list)

    #return返回格式为((签到状态, 字典型的用户名密码表))
    #举例：((0, {'admin': '123456'}), (1, {'admin': '123456'}), (1, {'admin': '123456'}))
    return iyunv_content, cdtkdw_content, mmy_content

