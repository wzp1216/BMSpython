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
        self.draw2()
        self.initui()

    def draw2(self):
        self.plt2=pg.PlotWidget()
        self.tim1=QTimer()
        self.tim1.timeout.connect(self.update)
        self.tim1.start(100)

        self.x=500
        self.plt2.setRange(xRange=[0,self.x],yRange=[0,5],padding=0)
        self.dat=array.array('d')
        self.dat2=array.array('d')
        self.curve=self.plt2.plot(pen='y')
        self.curve2=self.plt2.plot(pen='r')


    def update(self):
        global idx
        global rand
        if idx<rand:
            tmp1=3.8
            tmp2=3.6
        else:
            idx=0
            rand=random.randint(50,300)
            tmp1=3.9
            tmp2=3.5
        if len(self.dat)<self.x:
            self.dat.append(tmp1)
            self.dat2.append(tmp2)
        else:
            self.dat[:-1]=self.dat[1:]
            self.dat[-1]=tmp1
            self.dat2[:-1] = self.dat2[1:]
            self.dat2[-1] = tmp2
        self.curve.setData(self.dat)
        self.curve2.setData(self.dat2)
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
