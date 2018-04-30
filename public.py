import re
import time

class Public:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
    def __init__(self):
        pass

    # 传入api获得flag和url
    def getFlagAndUrl(self, api):
        if type(api) == dict:
            return api['flag'], api['url']
        patt = re.compile('-flag-(.*?)-')
        pattapi = re.compile('(http.*?)$')
        flag = patt.findall(api)[0]
        apiurl = pattapi.findall(api)[0]
        return flag, apiurl

    # 用于检测页数
    def checkPageCount(self, html):
        patternNum = re.compile('<span class="green">(.*?)</span>')
        nums = int(patternNum.findall(html)[0])
        print("共%s页数据, 一秒后开始采集.." % nums)
        time.sleep(1)
        return nums

    # 打印采集日志
    def printLog(self, html):
        movlistPattern = r'div>(\d.*?)</div>'
        movList = re.findall(movlistPattern, html)
        for mov in movList:
            single = re.sub("<.*?>", "", mov).replace("\n","")
            print(single)



