import os
from public.Common.ReadConfigini import ReadConfigini


# 此文件目录
file_path = os.path.split(os.path.realpath(__file__))[0]


# 实例化配置文件对象
read_config = ReadConfigini(os.path.join(file_path, 'Config.ini'))


# 项目目录
project_path = read_config.getConfigValue('project', 'project')


# 日志目录
log_path = os.path.join(project_path, 'Log')


# 测试报告目录
report_path = os.path.join(project_path, 'Report')


# 测试数据
data_path = os.path.join(project_path, 'TestData')

# 配置文件目录
configIni_path = os.path.join(project_path, 'Config/Config.ini')
