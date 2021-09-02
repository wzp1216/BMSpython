# -*- coding: utf-8 -*-
from pyqtgraph.Qt import QtGui,QtCore
import numpy as np
import pyqtgraph as pg

app=pg.mkQApp("test2-sample")
win=pg.GraphicsLayoutWidget(show=True,title='plot example')
win.resize(800,100)
win.setWindowTitle('pyqt plot')

pg.setConfigOptions(antialias=True)

p6=win.addPlot(title="update plot")
curve=p6.plot(pen='y')
data=np.random.normal(size=(10,1000))
ptr=0
def update():
    global curve,data,ptr,p6
    curve.setData(data[ptr%10])
    if ptr==0:
        p6.enableAutoRange('xy',False)
    ptr+=1
timer=QtCore.QTimer()
timer.timeout.connect(update)
timer.start(100)

if __name__=='__main__':
    pg.exec()

