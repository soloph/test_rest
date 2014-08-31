#!/usr/bin/env python
# coding:utf-8

import datetime
import settings
from cache import cache
from ses import ases
from tornado.web import RequestHandler, asynchronous

class EmailHandler(RequestHandler):
  @asynchronous
  def get(self, *args, **kwargs):
    self.render("email.html")
  
  @asynchronous
  def post(self):
    email = self.get_argument("email", None)
    first_name = self.get_argument("first_name", None)
    last_name = self.get_argument("last_name", None)
    contact_number = self.get_argument("contact_number", None)
    title = self.get_argument("title", None)
    content = self.get_argument("content", None)
    link = self.get_argument("link", None)
    
    cache.set(str(email), [first_name, last_name, contact_number, title, content, link])
    ases.send_mail(settings.DEFAULT_EMAIL_USER, settings.DEFAULT_EMAIL_SUBJECT, settings.DEFAULT_EMAIL_CONTENT % (last_name), email)
    ases.send_mail(settings.DEFAULT_EMAIL_USER, settings.DEDICATED_EMAIL_SUBJECT % (email), settings.DEDICATED_EMAIL_CONTENT % (last_name, first_name, datetime.datetime.now()), settings.DEDICATED_EMAIL_USER)
    self.finish()

def main():
  pass

if __name__ == '__main__':
  main()
