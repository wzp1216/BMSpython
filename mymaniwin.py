# -*- coding: utf-8 -*-
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QFileDialog
from PyQt5.QtWidgets import QGridLayout
from mainui import Ui_MainWindow
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class myFigure(FigureCanvas):
    def __init__(self,width=5,height=4,dpi=100):
        self.fig=Figure(figsize=(width,height),dpi=dpi)
        super(myFigure,self).__init__(self.fig)
        self.axes=self.fig.add_subplot()
    def plotsin(self):
        t=np.arange(0,3,0.01)
        s=np.sin(t)
        self.axes.plot(t,s)


class mymainwin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mymainwin,self).__init__()
        self.setupUi(self)
        self.setUI()
        self.draw()
    def setUI(self):
        self.desktop=QApplication.desktop()
        self.maxheight=self.desktop.height()-100
        self.maxwidth=self.desktop.width()-100
        self.setFixedSize(self.maxwidth,self.maxheight)
        self.statusbar.show()
        self.statusbar.showMessage("Battery Managet Sysem is ready!")
        self.layoutWidget.setGeometry(QRect(40, 20, self.maxwidth-100,self.maxheight-200))
        self.tabWidget.resize(self.maxwidth-40,self.maxheight-60)
    def draw(self):
        self.F=myFigure(width=3,height=2,dpi=100)
        self.F.plotsin()
        self.gridLayout=QGridLayout(self.groupBox1)
        self.gridLayout.addWidget(self.F)


