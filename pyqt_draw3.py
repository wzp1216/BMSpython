import sys
import random
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer

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
        self.x=np.arange(0,10,0.01,None)
        self.y=np.random.normal(size=1000)
        self.curve=self.plt2.plot(pen='y')

    def update(self):
        pass





    def initui(self):
        self.resize(1200, 1000)
        label1=QLabel("test the pyqtgraph")
        layout=QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(self.plt1)
        layout.addWidget(self.plt2)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win= main()
    win.show()
    sys.exit(app.exec_())