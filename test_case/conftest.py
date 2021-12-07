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
from tools.commonly_method import *
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
    """省协会获取登录token"""
    return login("login-001")

@pytest.fixture(scope="session")
def token_province():
    """省公司获取登录token"""
    return login("login-002")

@pytest.fixture(scope="session")
def token_city():
    """市公司获取登录token"""
    return login("login-003")

@pytest.fixture(scope="session")
def company(token):
    """省协会-获取当前账号登录的所属公司id"""
    return requests_zzl("case_1_GetCurrentAllCompany",token)["data"][0]["id"]

@pytest.fixture(scope="session")
def company_province(token_province):
    """省公司-获取当前账号登录的所属公司id"""
    return requests_zzl("case_1_GetCurrentAllCompany",token_province)["data"][0]["id"]

@pytest.fixture(scope="session")
def company_city(token_city):
    """地市公司-获取当前账号登录的所属公司id"""
    return requests_zzl("case_1_GetCurrentAllCompany",token_city)["data"][0]["id"]

@pytest.fixture(scope="session")
def rewards_id(token):
    """奖惩个人详情中需要删除的id"""
    return all(token=token,inData=ExcelData("case_1_lecturermanageGetAwardInfo")[0],conftest=False).ParameterlessAdjustment(company=company)[1].json()["data"][0]
