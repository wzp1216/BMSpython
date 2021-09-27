# -*- coding: utf-8 -*-
# BMS  dlg_draw  show the voltage of battery;
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import numpy as np
import matplotlib

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

b1 = 1
b2 = 1
b3 = 1
b4 = 1
b5 = 1
b6 = 1
b7 = 1
b8 = 1


class myFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(myFigure, self).__init__(self.fig)
        self.axes = self.fig.add_subplot()

    def plot_vol(self):
        global b1, b2
        x = np.arange(0, 10, 0.01)
        self.y1 = x
        self.y2 = 3.7 + 0.01 * np.cos(2 * x)
        self.axes.set_xlim([0, 10])
        self.axes.set_ylim([0, 5])

    def update_plot(self):
        self.axes.plot(self.x, self.y1)
        self.canvas.draw()


class dlg_draw(QWidget):
    def __init__(self, parent=None):
        super(dlg_draw, self).__init__(parent)
        self.draw()

    def draw(self):
        self.f = myFigure(width=3, height=2, dpi=100)
        self.f.plot_vol()
        self.f.update_plot()
        self.gridlayout = QGridLayout(self)
        self.gridlayout.addWidget(self.f, 0, 0, 10, 8)
        self.check_b1 = QCheckBox("通道1")
        self.check_b2 = QCheckBox("通道2")
        self.check_b3 = QCheckBox("通道3")
        self.check_b4 = QCheckBox("通道4")
        self.check_b5 = QCheckBox("通道5")
        self.check_b6 = QCheckBox("通道6")
        self.check_b7 = QCheckBox("通道7")
        self.check_b8 = QCheckBox("通道8")
        self.check_b9 = QCheckBox("通道9")
        self.check_b10 = QCheckBox("通道10")
        self.check_b11 = QCheckBox("通道11")
        self.check_b12 = QCheckBox("通道12")
        self.check_b13 = QCheckBox("通道13")
        self.check_b14 = QCheckBox("通道14")
        self.check_b15 = QCheckBox("通道15")
        self.check_b16 = QCheckBox("通道16")
        self.gridlayout.addWidget(self.check_b1, 0, 10)
        self.gridlayout.addWidget(self.check_b2, 1, 10)
        self.gridlayout.addWidget(self.check_b3, 2, 10)
        self.gridlayout.addWidget(self.check_b4, 3, 10)
        self.gridlayout.addWidget(self.check_b5, 4, 10)
        self.gridlayout.addWidget(self.check_b6, 5, 10)
        self.gridlayout.addWidget(self.check_b7, 6, 10)
        self.gridlayout.addWidget(self.check_b8, 7, 10)
        self.gridlayout.addWidget(self.check_b9, 0, 11)
        self.gridlayout.addWidget(self.check_b10, 1, 11)
        self.gridlayout.addWidget(self.check_b11, 2, 11)
        self.gridlayout.addWidget(self.check_b12, 3, 11)
        self.gridlayout.addWidget(self.check_b13, 4, 11)
        self.gridlayout.addWidget(self.check_b14, 5, 11)
        self.gridlayout.addWidget(self.check_b15, 6, 11)
        self.gridlayout.addWidget(self.check_b16, 7, 11)

        self.check_b1.stateChanged.connect(self.check_changed)
        self.check_b2.stateChanged.connect(self.check_changed)
        self.check_b3.stateChanged.connect(self.check_changed)
        self.check_b4.stateChanged.connect(self.check_changed)
        self.check_b5.stateChanged.connect(self.check_changed)
        self.check_b6.stateChanged.connect(self.check_changed)
        self.check_b7.stateChanged.connect(self.check_changed)
        self.check_b8.stateChanged.connect(self.check_changed)

    def check_changed(self):
        global b1, b2, b3, b4, b5, b6, b7, b8
        if True == self.check_b1.isChecked():
            b1 = 1
        else:
            b1 = 0
        if True == self.check_b2.isChecked():
            b2 = 1
        else:
            b2 = 0
        if True == self.check_b3.isChecked():
            b3 = 3
        else:
            b3 = 0
        if True == self.check_b4.isChecked():
            b4 = 4
        else:
            b4 = 0
        if True == self.check_b5.isChecked():
            b5 = 5
        else:
            b5 = 0
        if True == self.check_b6.isChecked():
            b6 = 6
        else:
            b6 = 0
        if True == self.check_b7.isChecked():
            b7 = 7
        else:
            b7 = 0
        if True == self.check_b8.isChecked():
            b8 = 8
        else:
            b8 = 0
        self.f.plot_vol()
        self.f.update_plot()
