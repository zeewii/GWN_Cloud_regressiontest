#coding=utf-8
#作者：曾祥卫
#时间：2018.06.11
#描述：cloud监控面板-ap列表的业务层


from allaplist_control import AllApListControl
from connect.ssh import SSH
from data import data
import time, subprocess

data_basic = data.data_basic()
data_ap = data.data_AP()

class AllApListBusiness(AllApListControl):

    def __init__(self, s):
        #继承AllApListControl类的属性和方法
        AllApListControl.__init__(self, s)

