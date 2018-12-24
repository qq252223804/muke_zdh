import json
# fp=open("../dataconfig/data.json")
# data=json.load(fp)
# print(data["elme"])

class Operationjson:
    def __init__(self):
        self.data=self.read_data()    #初始化 赋予对象 方法
    def read_data(self): #获取json文件
        with open ('../dataconfig/data.json') as fp: #不用设置句柄，不用关闭文件
            data =json.load(fp)   #加载文件
            return data

    #根据关键字获取数据
    def get_data(self,id):
        return self.data[id]
if __name__=='__main__':
    a= Operationjson()
    print(a.get_data("muke_login"))

        
    


