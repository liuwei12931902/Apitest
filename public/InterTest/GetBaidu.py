import requests
from public.Common.ConfigHttp import ConfigHttp
from public.Common.DoExcel import ReadExcel


def BaiduGet():
    excel = ReadExcel('case.xls', 'sheet1')
    row = excel.get_row_num(0, 'bd-001')
    url = excel.read_excel(row, 2)
    params = {
        'wd': 'leo'
    }
    headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q = 0.9,image/webp,image/apng,*/*;q = 0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9, en-US;q=0.8, en;q=0.7",
        "User-Agent": "Mozilla/5.0(Macintosh;Intel Mac OS X 10_14_6) AppleWebKit/537.36(KHTML,likeGecko) Chrome/78.0.3904.87Safari/537.36"
    }
    new = ConfigHttp('HTTP', 'baseurl', 'port', 'timeout')
    new.set_url(url)
    new.set_headers(headers)
    new.set_params(params)
    r = new.get()
    print(r.status_code)
    print('==========================')
    excel.write_excel(0, row, 10, r.status_code)
