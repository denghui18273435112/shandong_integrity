import pytest
from tools.ExcelData import ExcelData
import allure
from tools.caseCheck import caseCheck
from lib.all import all

@allure.epic("山东诚信系统")
class Test_all(object):

    @pytest.mark.parametrize("Data",ExcelData("case_3"))
    def test_ParameterlessAdjustment(self,token,token_province,token_city,Data,company,company_province,company_city):
        """所有测试用例集合"""
        res =all(token=token,token_province=token_province,token_city=token_city,inData=Data).\
            ParameterlessAdjustment(company=company,company_city=company_city,company_province=company_province)
        caseCheck().case_Check(res[0])