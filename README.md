```
### 项目基本介绍

```
1. 开发环境：deepin Linux/mac os
2. 配置：python3+pytest+requests
3. 安装：
mac ：
  使用homebrew安装python3，pip3就可以
  pip3 install -U pytest 
  pip3 install requests
Linux：
  一般linux会安装python2.7，和python3.5，只需要自己安装pip就可以
  sudo apt-get install -y python3-pip  
  pip3 install -U pytest 
  pip3 install requests
4.已知其他配置需要：
 LibreSSL 2.9.1
 可以使用公司镜像，安装已经编译过的软件就不会有这些问题
5. 安装生成报告的库
	pytest简单的生成报告的库：pytest-html
		pip3 install pytest-html
	allure报告模板安装：
		先下载 pip3 install allure-pytest
		在下载allure-command工具
		https://github.com/allure-framework/allure2/releases
		下载合适的之后将bin目录下的执行文件allure添加到环境变量或者bashrc下
````
### 项目目录介绍

├── Config                  # 配置文件路基
│   ├── Config.ini
│   ├── GlobalConfig.py     # 读取配置文件
│   ├── __init__.py
├── Log                     # 日志文件路径
│   └── 2019-11-11.log
├── README.md               # 简介
├── Report                  # 测试报告
│   └── testreport.html
├── Run_AllCase.py          # 执行用例入口
├── TestCase                # 测试用例文件
│   ├── TC_Get_Baidu.py     # 测试用例 
│   └── __init__.py
├── TestData                # 测试数据
│   ├── __init__.py
│   └── case.xls
├── cert                    # 证书文件
└── public                  # 公共方法
    ├── Common              
    │   ├── ConfigHttp.py   # http封装
    │   ├── CreateLog.py    # 创建日志
    │   ├── DoExcel.py      # 读取测试数据
    │   ├── ReadConfigini.py# 读取配置文件
    │   ├── SendMail.py     # 发送邮件
    │   ├── __init__.py
    │   └── generate_sessId.py # 获取sessid
    ├── InterTest
    │   ├── GetBaidu.py
    │   └── __init__.py
    ├── __init__.py