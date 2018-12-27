#-*- coding: UTF-8 -*-
from selenium import webdriver
import time

'''
前提：用户名和密码必须正确！！！！！！
不用选择心情和输入想说的话，直接签到的网站判断思路：
如果能够点击签到按键，则说明未签到；若不能点击签到按键，则说明已经签到
'''
def iyunv(username, password):
    url = 'https://www.iyunv.com/member.php?mod=logging&action=login'

    # 设定无界面chromedriver
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_option.add_argument('window-size=800x600')  # 指定浏览器分辨率
    chrome_option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_option.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    chrome_option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    chrome_option.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    '''
    警告信息：
    #DeprecationWarning: use options instead of chrome_options warnings.warn('use options instead of chrome_options', DeprecationWarning
    根据源码的提示发现使用chrome_options 时会将chrome_options 值传给options,然后在给一个警告信息，
    根据错误信息已经源码的注解了解到未来options会取代chrome_options，所以我们只需要chrome_options改成options即可，
    该问题应该在最近的版本更改的目前我这边使用的是selenium==3.9.0，有兴趣的可以去看下官方文档，那个版本开始做的此项的修改。
    '''
    # 调用chromedriver
    browser = webdriver.Chrome(options=chrome_option)
    try:
        browser.get(url)
    except EnvironmentError:
        print('运维网网站已失效或网络连接超时，请检查网站或网络')
    time.sleep(1)

    # 输入用户名
    browser.find_element_by_name("username").send_keys(username)
    time.sleep(1)

    # 输入密码
    browser.find_element_by_name("password").send_keys(password)
    time.sleep(1)

    # 点击登入
    browser.find_element_by_name("loginsubmit").click()
    time.sleep(1)

    # 点击金币
    browser.get('https://www.iyunv.com/k_misign-sign.html')
    time.sleep(1)

    # 判断是已经签到
    try:
        browser.find_element_by_id("JD_sign").click()
        print('成功签到运维网，用户ID：' + username)
    except:
        print('运维网网站已经签到过，用户ID：' + username)

    time.sleep(2)
    browser.quit()

def cdtkdw(username, password, say):
    url = 'http://www.cdtkdw.com/member.php?mod=logging&action=login'

    # 设定无界面chromedriver
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_option.add_argument('window-size=800x600')  # 指定浏览器分辨率
    chrome_option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_option.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    chrome_option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    chrome_option.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    '''
    警告信息：
    #DeprecationWarning: use options instead of chrome_options warnings.warn('use options instead of chrome_options', DeprecationWarning
    根据源码的提示发现使用chrome_options 时会将chrome_options 值传给options,然后在给一个警告信息，
    根据错误信息已经源码的注解了解到未来options会取代chrome_options，所以我们只需要chrome_options改成options即可，
    该问题应该在最近的版本更改的目前我这边使用的是selenium==3.9.0，有兴趣的可以去看下官方文档，那个版本开始做的此项的修改。
    '''
    # 调用chromedriver
    browser = webdriver.Chrome(options=chrome_option)
    try:
        browser.get(url)
    except EnvironmentError:
        print('成都电玩网网站已失效或网络连接超时，请检查网站或网络')
    time.sleep(1)

    # 填写用户名
    browser.find_element_by_name("username").send_keys(username)
    time.sleep(1)

    # 填写密码
    browser.find_element_by_name("password").send_keys(password)
    time.sleep(1)

    # 点击登入
    browser.find_element_by_name("loginsubmit").click()
    time.sleep(1)

    # 跳转签到界面
    browser.get("http://www.cdtkdw.com/plugin.php?id=dsu_paulsign:sign")
    time.sleep(1)

    try:
        # 选择心情
        browser.find_element_by_css_selector("img[src='source/plugin/dsu_paulsign/img/emot/ng.gif']").click()
        time.sleep(1)

        # 输入我今天最想说的
        browser.find_element_by_id("todaysay").send_keys(say)
        time.sleep(1)

        # 点击开始签到
        browser.find_element_by_css_selector("img[src='source/plugin/dsu_paulsign/img/qdtb.gif']").click()
        print('成功签到成都电玩网，用户ID：' + username)
    except EnvironmentError:
        print('成都电玩网网站已经签到过，用户ID：' + username)

    time.sleep(2)
    browser.quit()

def mmy(username, password, say):
    url = 'https://mmy.la/forum.php'

    # 设定无界面chromedriver
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_option.add_argument('window-size=800x600')  # 指定浏览器分辨率
    chrome_option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_option.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    chrome_option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    chrome_option.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    '''
    browser = webdriver.Chrome(chrome_options=chrome_option)时会出现警告信息：
    #DeprecationWarning: use options instead of chrome_options warnings.warn('use options instead of chrome_options', DeprecationWarning
    根据源码的提示发现使用chrome_options 时会将chrome_options 值传给options,然后在给一个警告信息，\
    根据错误信息已经源码的注解了解到未来options会取代chrome_options，所以我们只需要chrome_options改成options即可，\
    该问题应该在最近的版本更改的目前我这边使用的是selenium==3.9.0，有兴趣的可以去看下官方文档，那个版本开始做的此项的修改。
    '''
    # 调用chromedriver
    browser = webdriver.Chrome(options=chrome_option)
    try:
        browser.get(url)
    except EnvironmentError:
        print('慢慢游网站已失效或网络连接超时，请检查网站或网络')
    time.sleep(1)

    # 填写用户名
    browser.find_element_by_name("username").send_keys(username)
    time.sleep(1)

    # 填写密码
    browser.find_element_by_name("password").send_keys(password)
    time.sleep(1)

    # 点击登入
    browser.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(1)

    # 签到领奖
    browser.find_element_by_css_selector("font[color='red']").click()
    time.sleep(1)

    try:
        # 选择心情
        browser.find_element_by_css_selector("img[src='source/plugin/dsu_paulsign/img/emot/ng.gif']").click()
        time.sleep(1)

        # 填写想说的话
        browser.find_element_by_name("todaysay").send_keys(say)
        time.sleep(1)

        # 点击签到
        browser.find_element_by_css_selector("button[class='pn pnc']").click()
    except EnvironmentError:
        print('慢慢游网站已经签到过，用户ID：' + username)


    time.sleep(2)
    browser.close()
