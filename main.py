import threading
import userinfo
from userinfo import UserInfo
from colects import StartCollect
from getCookies import GetCookies
from view import *
import time
import os
softwarestatus = -1
usi = UserInfo()
    
def checkVersion():
    global softwarestatus
    softwarestatus = UserInfo().softwarestatus    
    if softwarestatus == 1:
        print("需要更新")

def run():
    if os.path.exists(userinfo.filePath):
        print("检测到登陆文件")
        # 检测登录是否出错:
        try:
            GetCookies().checkLogin()
        except:
            print('配置出错,  已经为你重置')
            os.remove(userinfo.filePath)
            return run()
        startnum = startprint()
        if startnum == 0 and softwarestatus == -1:
            choose = IndexList()
        elif startnum == 1 and softwarestatus == -1:
            choose = collectPageDefault() 
        elif startnum == 2 and softwarestatus == -1:
            choose = collectPageUser()
        elif startnum == 3 and softwarestatus == -1:
            os.remove(userinfo.filePath)
            print("已经删除, ", userinfo.filePath)
            return run()
        else:
            startprint()

        chooseTime = startChooseTime()
        clt = StartCollect()
        if chooseTime == 0 and softwarestatus == -1:
            clt.getOneDay(choose)
        if chooseTime == 1 and softwarestatus == -1:
            clt.getAll(choose)
    else:       
        usi.readFile()
        return run()

        


    

if __name__ == '__main__':    
    run_thread = threading.Thread(target=run)
    check_thread = threading.Thread(target=checkVersion)
    run_thread.start()
    time.sleep(10)
    check_thread.start()
