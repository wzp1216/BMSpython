# -*- coding: utf-8 -*-
# BMS tabU_widget   show the voltage of battery;
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import *

class tab_tmp(QWidget):
    def __init__(self):
        super().__init__()
        labeltest=QLabel(self)
        labeltest.setText("this is tab_tmp  widget")
        layout=QGridLayout()
        layout.addWidget(labeltest)       

