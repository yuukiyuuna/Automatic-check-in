关于本脚本
===

关于使用方法： 
---
  目前还没有在linux环境下使用  
  测试环境为pythonPython 3.7.1 + selenium 3.141.0 + ChromeDriver 2.45 + Google Chrome 71.0.3578.98（正式版本）（64 位）  
  请下载与自己的谷歌浏览器对应的ChromeDriver，放在C:\usr\bin目录中  
  注：只要配置好环境变量，能够直接使用即可，不一定必须放在usr/bin的目录下  
  
配置好init文件后，直接运行run.py即可      


关于作者的自我介绍：
---  
  因为想弄一个自动签到的脚本，但自己又不精通python，所以此脚本也就是个练习脚本了。  
  使用的是selenium + chromedrvier来实现的。在这里并没有使用cookie，因为有的网站cookie时间一长会超时  
  欢迎大家跟我这个初学者一起来研究python！！  

关于已知问题陈述：  
1、每天的第一遍执行若无其他因素没问题第二遍执行就会报错。（若有大神可以赐教的话请务必联系我）
    原因是我在主脚本调用函数的时候增加了try方法，但不知为何方法并没有生效（未来有时间回去修复）
    在签到cdtkdw和mmy时因为是查找的心情图片；已签到后将查不到心情图片，导致程序报错。  
2、因为并没有增加其他判断方法，只写了最基本的签到流程和最基础的检查错误手段，有很多报错将会直接导致整体程序中断。
    届时请直接修改init配置里的状态参数，跳过有问题的网站  
3、因为初学者，因此需要时间去测试带有验证码机制的网站，所以目前也就写了三个我自己常用的网站=。=  
    

关于未来（如果不鸽的话）修改方向：  
1、增加判断是否成功登入的功能  
2、增加多点的网站来自动签到  
3、增加查询金币、登记等信息的功能  
