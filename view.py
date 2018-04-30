from getApiUrl import GetApiUrl
from userinfo import UserInfo

# 主页快捷菜单里的api
def IndexList():
    apiUrl = GetApiUrl()
    nameAndApi = apiUrl.adminIndexApi
    inpnum = chooseApi(nameAndApi, IndexList)
    print(inpnum)
    choose = nameAndApi[inpnum][1]
    # print(choose)
    # 返回被选择的api连接
    return choose

# 采集页面默认存在的api
def collectPageDefault():
    apiUrl = GetApiUrl()
    nameAndApi = apiUrl.DaultApi
    inpnum = chooseApi(nameAndApi, collectPageDefault)
    print(inpnum)
    choose = nameAndApi[inpnum][1]
    print(choose)
    # 返回被选择的api连接
    return choose

def collectPageUser():
    apiUrl = GetApiUrl()
    nameAndApi = apiUrl.adminCollectPageApi
    inpnum = chooseApi(nameAndApi, collectPageUser)
    print(inpnum)
    choose = nameAndApi[inpnum][1]
    print(choose)
    # 返回被选择的api连接
    return choose

# 通用函数:
def chooseApi(nameApi, func):
    for index, (name, api) in enumerate(nameApi):
        print("%s: %s" % (index, name))    
    inp = input("输入采集api: ")
    try:
        inpnum = int(inp)
    except:
        print('非数字, 重新..')
        func()
        return
    if inpnum<0 or inpnum>len(nameApi) or len(inp)==0:
        print("错误超出范围>...")
        func()
        return 
    return inpnum


def startprint():
    print("*"*10)
    print("请选择采集的列表: ")
    print("0. 快捷菜单")
    print("1. 苹果cms默认列表(官方默认列表, 如果没有请忽略)")
    print("2. 采集页面的采集节点")
    print('3. 清除用户数据')
    try:
        inp = int(input("输入编号: "))
    except:
        print("错误")
        return startprint()

    return inp



def startChooseTime():
    print("*"*10)
    print("请选择采集的列表: ")
    print("0. 当日")
    print("1. 全部")
    try:
        inp = int(input("输入采集时段:"))
    except:
        print("错误", startChooseTime())
    if inp<0 or inp>1:
        startChooseTime()
    return inp



if __name__ == '__main__':    
    pass

    