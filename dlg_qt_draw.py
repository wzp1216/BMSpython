# -*- coding: utf-8 -*-
# BMS  dlg_draw  show the voltage of battery;

import sys
import random
import numpy as np
import array
import random
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout,QGridLayout,QCheckBox,QLineEdit
from PyQt5.QtWidgets import QLayout
from PyQt5.QtCore import QTimer

idx=0
rand1=random.randint(0,800)
rand2=random.randint(0,100)
vol=[3.5, 3.8, 3.6, 3.7,3.9,3.6,3.8,3.5]
checked=[True,True,True,True,True,True,True,True]
class dlg_qt_draw(QWidget):
    def __init__(self):
        super(dlg_qt_draw, self).__init__()
        self.draw2()
        self.initui()

    def draw2(self):
        self.plt2=pg.PlotWidget()
        self.tim1=QTimer()
        self.tim1.timeout.connect(self.update)
        self.tim1.start(100)

        self.x=500
        self.plt2.setRange(xRange=[0,self.x],yRange=[0,5],padding=0)
        self.dat0=array.array('d')
        self.dat1=array.array('d')
        self.curve0=self.plt2.plot(pen='y')
        self.curve1=self.plt2.plot(pen='r')


    def update(self):
        global idx
        global rand1,rand2
        global vol
        if rand1%10==0:
            tmp=rand1%8
            if rand2>50:      vol[tmp]=vol[tmp]+0.01
            if rand2<5:      vol[tmp]=vol[tmp]-0.01
            if vol[tmp]>4.1:  vol[tmp]=4.1
            if vol[tmp]<3.4:  vol[tmp]=3.4
        rand1 = random.randint(0, 1800)
        rand2 = random.randint(0, 100)

        if len(self.dat0)<self.x:
            self.dat0.append(vol[0])
        else:
            self.dat0[:-1]=self.dat0[1:]
            self.dat0[-1]=vol[0]
        self.curve0.setData(self.dat0)
        idx+=1;


    def initui(self):
        self.gridlayout = QGridLayout(self)
        self.gridlayout.addWidget(self.plt2, 0, 0, 9, 8)
        self.checkb = [QCheckBox("通道1"),QCheckBox("通道2"),QCheckBox("通道3"), QCheckBox("通道4"),QCheckBox("通道5"), QCheckBox("通道6"), QCheckBox("通道7"), QCheckBox("通道8")]
        for i in range(8):
            self.gridlayout.addWidget(self.checkb[i], i,10)
            self.checkb[i].stateChanged.connect(self.check_change)
        self.setLayout(self.gridlayout)

    def check_change(self):
        global checked
        for i in range(8):
            checked[i]=self.checkb[i].isChecked()
            print(i,checked[i])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win= dlg_qt_draw()
    win.show()
    sys.exit(app.exec_())
