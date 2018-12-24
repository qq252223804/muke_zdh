import requests
import json


class RunMain:
    # def __init__(self, url, method, data=None,headers=None):  # 构造函数 就不用下面每次实例化了
    #     self.res = self.method_main(url, method, data,headers)

    def GET(self,url, data):
        # url=ReadExcel(0,1,2)
        # data=ReadExcel(0,1,3)
        # url1 = url + '?' + data
        # print url1,data
        # req = urllib2.Request(url1)
        # response = urllib2.urlopen(req)
        # page=response.read()                  #  不采取urllib2进行传参数！！！
        # # print response.getcode,response.msg
        # # print(page)
        # return page

        html = requests.get(url, data)
        # print(html.text)
        print(html.status_code)
        return html.text

    def POST(self,url, data,headers=None):
        # url=ReadExcel(0,3,2)
        # data=ReadExcel(0,3,3)
        # print(data) ,type(data)

        # data1 = data.encode('utf-8')  # 将 Unicode 转换成 str
        # # print data,type(data1)
        # datas = eval(data1)  # 将str 转换成 dict
        # # print(datas),type(datas)

        html = requests.post(url, data=data,headers=headers)
        # print(html.status_code)
        return html.text

    def method_main(self, url,method,data=None,headers=None):
        respose = None
        if method == 'GET':
           respose = self.GET(url, data)
        else:
            respose = self.POST(url, data,headers)
        return respose


if __name__ == '__main__':
    run = RunMain()# 实例化
    url = 'http://www.imooc.com'
    data = {
        "cart":"11"
    }

    respose=run.method_main(url, 'GET', data)
    # print (json.dumps(respose, indent=2, sort_keys=True))
 
    # print (type(respose))

    print (respose)