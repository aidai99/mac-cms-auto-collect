import requests
import re
import lxml.html
from getCookies import GetCookies
from public import Public
headers = Public.headers

class GetApiUrl(GetCookies):
    
    def __init__(self):
        super(GetApiUrl, self).__init__()
        

    # 用户自定义的api
    @property
    def adminCollectPageApi(self):
        collectPageUrl = self.baseUrl + '/admin/index.php?m=collect-union'
        collectPageHtml = self.sess.get(collectPageUrl, headers=headers).text
        patt = re.compile('(\?m=collect-list.*?)\".*?>(.*?)<')
        apiAndName = patt.findall(collectPageHtml)
        nameAndApi = []
        for i in apiAndName:
            if "绑定" in i[1]:
                continue
            nameAndApi.append((i[1], i[0]))
        # print(nameAndApi)
        # [('色色在线采集', 'url...'), (...]
        return nameAndApi

    # 主页快捷菜单里的的api
    @property
    def adminIndexApi(self):
        adminIndexUrl = self.baseUrl + '/admin/index.php?m=admin-index'
        # print(adminIndexUrl)
        adminIndexHtml = self.sess.get(adminIndexUrl, headers=headers)
        patt = re.compile('{.*?"text":"(.*?)","url":"(.*?)".*?};')
        fastList = patt.findall(adminIndexHtml.text)
        def killsys(li):
            return 'api' in li[1]
        # 过滤掉系统快捷菜单, 仅保留api
        indexApi = filter(killsys, fastList)
        listIndexApi = list(indexApi)
        # print(listIndexApi)        
        # [(name,api)...]
        return listIndexApi


    
    # 默认存在的api
    @property
    def DaultApi(self):
        url = 'http://www.maccms.com/union/xmlutf_2014.js'
        js =self.sess.get(url, headers=headers).text        
        namePatt = re.compile("\'name\':(.*?)\n")
        urlPatt = re.compile("\'apiurl\':(.*?)\n")
        flagPatt = re.compile("\'flag\':(.*?)\n")
        names = namePatt.findall(js)
        flags = flagPatt.findall(js)
        urls = urlPatt.findall(js)
        deaultApi = []
        for index, name in enumerate(names):
            name = name.replace("'", "").replace("\r", "").replace(",", "")
            flag = flags[index].replace("'", "").replace("\r", "").replace(",", "")
            url = urls[index].replace("'", "").replace("\r", "").replace(",", "")
            apiString = '?m=collect-list-xt-1-ct--group--flag-' + flag + '-apiurl-' + url
            api = (name, apiString)
            deaultApi.append(api)
            # ?m=collect-list-xt-1-ct--group--flag-sszyz-apiurl-http://sscj8.com/inc/api.php?
        # 返回结果是[(name, api)...]        
        # print(deaultApi)
        return deaultApi


if __name__ == '__main__':
    obj = GetApiUrl()
    print(obj.DaultApi)
    