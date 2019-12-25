import requests
from public.Common.ReadConfigini import ReadConfigini
from Config import GlobalConfig

config = GlobalConfig.configIni_path
ReadConfig = ReadConfigini(config).getConfigValue


class ConfigHttp(object):
    def __init__(self, section, host, port, timeout):
         '''
         读取config.ini 文件中的全局配置信息，如baseurl、端口、timeout
         :param section:
         :param host:
         :param port:
         :param timeout:
         '''
         self.host = ReadConfig(section, host)
         self.port = ReadConfig(section, port)
         self.timeout = ReadConfig(section, timeout)
         self.headers = {}
         self.params = {}
         self.data = {}
         self.url = None
         self.files = {}

    def set_url(self, url):
        '''
        拼接完成的接口测试地址
        :param url:
        :return:
        '''
        self.url = self.host + url

    def set_headers(self, headers):
        self.headers = headers

    def set_params(self, params):
        self.params = params

    def set_data(self, data):
        self.data = data

    def set_files(self, files):
        self.files = files

    def get(self):
        '''
        重写get
        :return:
        '''
        try:
            repones = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(self.timeout))
            return repones
        except TimeoutError:
            return None

    def post(self):
        '''
        重写post
        :return:
        '''
        try:
            repones = requests.get(self.url, params=self.params, headers=self.headers,json=self.data, files=self.files, timeout=float(self.timeout))
            return repones
        except TimeoutError:
            return None

# 演示示例
# if __name__ == '__main__':
#     host = 'https://www.baidu.com'
#     url = '/s'
#     port = 443
#     timeout = 2
#     params ={
#         'wd':'leo'
#     }
#     headers ={
#         "Accept":"text/html,application/xhtml+xml,application/xml;q = 0.9,image/webp,image/apng,*/*;q = 0.8,application/signed-exchange;v=b3",
#         "Accept-Encoding": "gzip,deflate,br",
#         "Accept-Language": "zh-CN,zh;q=0.9, en-US;q=0.8, en;q=0.7",
#         "User-Agent": "Mozilla/5.0(Macintosh;Intel Mac OS X 10_14_6) AppleWebKit/537.36(KHTML,likeGecko) Chrome/78.0.3904.87Safari/537.36"
#     }
#     new = ConfigHttp(host, port, timeout)
#     new.set_url(url)
#     new.set_headers(headers)
#     new.set_params(params)
#     r = new.get()
#     print(r.status_code)
