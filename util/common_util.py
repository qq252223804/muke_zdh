# import UserString
class CommonUtil:
    def is_contain(self,str_one,str_two):
        '''
         判断一个字符串是否再另外一个字符串中
        :param str_one: 查找的字符串
        :param str_two:被查证的字符串
        :return:
        '''
        flag=None
        # if isinstance(str_one,str):  #判断str_one 是否为str
        #     str_one=str_one.encode('unicode-escape')
        if str_one in str_two:
            flag=True
        else:
            flag=False
        return flag