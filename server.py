#!/usr/bin/env python
# coding:utf-8

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.options import define, options, parse_command_line

from settings import SERVER_SETTINGS
from urls import urls

define("port", default=7900, help="run on the given port", type=int)

def main():
  parse_command_line()
  http_server = HTTPServer(Application(handlers=urls, **SERVER_SETTINGS))
  http_server.listen(options.port)
  IOLoop.instance().start()

if __name__ == "__main__":
  main()
