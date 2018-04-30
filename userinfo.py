# 基本信息
import os
import pickle
import base64
import userinfo
from config import Urls
from checkUpdate import MyVersion
baseDir = os.path.abspath(os.path.dirname(__file__))
# print(baseDir)
countFile = "co.txt"
filePath = os.path.join(baseDir, countFile)

class UserInfo:
    def __init__(self):    
        self.data, self.baseUrl = self.readFile()        
        self.logInUrl = self.baseUrl + '/admin/index.php?m=admin-check' 
        self.version = Urls().version




    @property
    def softwarestatus(self):
        return MyVersion(self.version)()             
    
    # 输入并存储数据
    def inputUserInfo(self):
        username = input("输入登录名:>>").strip()
        pasword = input("输入密码:>>").strip()
        check = input("校验码:>>").strip()
        url = input("网址:>>").strip().strip("/")
        if not(url.startswith("http://") or url.startswith("https://")):
            url = "http://" + url
        info = {
            'm_check': check,
            'm_name':	username,
            'm_password':	pasword,
        }
        encodeInfo = {
            base64.b32encode('你好,可能你已经破解了, 苟利国家生死以, 岂因祸福避趋之, 强行面向对象, 写着好烦呀, 有没有工作求介绍啊, 联系方式是jflasdkjflkfajsl冬季风蓝思风铃这里写着玩的,写着写着写乱了卧槽, 好烦呀 哈哈哈哈昂昂昂昂昂, 第一行就随便写, 反正有不会读.'.encode('utf8')):111,
            base64.b32encode('m_check'.encode("utf8")): base64.b32encode(check.encode("utf8")),
            base64.b32encode('m_name'.encode("utf8")):	base64.b32encode(username.encode("utf8")),
            base64.b32encode('m_password'.encode("utf8")):	base64.b32encode(pasword.encode("utf8")), 
            base64.b32encode('url'.encode("utf8")):	base64.b32encode(url.encode("utf8"))
        }
        with open(filePath, "wb") as wf:
            pickle.dump(encodeInfo, wf)


    # 读取数据
    def readFile(self):   
        if not os.path.exists(filePath):
            print("未检测到登陆文件, 请登录, 登录后将加密保存至", userinfo.filePath)
            self.inputUserInfo()
        with open(filePath, 'rb') as rf:
            encodeInfo = pickle.load(rf)
        info = {
            'm_check': base64.b32decode(encodeInfo[base64.b32encode('m_check'.encode("utf8"))]).decode('utf8'),
            'm_name':	base64.b32decode(encodeInfo[base64.b32encode('m_name'.encode("utf8"))]).decode('utf8'),
            'm_password':base64.b32decode(encodeInfo[base64.b32encode('m_password'.encode("utf8"))]).decode('utf8'),
        }
        url = base64.b32decode(encodeInfo[base64.b32encode('url'.encode("utf8"))]).decode('utf8')
        infos = (info, url)
        return infos

    

if __name__ == '__main__':
    pass
    
        

        
        

    