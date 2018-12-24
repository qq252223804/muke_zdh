#coding:utf-8
import unittest
import json,requests
from base.demo import RunMain
from mock import mock
from base.mock_demo import  mock_test


class TestMethod(unittest.TestCase):
    # @classmethod    #类方法 每次只执行一次
    # def setUpClass(self):
 
    #     print('test-setup')
    #     print('类执行之前的方法')
    # @classmethod
    # def tearDownClass(cls):
    #     print('类执行之后的方法')
     #每次方法之前执行
    
    def setUp(self):      #实例化方法
        RunMain()    # 类的实例化 后面用例不用一一执行了
        print('test-setup')

    def tearDown(self):
        pass

    # print('test-teardown')
    # def __int__(self):
    #     self.run = RunMain()
    #     print('test-setup')


    def test_01(self):

        url = 'http://openapi.ele.me/v2/restaurants'
        data = {"consumer_key":"7284397484","sig":"e76dfee7276f0c7a382b4f0dbdad802a95c642aa","timestamp":"1374908054"}
        # print(type(data))
        respose =RunMain().method_main(url, 'GET',data)
        print(type(respose))
        res=json.loads(respose)
        # print (json.loads(respose))
      
        self.assertEqual(res["code"], 1003,'测试失败')
    def test_02(self):
        url = "https://fanyi.baidu.com/v2transapi"
        data = {
            'from': 'en',
            'to': 'zh',
            'query': 'study',
            'transtype': 'translang',
            'simple_means_flag': '3',
            'sign': '704127.941390',
            'token': '97bfaa70c157bf1166391185ee7a29ec'
        }

        headers =  {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "Cookie":"BIDUPSID=ABF6830AB773673A244EF20622AF5FE4; PSTM=1531370396; BAIDUID=0E8BBB9E5383F7BCBC5FF7C7F9D8B8A5:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=RRWUxDOWxlN2txcEJZZENBNjJtWlVrT210TTBPd0VJZmFxVUZtNktnNXdnLWRiQVFBQUFBJCQAAAAAAAAAAAEAAAAHEheR1dTmw9y9AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHD2v1tw9r9bdG; H_PS_PSSID=1444_21110_26350_27509; MCITY=-%3A; delPer=0; PSINO=5; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=baidu; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1542096145,1542096802; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1542096802",
            "X-Requested-With":"XMLHttpRequest",
            "Content - Type":"application/x-www-form-urlencoded;charset =UTF-8"
        }

        # print(type(data))
        # print(type(headers))
        response =RunMain().method_main(url,'POST',data,headers=headers)
        # print(response)
        res=json.loads(response)
        self.assertEqual(res['liju_result']['tag'],['学习', '研究', '课题', '书房', '结论', '考虑', '沉思', '努力', '想出'], '测试失败')

        print(json.dumps(res, indent=2, sort_keys=True))
    def test_03(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1530065252258',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0'

        }
        response=RunMain().method_main(url,'POST',data)
        res = json.loads(response)
        self.assertEqual(res["errorCode"], 1007, '测试失败')
        # print(json.dumps(res, sort_keys=True))
    def test_04(self):    #模拟接口测试
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode':1003
        }
        '''1'''
        # mock_data=mock.Mock(return_value=data)  #面向对象-对象
        # self.run.method_main=mock_data    #  模拟返回数据 返回上面的data 数据 新增了errCOde
        '''2'''
        # self.run.method_main=mock.Mock(return_value=data)  # 实例化 run.method_main这样mock数据就等于response
        # respose = self.run.method_main(url, 'POST', data)
        '''3'''
        response=mock_test('POST',url,'POST',data,data)  #mock 的封装使用
        # res = json.loads(response)
        self.assertEqual(response["errorCode"], 1003, '测试失败')
        # print(json.dumps(response, indent=2, sort_keys=True))
if __name__ == '__main__':
    unittest.main()









# import requests
#
# url = "http://fanyi.baidu.com/v2transapi"
# data = {
#     'from':'en',
#     'to':'zh',
#     'query':'study',
#     'simple_means_flag':'3',
#     'sign':'704127.941390',
#     'token':'038c2e358377b35d477519e4a67cdf93'
#     }
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Ch",
#     "Cookie":"BDUSS=FnUW1BbUhKVFNYV0hFbDVUVHJLZmNLU2t-a1ZreDhTcTJycldLNW1CLTVKMWRaSVFBQUFBJCQAAAAAAAAAAAEAAAAjs3g6wtK3x8S"
#              "rAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALmaL1m5mi9Zdk; "
#              "BAIDUID=189B749BBC323202E937833632299713:FG=1; BIDUPSID=189B749BBC323202E937833632299713; PSTM=1514427528; "
#              "locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1522393132; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; "
#              "HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C"
#              "%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; "
#              "to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%2"
#              "2%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1522393853"
# }
#
# reps = requests.post(url=url,data=data,headers=headers)
# print(reps.json())