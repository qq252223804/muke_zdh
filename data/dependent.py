from util.operation_excel import OperationExcel
from data.get_data import GetData
from base.runmethod import RunMethod
from jsonpath_rw import jsonpath, parse
import json,re

class DependentData:
    def __int__(self):
        pass
        # RunMethod()
        # GetData()
        # OperationExcel()
        # self.case_id=case_id            # 实例化操作
        # self.opera_excel=OperationExcele()
        
    #通过case_id去获取case_id整行数据
    @staticmethod
    def get_case_line_data(case_id):

        rows_data=OperationExcel().get_num_data(case_id)
        return rows_data
    # 执行case_id 依赖测试用例，获取返回结果
    @staticmethod
    def run_dependent(case_id):  
        row_num=OperationExcel().get_row_num(case_id)       #获取行号
        request_data=GetData().get_request_data(row_num)
        header=GetData().is_header(row_num)
        method=GetData().get_request_method(row_num)
        url=GetData().get_request_url(row_num)
        res=RunMethod().run_main(method,url,request_data,header)
        return json.loads(res)
    
    #根据依赖的key 去获取执行case依赖 字段 的响应然后返回
    @staticmethod
    def get_data_for_key(self,row,case_id):
        depend_key=GetData().get_depend_key(row)  #依赖数据的key
        response_data=self.run_dependent(case_id)  #运行依赖用例 得响应数据
        # json_exe = parse(depend_key)
        # modle=json_exe.find(response_data)
        # return [math.value for math in modle][0]
        #第二种
        list=[item for item in response_data]
        return list[0].get(depend_key)
        #第三种
        # list2=re.findall(r'depend_key: '(.+?)',str(response_data))
        # print(list2[0])
        


        
        
        
        
        