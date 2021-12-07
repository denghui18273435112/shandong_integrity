import pytest
from configs.path import *
from lib.all import *
from lib.login import login
from tools.ExcelData import ExcelData
from selenium import webdriver
from configs.path import *
import time
import imageio
import pytest
import os
from tools.verification_code import *
import requests
from configs.path import *
from configs.conf import *

def login(case_id="login-002"):
    """
    支持不同角色登录
    :param case_id:
    :return:
    """
    token = ""
    while True:
        res=requests.get("{}/base/home/VerificationCode?".format(url))
        if res.status_code==200:
            imgname  = file_data+os.sep+'code.jpg'
            with open(imgname,"wb") as fd:
                fd.write(res.content)
        vcode = res.cookies["vcode"]
        headers= {"cookie":"{0}={1}".format(vcode_name,vcode)}
        data = json.loads(ExcelData(case_id)[0]["params"])
        data["Vcode"] = verification_code("code.jpg")
        body = requests.post(url="{}/base/home/Login".format(url),json=data,headers=headers)
        if body.json()["msg"]=="登录成功":
            token = "{0}={1};{2}={3}".format(cookie_name,body.cookies["sd-siccms-token"],vcode_name,vcode)
            break
        else:
            print("再次登录")
    return token

def  requests_zzl(case_id,token):
    """
接口请求
    :return:
    """
    table_data = ExcelData(case_id)[0]
    url_new = url+table_data["url"]
    data_new = json.loads(table_data["params"])
    header = {"Cookie":"{0}".format(token)}
    return requests.post(url=url_new, headers=header, json=data_new).json()



if __name__ == '__main__':

    print(requests_zzl("case_3_creditlogGetAuditList_01",login())["data"]["list"][0]["id"])