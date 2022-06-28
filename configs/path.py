#-*- conding:utf-8 -*-
#@File      :path.py
#@Time      : 14:32
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import os
current =os.path.abspath(__file__)                          #当前文件的路径
BASE_DIR = os.path.dirname(os.path.dirname(current))        # 当前项目的绝对路径

#一级文件夹路径
config_path = BASE_DIR +os.sep+"config"
data_path =BASE_DIR +os.sep+"data"
docs_path =BASE_DIR +os.sep+"docs"
lib_path = BASE_DIR +os.sep+"lib"
logs_path = BASE_DIR +os.sep+"logs"
report_path =BASE_DIR +os.sep+"report"
test_case_path =BASE_DIR +os.sep+"test_case"
tools_path =BASE_DIR +os.sep+"tools"
report_path =BASE_DIR +os.sep+"report"

#二级文件夹路径
result_path = report_path+os.sep+"result"
allure_reportt_path = report_path+os.sep+"allure_report"
file_path= data_path+os.sep+"file"

#文件路径
_config_file = config_path +os.sep+"conf.yaml"            #定义conf.yaml的路径
_yonglie_file = config_path +os.sep+"yonglie.yaml"            #定义conf.yaml的路径
_db_config_file = config_path +os.sep+"db_conf.yaml"     #定义db_conf.yaml的路径
test_xlsx = data_path+os.sep+"ctest.xlsx"

#文档路径
file_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
file_path_01= docs_path+os.sep+"00-山东诚信系统用例.xls"
file_path_02= file_path+os.sep+"01-山东在职人员导入模板.xlsx"
file_path_03= file_path+os.sep+"02-山东离职人员导入模板.xlsx"
file_path_04= file_path+os.sep+"03-入职前诚信级别批量查询模板.xlsx"
file_path_05= file_path+os.sep+"99-图片.jpg"
file_path_06= file_path+os.sep+"111_431226199407030014.jpg"
file_path_07= file_path+os.sep+"04-山东在职人员业务指标导入模板.xlsx"
file_path_08= file_path+os.sep+"05-山东讲师资质导入模板.xlsx"
