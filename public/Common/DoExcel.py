import xlrd
from xlutils.copy import copy
from Config import GlobalConfig
import os


# workbook = xlrd.open_workbook('Demo.xlsx')
# print(workbook.nsheets)
#
# # 获取sheet对象
# sheet_name = workbook.sheet_names()
# sheet1 = workbook.sheet_by_name(sheet_name[0])
#
# # 读取第一行数据
# rows = sheet1.row_values(0)
# print(rows)
# # 读取第一列数据
# cols = sheet1.col_values(0)
# print(cols)
#
# # 读取单元格
# sheetValue = sheet1.cell(1, 0).value
# print(sheetValue)

# 对Excel 进行封装，新增对Excel 中写入用例
data_path = GlobalConfig.data_path


class ReadExcel(object):
    '''
        读取Excel
    '''
    def __init__(self, fileName, sheetName):
        '''

        :param fileName:Excel名字
        :param sheetName:sheet名字
        '''
        self.fileName = os.path.join(data_path, fileName)
        self.workbook = xlrd.open_workbook(self.fileName)
        self.sheetName = self.workbook.sheet_by_name(sheetName)

    def get_row_num(self, cols_num, case_id):
        '''
         作用：找到与case_id相匹配的行号
        :param cols_num:
        :param case_id:
        :return:
        '''
        cols = self.sheetName.col_values(cols_num)
        colnum = 0
        for col_data in cols:
            if col_data == case_id:
                break
            colnum += 1
            return colnum

    def get_rowline_data(self, row):
        '''
        作用：根据get_row_num返回的行号 ，获取某行的值
        :param row: 在get_row_num中返回的行号
        :return:
        '''
        rowline_data = self.sheetName.row_values(row)
        return rowline_data

    def read_excel(self, rowNum, colNum):
        '''
        作用：获取某个单元格的值
        :param rowNum:
        :param colNum:
        :return:
        '''
        value = self.sheetName.cell(rowNum, colNum).value
        return value

    def write_excel(self, sheetnum, row, col, value):
        '''
        作用：写入Excel 数据
        :param sheetnum:
        :param row:
        :param col:
        :param value:
        :return:
        '''
        newworkbook = xlrd.open_workbook(self.fileName)
        newbook = copy(newworkbook)
        sheet = newbook.get_sheet(sheetnum)
        sheet.write(row, col, value)
        newbook.save(self.fileName)


if __name__ == '__main__':
    excel = ReadExcel('case.xls', 'sheet1')
    row = excel.get_row_num(0, 'bd-001')
    print(row)
    row_data = excel.get_rowline_data(row)
    print(row_data)
    print('==============================')
    excel.write_excel(0, 6, 4, 'test')
