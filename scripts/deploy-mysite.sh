#!/bin/sh

systemctl status supervisord
systemctl start supervisord
systemctl stop supervisord


supervisorctl stop chinamobile
supervisorctl status chinamobile
supervisorctl restart chinamobile


# 启动服务器
-------------
service nginx start
service nginx status
service nginx restart
service nginx stop
-------------


