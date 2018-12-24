from typing import Any

import xlrd
from xlutils.copy import copy
# data=xlrd.open_workbook('../dataconfig/interface.xlsx')
# tables=data.sheets()[0]
# print(tables.nrows)  #行数
# print(tables.ncols)  #列数
# print(tables.cell_value(2,3))

class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):   #初始化方法
        if file_name:
            self.file_name=file_name
            self.sheet_id=sheet_id          
        else:
            self.file_name='E:/muke_zdh/dataconfig/interface.xlsx'
           
            self.sheet_id=0

        self.data = self.get_data()

    # 获取某页表格所有数据
    def get_data(self):
        data=xlrd.open_workbook(self.file_name)
        tables=data.sheets()[self.sheet_id]
        return tables

    #获取单元格的行数
    def get_lines(self):
        return self.data.nrows
    #获取[某一指定单元格]的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)
    #写入数据
    def write_value(self,row,col,value):
        """
        写入excel数据
        :param row:
        :param col:
        :param value:
        :return:
        """
        read_data = xlrd.open_workbook(self.file_name)
        #拿到的数据复制一份
        write_data =copy(read_data)
        sheet_data =write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    #根据行号,获取【该行内容 】
    def get_row_values(self, row):
        rows_data = self.data.row_values(row)  # 获取某一行内容  row_values
        return rows_data
  

    # 根据列号，获取【该列所有内容-cases-id】
    def get_cols_values(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)  # 获取某一列内容  col_values
        else:
            cols = self.data.col_values(0)  # 获取第一列内容
        return cols
     # 根据依赖的case_id 【循环判断 case_id】 返回对应的行号
    def get_row_num(self, case_id):
        num = 0
        # cols_data = self.get_cols_data() #获取一列的内容
        for col_data in self.get_cols_values():
            if case_id in col_data:
                return num
            num = num + 1

    # 根据依赖的case_id [拿到行号，找到对应行的内容 ]
    def get_num_data(self, case_id):
        row_num = self.get_row_num(case_id)  #拿到行号
        self.get_row_values(row_num)         #根据行号 获取行内容


   
            
        

if __name__=='__main__':
    opers=OperationExcel()
    print (opers.get_data().ncols)   #打印列数
    print(opers.get_data().nrows)  #打印行数
    print (opers.get_lines())   # 打印行数
    # print(opers.get_cell_value(2,2))