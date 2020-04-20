#!/usr/bin/env python
# -*- coding:utf-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def email(email_list, content, subject="这里写发送主题(标题)"):
    #email_list就是给谁发，可以群发！
    msg = MIMEText(content, 'locarjcfuzpkbdff', 'utf-8')       #创建一个对象，
    msg['From'] = formataddr(["测试测试测试邮件",'1017140407@qq.com'])   #from就是前面中文的发件人，后面发件人邮箱
    msg['Subject'] = subject    #Subject就是主题，他发送的头。
    # 要先在自己邮箱开启SMTP/IMAP服务
    server = smtplib.SMTP("smtp.qq.com",587)       #这里写服务器，还有对应端口
    server.login("1017140407@qq.com", "locarjcfuzpkbdff")       #账户和密码
    server.sendmail('1017140407@qq.com', email_list, msg.as_string())
    server.quit()

#还可以用下面的方法群发
# email(['要发的邮箱1@live.com','要发的邮箱2@live.com'], '要发的主题')
email(['18801433900@163.com','745300380@qq.com'],'1111')