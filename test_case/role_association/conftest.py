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
    """所有账号登录，返回token"""
    return login("login-integrity-001"),login("login-integrity-002"),login("login-integrity-003"),login("login-integrity-004"),login("login-integrity-005"),login("login-integrity-006"),login("login-integrity-007")

@pytest.fixture(scope="session")
def all_token(token):
    """把所有的token存放到字典中"""
    new_token ={}
    for x in range(len(token)):
        new_token["token-00{}".format(x+1)] = token[x]
    return new_token