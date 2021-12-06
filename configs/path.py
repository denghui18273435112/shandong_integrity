#-*- conding:utf-8 -*-
#@File      :path.py
#@Time      : 14:32
#@Author    :denghui
#@Email     :314983713@qq.com
#@Software  :PyCharm
import os
current =os.path.abspath(__file__)                          #当前文件的路径
BASE_DIR = os.path.dirname(os.path.dirname(current))        # 当前项目的绝对路径

#文件夹路径
config_path = BASE_DIR +os.sep+"config"
log_path = BASE_DIR +os.sep+"logs"
data_path =BASE_DIR +os.sep+"docs"
file_path =BASE_DIR +os.sep+"file"
report_path =BASE_DIR +os.sep+"report"
testcase_path =BASE_DIR +os.sep+"test_case"
file_data =BASE_DIR +os.sep+"data"
result_path = report_path+os.sep+"result"
allure_reportt_path = report_path+os.sep+"allure_report"
screenshots_path = file_path+os.sep+"screenshots"
process_file_path =BASE_DIR +os.sep+"process_file"
file_data_path_1 = file_data+os.sep+"业务流程"
file_data_path_2 = file_data+os.sep+"格式校验"

#文件路径
_config_file = config_path +os.sep+"conf.yaml"            #定义conf.yaml的路径
_yonglie_file = config_path +os.sep+"yonglie.yaml"            #定义conf.yaml的路径
_db_config_file = config_path +os.sep+"db_conf.yaml"     #定义db_conf.yaml的路径
test_xlsx = data_path+os.sep+"ctest.xlsx"

#上传文件
file_application = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

excel_1_name = "在职-异常-证件号码重复.xlsx"
excel_1 = file_data_path_2 +os.sep+excel_1_name

excel_2_name = "在职-异常-已在别的公司.xlsx"
excel_2 = file_data_path_2 +os.sep+excel_2_name

excel_3_name = "在职-异常-字段的基本格式.xlsx"
excel_3 = file_data_path_2 +os.sep+excel_3_name

excel_4_name = "在职-正常-导入4人数据.xlsx"
excel_4 = file_data_path_2 +os.sep+excel_4_name

excel_5_name = "1在职-正常-导入1人数据.xlsx"
excel_5 = file_data_path_1 +os.sep+excel_5_name

excel_6_name = "2 山东在职人员业务指标导入模板.xlsx"
excel_6 = file_data_path_1 +os.sep+excel_6_name