# 一个图上绘制两条曲线

import sys
import random
import numpy as np
import array
import random
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer

class main(QWidget):
    def __init__(self):
        super(main, self).__init__()
        self.draw1()
        self.initui()
    def draw1(self):
        self.plt1=pg.PlotWidget()
        x=np.linspace(0,10,1000)
        y1=3.5+0.1*np.sin(x)
        y2=3.7+0.1*np.cos(x)
        self.plt1.plot(x,y1,pen='r')
        self.plt1.plot(x,y2,pen='g')
        self.plt1.setRange(xRange=[0,10],yRange=[0,5],padding=0)

    def initui(self):
        self.resize(1200, 1000)
        label1=QLabel("test the pyqtgraph")
        layout=QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(self.plt1)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win= main()
    win.show()
    sys.exit(app.exec_())
