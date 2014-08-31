#!/usr/bin/env python
# coding:utf-8

urls = [
(r'/email/add', 'handler.EmailHandler'),
(r'/email/get', 'handler.EmailHandler'),
(r'/email/get/(\w+)', 'handler.EmailHandler'),
]
