#coding=utf-8
#作者：曾祥卫
#时间：2018.06.08
#描述：cloud监控面板-网络列表的业务层


from networklist_control import NetworkListControl
from connect.ssh import SSH
from data import data
import time, subprocess

data_basic = data.data_basic()
data_ap = data.data_AP()

class NetworkListBusiness(NetworkListControl):

    def __init__(self, s):
        #继承NetworkListControl类的属性和方法
        NetworkListControl.__init__(self, s)

