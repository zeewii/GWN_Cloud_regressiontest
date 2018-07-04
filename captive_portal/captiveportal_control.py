#coding=utf-8
#作者：曾祥卫
#时间：2018.03.19
#描述：captive portal SSIDs的控制层


import time, subprocess
from data import data
from publicControl.public_control import PublicControl



class CPControl(PublicControl):

    def __init__(self, s):
        #继承PublicControl类的属性和方法
        PublicControl.__init__(self, s)

    #cloud增加portalpolicy
    def add_portalpolicy(self):
        pass

    #cloud删除portalpolicy
    def delete_portalpolicy(self):
        pass

    #cloud编辑portalpolicy
    def edit_portalpolicy(self):
        pass

