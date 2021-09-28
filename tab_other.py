# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import *

class tab_data(QWidget):
    def __init__(self):
        super(tab_data, self).__init__()
        self.setui()
    def setui(self):
        label1=QLabel("电池数据信息")
        bdata=QTableWidget()
        bdata.setRowCount(10)
        bdata.setColumnCount(6)
        bdata.setHorizontalHeaderLabels(['序号','电池编号','采样日期','采样时间','工作电压','工作温度'])
        for i in range(6):
            bdata.setColumnWidth(i,200)
        lay=QVBoxLayout()
        lay.addWidget(label1)
        lay.addWidget(bdata)
        self.setLayout(lay)
class tab_alter(QWidget):
    def __init__(self):
        super(tab_alter, self).__init__()
        self.setui()
    def setui(self):
        label1=QLabel("电池报警信息")
        alter=QTableWidget()
        alter.setRowCount(10)
        alter.setColumnCount(7)
        alter.setHorizontalHeaderLabels(['序号','电池编号','报警日期','报警时间','报警信息','工作电压','工作温度'])
        for i in range(7):
            alter.setColumnWidth(i,180)
        lay=QVBoxLayout()
        lay.addWidget(label1)
        lay.addWidget(alter)
        self.setLayout(lay)

class tab_battery(QWidget):
    def __init__(self):
        super(tab_battery, self).__init__()
        self.setui()
    def setui(self):
        label1=QLabel("电池模组信息")
        battery=QTableWidget()
        battery.setRowCount(10)
        battery.setColumnCount(5)
        battery.setHorizontalHeaderLabels(['序号','电池编号','启用时间','工作状态','是否报警'])
        for i in range(5):
           battery.setColumnWidth(i,240)
        lay=QVBoxLayout()
        lay.addWidget(label1)
        lay.addWidget(battery)
        self.setLayout(lay)
class tab_user(QWidget):
    def __init__(self):
        super(tab_user, self).__init__()
        self.setui()
    def setui(self):
        label1=QLabel("系统用户管理")
        user=QTableWidget()
        user.setRowCount(10)
        user.setColumnCount(5)
        user.setHorizontalHeaderLabels(['序号','用户名','登陆密码','用户分组','是否启用'])
        for i in range(5):
            user.setColumnWidth(i,240)
        lay=QVBoxLayout()
        lay.addWidget(label1)
        lay.addWidget(user)
        self.setLayout(lay)

'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = tab_data()
    demo.show()
    sys.exit(app.exec_())
'''