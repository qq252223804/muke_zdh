from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
import json,requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# ---------------------
class RunTest:
    def __int__(self):
        RunMethod()   #初始化 类对象
        GetData()
        CommonUtil()
    # 程序执行的
    def go_on_run(self):
        rows_count=GetData().get_case_lines()  #获取excel 有数据的行数
        # return rows_count

        for i in range(1,rows_count):
            # print(i)
            url=GetData().get_request_url(i)
            # print(url)
            method=GetData().get_request_method(i)
            is_run=GetData().get_is_run(i)
            data=GetData().get_request_data(i)# 从excel表格中取数据
            # print(data)
            # print(type(data))
            expect =GetData().get_expcet_data(i)
            print(expect)
            # print(type(expect))
            headers =GetData().is_header(i)
            # print(headers)
            # print(type(headers))
            if is_run:
                res=RunMethod().run_main(method,url,data,headers)

                if CommonUtil().is_contain(expect,res):   #此处只是一个判断的封装类
                # if expect in res:
                    GetData().write_result(i,'测试通过')
                    print('测试通过')
                    # return True      #这里放return True 只会执行一次就停止，针对于单个用例的方法判断有效，
                                        #for 循环就会失效 所以建议封装一个类 判断放在类中
                else:
                    GetData().write_result(i,'测试失败')
                    print('测试失败')
                    # return False
                # print(type(res))
                print (res)

if __name__ == '__main__':                        
    run=RunTest()
    RUN=run.go_on_run()
    print(RUN)
    json.dumps(RUN, indent=2, sort_keys=True)



