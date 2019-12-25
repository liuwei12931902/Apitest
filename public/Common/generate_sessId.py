"""
Author: ssc
Datetime: 2019/5/27 上午9:19
FILE : generate_url.py

1.先取出url
2.格式化，然后去重
3.拼接url

需要重新生成的
1. sessid
2. xz_sign

"""
import sys
import json
import requests
import hashlib
import time
import urllib.parse
from datetime import datetime

sys.path.append("..")
from common import paramsforxzsign


# uniqueId=869600040058817

class Generate_sessId:

    def __init__(self, username, password):
        self.response = self.generate_url(username, password)

    # 调取登录接口，查找sessid和xz_token
    def getSessionid(self, username, password, imagecode):
        t = time.time()
        url = ''
        link = ""
        userName = username
        password = password
        imageCode = imagecode
        time_stamp = str(int(round(t * 1000)))
        get_url = 'userName=' + userName + '&password=' + password + '&imageCode=' + imageCode + '&_=' + time_stamp + '&nationCode=86&nationName=CN&dispathChannel=xiaozhu'

        params_before = urllib.parse.unquote(get_url, 'utf-8')
        params_after = urllib.parse.parse_qs(params_before)
        for s in params_after.keys():
            params_after[s] = params_after.get(s)[0]

        requests.packages.urllib3.disable_warnings()
        xz_sign = paramsforxzsign(link, params_after)
        response = requests.get(url + link, params=xz_sign, verify=False, cert='../config/client.pem').json()
        return response

    def generate_url(self, username, password):
        imagecode = self.getVerificationCode()
        response = self.getSessionid(username, password, imagecode)
        return response


if __name__ == '__main__':
    fk = Generate_sessId('', '')
    fk_sessid = fk.response['content']['sessId']
    print(fk_sessid)
