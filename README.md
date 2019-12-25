``````

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