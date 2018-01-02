#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
import chat


sys.path.insert(0, abspath(dirname(__file__)))
app = chat.app
application = chat.socketio.run(app)

"""
建立一个软连接
ln -s /root/WebProjects/chat_websocket/bbs.conf /etc/supervisor/conf.d/chat.conf

ln -s /root/WebProjects/chat_websocket/bbs.nginx /etc/nginx/sites-enabled/chat



➜  ~ cat /etc/supervisor/conf.d/chat.conf

[program:bbs]
command=/usr/local/bin/gunicorn wsgi -c gunicorn.config.py
directory=/var/www/bbs
autostart=true
autorestart=true




/usr/local/bin/gunicorn wsgi
--bind 0.0.0.0:2001
--pid /tmp/飙泪og.pid
"""


