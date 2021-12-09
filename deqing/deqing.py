# -*- coding:utf-8 -*-
# !/usr/bin/env

# 德勤进程检测
# Mr: Bert

import os
import time
import requests
import sys
while True:

    url = 'curl -i http://wechat.9client.com'
    url3 = 'http://wechat.9client.com'
 #ping 这个域名是否可以连通, -w 最大超时时间超出后退出报异常 -c 试探域名连通性的次数 -i 每一次试探的时间>间隔.
#   url2 = 'ping -w 6 -c 5 -i 3 wechat.9client.com'
    err = """curl 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=62086a86-4b8b-457f-8428-865e\' -H \'Content-Type: application/json\' -d \'{"msgtype": "text","text": {"content": "德勤服务进程出现异常情况\n请引起注意,请及时排出故障"} }'"""
    http = os.system(url + ' >/dev/null')
    #requestse = requests.get(url3)
    #httpt = requestse.ok         #获取请求响应的布尔值   
    if http:
        os.system(err)
      #  sys.exit(0)
    else:
        time.sleep(600)
    #    print (11111111111)
    time.sleep(60)
   # print("222222222222222222")
