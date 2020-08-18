# -*- coding: utf-8 -*-
# BMS  dlg_draw  show the voltage of battery;
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class myFigure(FigureCanvas):
    def __init__(self,width=5,height=4,dpi=100):
        self.fig=Figure(figsize=(width,height),dpi=dpi)
        super(myFigure,self).__init__(self.fig)
        self.axes=self.fig.add_subplot()
    def plotsin(self):
        t=np.arange(0,5,0.01)
        s=2+np.sin(2*t+5)
        self.axes.plot(t,s)

class dlg_draw(QWidget):
    def __init__(self,parent=None):
        super(dlg_draw,self).__init__(parent)
        self.draw()

    def draw(self):
        self.f=myFigure(width=3,height=2,dpi=100)
        self.f.plotsin()
        self.gridlayout=QGridLayout(self)
        self.gridlayout.addWidget(self.f,0,0,9,8)
        self.check_b1=QCheckBox("通道1")
        self.check_b2=QCheckBox("通道2")
        self.check_b3=QCheckBox("通道3")
        self.check_b4=QCheckBox("通道4")
        self.check_b5=QCheckBox("通道5")
        self.check_b6=QCheckBox("通道6")
        self.check_b7=QCheckBox("通道7")
        self.check_b8=QCheckBox("通道8")
        self.gridlayout.addWidget(self.check_b1,0,10)
        self.gridlayout.addWidget(self.check_b2,1,10)
        self.gridlayout.addWidget(self.check_b3,2,10)
        self.gridlayout.addWidget(self.check_b4,3,10)
        self.gridlayout.addWidget(self.check_b5,4,10)
        self.gridlayout.addWidget(self.check_b6,5,10)
        self.gridlayout.addWidget(self.check_b7,6,10)
        self.gridlayout.addWidget(self.check_b8,7,10)

    
