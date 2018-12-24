import requests
import json






class RunMethod:
	def post_main(self,url,data,headers=None):
		res = None
		datas=eval(data)     #!!!!!!取出来的str-dict
		# print(type(datas))
		if headers !=None:
			res = requests.post(url=url,data=datas,headers=headers,encoding='utf-8')
		else:
			res = requests.post(url=url,data=datas)
		# print(data)
		# print(type(res.json()))
		return res.json()

	def get_main(self,url,data=None,headers=None):
		res = None
		# print(url)
		# print(data)
		# urls=url+'?'+data
		# print(ulrs)
		if headers !=None:
			res = requests.get(url=url,data=data,headers=headers,verify=False)
		else:
			res = requests.get(url=url,data=data,verify=False)
		# print(type(res.json()))
		return res

	def run_main(self,method,url,data=None,headers=None):
		res = None
		if method == 'POST':
			res = self.post_main(url,data,headers)
			return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
		else:
			res = self.get_main(url,data,headers)
			return  res.text

if __name__ == '__main__':
	run = RunMethod()  # 实例化
	# url = 'http://openapi.ele.me/v2/restaurants/'
	# data = 'consumer_key=7284397484&sig=e76dfee7276f0c7a382b4f0dbdad802a95c642aa&timestamp=1374908054'
	s = requests.session()
	url1="http://192.168.31.172:8082/cms/login"
	res=s.post(url1,{"username":18657738815,"password":111111})
	# print(json.loads(res.text))
	url="http://192.168.31.172:8082/cms/dealer/getDealerUserList/"
	datas={"page":"1","limit":"20","keyword":"","level":"","locked":"","cityCode":"","begin_date":"","end_date":""}
	print(type(datas))
	respose = s.get(url=url,params=datas)
	print(json.loads(respose.text))
	# print(type(respose))

# url = 'http://coding.imooc.com/api/cate'
# a=GetData()
# data1=a.get_request_data(4)
# # print(data1)
# # print(type(data1))
# c = RunMethod()
# respose =c.post_main(url, data1)
# print(respose)