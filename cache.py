#!/usr/bin/env python
# coding:utf-8

import memcache
import settings

cache = memcache.Client([settings.DEFAULT_MEMCACHE_LOCATION], debug=0)

def main():
  print cache.set('1', 1)
  print cache.get('1')

if __name__ == '__main__':
  main()
