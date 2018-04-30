import requests
import re
import time
import view
from public import Public
from getCookies import GetCookies
from getApiUrl import GetApiUrl
# from main import run
headers = Public.headers


class StartCollect(GetApiUrl):
    def __init__(self):
        super(StartCollect, self).__init__()
        self.pb = Public()
    # 获得当日
    def getOneDay(self, api):    
        flag, apiurl = self.pb.getFlagAndUrl(api)
        firstUrl = self.baseUrl + '/admin/index.php?m=collect-cj-ac2-day-xt-1-ct--group--flag-' + \
        flag +"-hour-24-apiurl-" + apiurl
        response = self.sess.get(firstUrl, headers=headers)
        html = response.text
        pagesCount = self.pb.checkPageCount(html)
        self.pb.printLog(html)
        print(pagesCount)
        for page in range(2, pagesCount+1):
            afterPages = self.baseUrl +'/admin/index.php?m=collect-cj-ac2-day-pg-' + str(page) + \
            '-type-0-hour-24-xt-1-ct--group--flag-' + flag + '-apiurl-' + apiurl
            response = self.sess.get(afterPages, headers=headers)
            html = response.text
            self.pb.printLog(html)
        print('采集完毕')
        return view.startprint()


    # 获取全部:
    def getAll(self, api):
        flag, apiurl = self.pb.getFlagAndUrl(api)
        firstUrl = self.baseUrl + '/admin/index.php?m=collect-cj-ac2-all-xt-1-ct--group--flag-' +\
        flag + '-apiurl-' + apiurl
        response = self.sess.get(firstUrl, headers=headers)
        html = response.text
        pagesCount = self.pb.checkPageCount(html)
        self.pb.printLog(html)
        for page in range(2, pagesCount+1):
            afterPages = self.baseUrl +'/admin/index.php?m=collect-cj-ac2-all-pg-' + str(page) + \
            '-type-0-hour-0-xt-1-ct--group--flag-' + flag + '-apiurl-' + apiurl
            response = self.sess.get(afterPages, headers=headers)
            html = response.text
            self.pb.printLog(html)
        print("采集完毕")
        return view.startprint()


if __name__ == '__main__':
    obj = StartCollect()
    obj.getOneDay('?m=collect-list-ac2--hour--xt-1-ct--group--flag-zy131com-apiurl-http://cj.zy131.com/inc/api.php')

    