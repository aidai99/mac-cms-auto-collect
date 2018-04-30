import requests
from public import Public
from userinfo import UserInfo
headers = Public.headers
class GetCookies(UserInfo):
    def __init__(self):
        super(GetCookies, self).__init__()
        self.logInUrl = self.baseUrl + '/admin/index.php?m=admin-check'
        self.sess = requests.Session()
        self.sess.post(self.logInUrl, data=self.data, headers=headers)
    

if __name__ == '__main__':
    obj1 = GetCookies()
    print(obj1.baseUrl)
    