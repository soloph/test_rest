#!/usr/bin/env python
# coding:utf-8

import smtplib
from email.mime.text import MIMEText

mail_host = "smtp.126.com"
mail_user = "soloph_test"
mail_pass = "soloph_test_pass"
mail_postfix="126.com"

def send_mail(to_list, sub, context):
    me = mail_user + "<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(context)
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        send_smtp = smtplib.SMTP()
        send_smtp.connect(mail_host)
        send_smtp.login(mail_user, mail_pass)
        send_smtp.sendmail(me, to_list, msg.as_string())
        send_smtp.close()
        return True
    except Exception, e:
        print(str(e))
        return False

if __name__ == '__main__':
    mailto_list=["1846942638@qq.com","soloph@sina.com"]
    if (True == send_mail(mailto_list,"subject","context")):
        print ("ok")
    else:
        print ("error")