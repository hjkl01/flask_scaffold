#!/usr/bin/env python3

# gunicorn.py
import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing

bind = '0.0.0.0:8000'
backlog = 512  # 监听队列
# chdir = '/home/test/server/bin'  #gunicorn要切换到的目的工作目录
timeout = 30
worker_class = 'gevent'

workers = multiprocessing.cpu_count() * 2 + 1  # 进程数
threads = 20
loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
"""
其每个选项的含义如下：
h          remote address
l          '-'
u          currently '-', may be user name in future releases
t          date of the request
r          status line (e.g. ``GET / HTTP/1.1``)
s          status
b          response length or '-'
f          referer
a          user agent
T          request time in seconds
D          request time in microseconds
L          request time in decimal seconds
p          process ID
"""

if not os.path.exists('logs'):
    os.mkdir('logs')
accesslog = "./logs/gunicorn_access.log"  # 访问日志文件
errorlog = "./logs/gunicorn_error.log"  # 错误日志文件
