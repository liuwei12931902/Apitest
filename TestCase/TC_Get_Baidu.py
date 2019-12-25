import requests
import unittest
import logging
from public.Common.ConfigHttp import ConfigHttp
from public.Common.DoExcel import ReadExcel
from public.InterTest.GetBaidu import BaiduGet
from public.Common.CreateLog import RunLogger


class BaiduGetHeader(unittest.TestCase):
    '''

    '''
    def setUp(self):
        self.baidu = BaiduGet()
        self.logger = RunLogger()

    def test_baidu_get(self):
        pass

    def tearDown(self):
        pass
