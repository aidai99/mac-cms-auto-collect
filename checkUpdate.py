# 检测更新
import requests
import time 
import webbrowser
import tkinter as tk
import config
from public import Public
linkUrl = config.Urls()
headers = Public.headers
# 保存下载地址的地址:
url = linkUrl.downUrl

class MyVersion(object):   

    def __init__(self, curversion):
        # 当前版本
        self.__curVersion = curversion
        self.newVersion = self.getNewVersion       

    def __call__(self):
        return self.check()

    # 最终弹窗控制
    def check(self):
        if self.newVersion == self.__curVersion:
            return -1
        else:
            self.guiForUpdate()
            print("需要更新")
            # 更新
            return 1

    # 获取最新
    @property
    def getNewVersion(self):
        versionsUrl = linkUrl.checkUrl
        response = requests.get(versionsUrl)
        newVersion = response.content.decode("utf-8")
        # 获得新版本的一个字符串
        return newVersion

    # 打开更新窗口
    def guiForUpdate(self):
        win = tk.Tk()
        win.title("Maybe you should update!")
        win.geometry("200x200")

        # 打开网址:
        def update():          
            # print(downurl.text)
            webbrowser.open_new(downurl.text)

        lab = tk.Label(win, text="最新版本号为 %s\n %s" % (self.newVersion, self.improvement), width="100", height=7)
        lab.pack()
        # 下载地址
        downurl = requests.get(url)
     
        tk.Button(win, text="确定", command=update).place(x=80, y=120)
        win.mainloop() 

    # 文字: 比如: "做出以下改进"
    @property
    def improvement(self):
        url = linkUrl.checkUrl
        response = requests.get(url)
        return response.content.decode('utf-8')
   
    def countTiem(self):
        time.sleep(2)
        return -1
   
