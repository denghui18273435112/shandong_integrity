import pytest
from tools.ExcelData import ExcelData
import allure
from tools.caseCheck import caseCheck
from lib.all import all
import requests
import json
from tools.Base import *
from tools.commonly_method import *

def setup_module():
    allure.attach(body="TEST-01", name="所有用例执行前，执行一次", attachment_type=allure.attachment_type.TEXT)
def teardown_module():
    #清空导入数据
    allure.attach(body="TEST-06", name="所有用例执行完，执行一次", attachment_type=allure.attachment_type.TEXT)
    if environment=="line":
        #登录
        data = {"type":"I","Name":"zxs-sd","Vcode":"denghui","Pwd":"21ad15b19ad2fcc3ed51c089a8cc39ca"}
        url = "http://60.216.62.188:10263/base/home/Login"
        header = {"Content-Type": "application/json"}
        body = requests.post(url=url,json=data,headers=header)
        token = "{0}={1}".format("cipmcms-token",body.cookies["cipmcms-token"])
        allure.attach(body=token, name="登录后拼接的token", attachment_type=allure.attachment_type.TEXT)
        #身份证查询个人信息 删除
        for x in ["431226199407030014","431226199407030030","431226199407030057","431226199407030073",
                    "43122619940703009X","436199407030110","226199407030137","43122617030153","619940703017X","99407030196"]:
            url1 = "http://60.216.62.188:10263/api/member/DeleteMember"
            data1= {"idnumber":"{}".format(x)}
            header1 = {"Cookie":token}
            body1 = requests.post(url=url1,json=data1,headers=header1)
            body1.json()
            allure.attach(body=json.dumps(body1.json()), name="身份证查询个人信息查询返回的数据", attachment_type=allure.attachment_type.TEXT)

data_storage ={}
@allure.epic("山东诚信系统")
class Test_all(object):
    @pytest.mark.test
    @pytest.mark.run(order=1001)
    @pytest.mark.parametrize("inData",ExcelData("ED_,PD_,AA"))
    def test_precondition(self,all_token,inData):
        """所有前置条件"""
        res =all().case_ALL(all_token,inData,data_storage)
        caseCheck().case_Check(res[0])

    @pytest.mark.test1
    @pytest.mark.run(order=1003)
    @pytest.mark.parametrize("inData",ExcelData("case"))
    def test_HP(self,all_token,inData):
        """所有case开头的"""
        res =all().case_ALL(all_token,inData,data_storage)
        caseCheck().case_Check(res[0])