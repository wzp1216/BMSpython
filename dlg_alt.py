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

class dlg_alt(QWidget):
    def __init__(self,parent=None):
        super(alg_alt, self).__init__()
        self.init()

    def init(self):
        self.gridlayout = QGridLayout(self)
        self.setLayout(self.gridlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win= dlg_alt()
    win.show()
    sys.exit(app.exec_())
