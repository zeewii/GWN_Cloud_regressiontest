#coding=utf-8
#作者：曾祥卫
#时间：2018.03.19
#描述：captive portal SSIDs的业务层


from captiveportal_control import CPControl
from connect.ssh import SSH
from data import data
import time

data_basic = data.data_basic()

class CPBusiness(CPControl):

    def __init__(self, s):
        #继承CPControl类的属性和方法
        CPControl.__init__(self, s)

