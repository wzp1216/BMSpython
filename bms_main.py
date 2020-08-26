# -*- coding: utf-8 -*-
#BMS_main.py
import sys
from PyQt5.QtWidgets import QApplication
from bms_mainwin import bms_mainwindow

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainwin=bms_mainwindow()
    mainwin.show()
    sys.exit(app.exec_())
#end
