# -*- coding: utf-8 -*-
import sys
from  PyQt5.QtWidgets import QApplication, QPushButton,QWidget,QMainWindow
from  PyQt5.QtWidgets import QLabel,QLineEdit,QTextEdit
from  PyQt5.QtWidgets import QVBoxLayout,QFormLayout
from  PyQt5.QtCore import Qt,QDir

class login(QWidget):
    def __init__(self):
        super(login,self).__init__()
        self.setWindowTitle("用户登录")
        self.init()
    def init(self):
        self.lineedit1=QLineEdit("a")
        self.lineedit2=QLineEdit("b")
        self.btnok=QPushButton("登录")

        lay=QFormLayout()
        lay.addRow("user name:",self.lineedit1)
        lay.addRow("password:",self.lineedit2)
        lay.addWidget(self.btnok)
        self.setLayout(lay)

        self.lineedit1.textChanged.connect(self.change)
        self.lineedit2.textChanged.connect(self.change)

    def change(self):
        self.text1=self.lineedit1.text()
        self.text2=self.lineedit2.text()
        self.password=self.text1+'.'+self.text2


if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=login()
    mywin.show()
    sys.exit(app.exec_())

