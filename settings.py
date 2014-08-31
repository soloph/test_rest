#!/usr/bin/env python
# coding:utf-8

import sys, os
reload(sys)
sys.setdefaultencoding('utf8')

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = PROJECT_ROOT.replace('\\\\', '/').replace('\\', '/')#for windows
sys.path.insert(0,PROJECT_ROOT)

LOGS_DIR = PROJECT_ROOT + '/logs'
if not os.path.exists(LOGS_DIR):
  os.mkdir(LOGS_DIR)

SERVER_SETTINGS = dict(
  debug=True,
  template_path=os.path.join(os.path.dirname(__file__), "templates"),
  static_path=os.path.join(os.path.dirname(__file__), "static"),
  cookie_secret="__TEST_REST__",
  xsrf_cookies=False,
)

DEFAULT_MEMCACHE_LOCATION = '127.0.0.1:11211'

ACCESS_KEY = '1c420a5d0cf437d260da8e9d641dfb13'
SECRET_ID = 'SHAdsahdadw127862dehadq'

EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 25

DEFAULT_EMAIL_USER = 'soloph@sina.com'
DEFAULT_EMAIL_SUBJECT = 'Thanks for your application'
DEFAULT_EMAIL_CONTENT = '> Dear %s,\n>\n> We have received your application. Please do NOT reply this email.\n>\n> Thanks,\n> Tech Team'

DEDICATED_EMAIL_USER = 'soloph@sina.com'
DEDICATED_EMAIL_SUBJECT = 'Application Received from [%s]'
DEDICATED_EMAIL_CONTENT = '> Received an application from [%s] [%s] at [%s]'
