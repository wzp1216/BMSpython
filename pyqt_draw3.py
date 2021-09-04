import sys
import random
import numpy as np
import array
import random
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer

idx=0
rand=random.randint(50,300)
class main(QWidget):
    def __init__(self):
        super(main, self).__init__()
        self.draw1()
        self.draw2()
        self.initui()
    def draw1(self):
        self.plt1=pg.PlotWidget()
        x=np.random.normal(size=1000)
        y=np.random.normal(size=1000)
        self.plt1.plot(x,y,pen=None,symbol='o')

    def draw2(self):
        self.plt2=pg.PlotWidget()
        self.tim1=QTimer()
        self.tim1.timeout.connect(self.update)
        self.tim1.start(100)

        self.x=500
        self.plt2.setRange(xRange=[0,self.x],yRange=[0,5],padding=0)
        self.dat=array.array('d')
        self.curve=self.plt2.plot(pen='y')


    def update(self):
        global idx
        global rand
        if idx<rand:
            tmp1=3.8
        else:
            idx=0
            rand=random.randint(50,300)
            tmp1=3.9
        if len(self.dat)<self.x:
            self.dat.append(tmp1)
        else:
            self.dat[:-1]=self.dat[1:]
            self.dat[-1]=tmp1
        self.curve.setData(self.dat)
        idx+=1;


    def initui(self):
        self.resize(1200, 1000)
        label1=QLabel("test the pyqtgraph")
        layout=QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(self.plt2)
        layout.addWidget(self.plt2)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win= main()
    win.show()
    sys.exit(app.exec_())