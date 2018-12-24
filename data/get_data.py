from util.operation_excel import OperationExcel
from data.data_config import *
"""引进所有的方法
"""
from util.operation_json import Operationjson
import json

class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel() # 类的实例化对象 方法

    #去获取excel行数,就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    #获取是否执行
    def get_is_run(self,row):
        flag = None
        col = int(get_run())
        run_model = self.opera_excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    #是否携带header
    def is_header(self,row):
        col = int(get_header())
        header = self.opera_excel.get_cell_value(row,col)
        # print(type(header))
        if header != '':   #判断是否不为空
            return eval(header)    #！！！！将取出来的str-dict
           
        else:
            return None
    #获取请求方式
    def get_request_method(self,row):
        col = int(get_run_way())
        request_method = self.opera_excel.get_cell_value(row,col)
        return request_method

    #获取url
    def get_request_url(self,row):
        col = int(get_url())
        url = self.opera_excel.get_cell_value(row,col)
        return url

    #获取请求数据
    def get_request_data(self,row):
        col = int(get_data())
        data = self.opera_excel.get_cell_value(row,col)
        if data == '':
            return None
        return data

    #通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json = Operationjson()
        request_data =opera_json.get_data(self.get_request_data(row))
        return request_data

    #获取预期结果
    def get_expcet_data(self,row):
        col = int(get_expect())
        expect = self.opera_excel.get_cell_value(row,col)
        if expect == '':
            return None
        return expect  #  获取的预期结果为str格式
    #写入实际结果
    def write_result(self,row,value):
        col =int(get_result())
        result =self.opera_excel.write_value(row,col,value)
        return result
    #获取依赖数据的key
    def get_depend_key(self,row):
        col=int(get_data_depend())
        depent_key=self.opera_excel.get_cell_value(row,col)
        if depent_key =='':
            return None
        else:
            return depent_key
        
    def is_case_depend(self,row):
        pass

# a=GetData()
# b=a.get_expcet_data(3)
# print(b)
# print(type(b))