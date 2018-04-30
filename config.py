# 链接
class Urls(object):    
    def __init__(self):        
        self.mainUrl = "http://tgtpusgbyswb.wktadmin.com"
        # 新版本下载网址
        self.downUrl = "%s/newversionforcmsdown.txt" % self.mainUrl
        # 打开软件会访问此页面, 用于计算使用情况
        self.requestUrl = "http://www.wktadmin.com"
        # 本版本号
        self.version = "1.35"
        # 最新图片下载地址
        # self.imgUrl = '%s/img.txt' % self.mainUrl
        # 广告链接
        # self.adsUrl = '%s/ads.txt' % self.mainUrl
        # 新版验证
        self.checkUrl = "%s/newversionforcms.txt" % self.mainUrl
        # print(self.checkUrl)        
        # 最新版本详情        
        self.improvement = "%s/newversionforcmsinfo.txt" % self.mainUrl


