#coding=utf-8
#作者：曾祥卫
#时间：2018.06.14
#描述：cloud监控面板-概览的业务层


from overview_control import OverViewControl
from connect.ssh import SSH
from data import data
import time, subprocess

data_basic = data.data_basic()
data_ap = data.data_AP()

class OverViewBusiness(OverViewControl):

    def __init__(self, s):
        #继承OverViewControl类的属性和方法
        OverViewControl.__init__(self, s)

    #判断bandwidth图表是否有流量
    def check_overview_bandwidth(self, time):
        #获取监控面板-概览-速率，获取上传下载的bandwidth
        r = 0
        t = 0
        rx_bd, tx_bd = self.get_overview_bandwidth(time)
        for rx in rx_bd:
            r = r + rx
        for rx in rx_bd:
            r = r + rx
        print r, t
        if (r+t) > 50000:
            return True
        else:
            return False

    #判断客户端是否在监控面板-概览-Top Clients中
    def check_overview_top_client(self, time, mac):
        #获取监控面板-概览-Top Clients，client的所有信息
        clients_info = self.get_overview_top_clients(time)
        Mac = mac.upper()
        for client_info in clients_info:
            if client_info['mac'] == Mac:
                return True
        return False