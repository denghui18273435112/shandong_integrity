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
def integrity_association_token():
    """省协会，返回token"""
    return login("login-integrity-003")

@pytest.fixture(scope="session")
def integrity_province_token():
    """省公司，返回token"""
    return login("login-integrity-004")

@pytest.fixture(scope="session")
def integrity_prefectureLevel_token():
    """地市公司公司，返回token"""
    return login("login-integrity-005")

@pytest.fixture(scope="session")
def all_token(integrity_association_token,integrity_province_token,integrity_prefectureLevel_token):
    """把所有的token存放到字典中"""
    new_token ={}
    new_token["integrity_association_token"] = integrity_association_token
    new_token["integrity_province_token"] = integrity_province_token
    new_token["integrity_prefectureLevel_token"] = integrity_prefectureLevel_token
    return new_token