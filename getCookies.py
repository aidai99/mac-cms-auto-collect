import requests
import re
import os
import time
from public import Public
import userinfo
from userinfo import UserInfo
headers = Public.headers



class GetCookies(UserInfo):
    def __init__(self):
        super(GetCookies, self).__init__()
        self.logInUrl = self.baseUrl + '/admin/index.php?m=admin-check'
        self.sess = requests.Session()
        self.sess.post(self.logInUrl, data=self.data, headers=headers)        
        
      
    

    def checkLogin(self):
        print("首次检测是否可以登录, 稍后..")
        url = self.baseUrl + '/admin/index.php?m=admin-index'
        html = self.sess.get(url, headers=headers).text
        # print(html)
        linkpatt = re.compile("link")
        link = linkpatt.findall(html)
        link[0]
        return
        
    

if __name__ == '__main__':
    obj1 = GetCookies()
    # print(obj1.baseUrl)
    
