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

@pytest.fixture(scope="session",autouse=True)
def empty_report_file():
    """清空report-result文件夹,除environment.properties以外的其它所有文件"""
    try:
        for one in os.listdir(result_path):
            if "environment.properties" not in one:
                os.remove(result_path+os.sep+"{}".format(one))
    except:
        pass

@pytest.fixture(scope="session")
def token():
    """获取登录token"""
    token = ""
    while True:
        res=requests.get("{}/base/home/VerificationCode?".format(url))
        if res.status_code==200:
            imgname  = file_data+os.sep+'code.jpg'
            with open(imgname,"wb") as fd:
                fd.write(res.content)
        vcode = res.cookies["vcode"]
        headers= {"cookie":"{0}={1}".format(vcode_name,vcode)}
        data = json.loads(ExcelData("login-001")[0]["params"])
        data["Vcode"] = verification_code("code.jpg")
        body = requests.post(url="{}/base/home/Login".format(url),json=data,headers=headers)
        token = "{0}={1};{2}={3}".format(cookie_name,body.cookies["sd-siccms-token"],vcode_name,vcode)
        if body.json()["msg"]=="登录成功":
            break
    return token

@pytest.fixture(scope="session")
def company(token):
    """获取当前账号登录的所属公司id"""
    return all(token=token,inData=ExcelData("case_GetCurrentAllCompany")[0],conftest=False).ParameterlessAdjustment()[1].json()["data"][0]["id"]

@pytest.fixture(scope="session")
def rewards_id(token):
    """奖惩个人详情中需要删除的id"""
    return all(token=token,inData=ExcelData("case_lecturermanageGetAwardInfo")[0],conftest=False).ParameterlessAdjustment(company=company)[1].json()["data"][0]


