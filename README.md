test_rest
=========

a test of rest request

need install tornado related libs, can be both started in linux and windows.
here the program simply use memcached to save data, so you need install memcached, and start it on port 11211.

start: python server.py
stop: ctrl+c

Because of failure to apply for aws, here used smtplib to send a email synchronously, and you'd better change the host and password in util_mail.

after the server is started, you can visit localhost:7900/email/add to post a request.