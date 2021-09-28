# -*- coding: utf-8 -*-
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import *
from tab_vol import tab_vol
from tab_tmp import tab_tmp
from dlg_draw import dlg_draw
from tab_com import tab_com
from dlg_qt_draw import dlg_qt_draw
from tab_other import tab_data,tab_alter,tab_battery,tab_user


class bms_mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.set_size_pos()
        self.add_menu()
        self.add_mywidget()
    def set_size_pos(self):
        self.setObjectName("BMS_Mainwindow")
        self.desktop=QApplication.desktop()
        self.maxheight=self.desktop.height()-150
        self.maxwidth=self.desktop.width()-100
        self.setFixedSize(self.maxwidth,self.maxheight)
        self.move(50,50)
        self.setWindowTitle("梯次利用锂电池管理系统 BMS_Manage_System")
    def add_menu(self):
        #menu
        menubar=self.menuBar()
        self.filemenu=menubar.addMenu("FILE")
        self.filemenu.addAction("New")
        self.file_open_action=self.filemenu.addAction("Open")
        self.filemenu.addAction("Save")
        self.filemenu.addAction("Save As")
        self.filemenu.addSeparator()
        self.actionQuit=QtWidgets.QAction("Quit",self)
        self.filemenu.addAction(self.actionQuit)
        self.actionQuit.triggered.connect(self.close)
        self.helpmenu=menubar.addMenu("HELP")
        self.helpmenu.addAction("Help")
        self.actionAbout=QtWidgets.QAction("About",self)
        self.helpmenu.addAction(self.actionAbout)
        self.actionAbout.triggered.connect(self.About)

        self.file_open_action.triggered.connect(self.file_open)

        #status bar
        self.mystatusBar=QStatusBar()
        self.setStatusBar(self.mystatusBar)
        self.mystatusBar.showMessage("BMS software is ready")
    def file_open(self):
        fname=QFileDialog.getOpenFileName(self,'open file','.\\',"all (*.*)")

    def add_mywidget(self):
        #下面是用splitter实现
        self.select_bettery=QComboBox()
        self.select_bettery.addItems(["20200711B0001","20200918A0001","20200918A0002","20200918A0003","20201003A0001","20201102C0001"])

        self.tab_top=QTabWidget(self)
        self.tab1=tab_vol()
        self.tab2=tab_tmp()
        self.tab3=tab_com();
        self.tab4=tab_data();
        self.tab5=tab_alter();
        self.tab6=tab_battery();
        self.tab7=tab_user();
        self.tab_top.addTab(self.tab1,"电池电压")
        self.tab_top.addTab(self.tab2,"电池温度")
        self.tab_top.addTab(self.tab3,"串口通信")
        self.tab_top.addTab(self.tab4,"数据报表")
        self.tab_top.addTab(self.tab5,"报警记录")
        self.tab_top.addTab(self.tab6,"设备管理")
        self.tab_top.addTab(self.tab7,"用户管理")


        self.tab_down=QTabWidget(self)
        self.mydraw=dlg_qt_draw(self)

        self.tab_down.addTab(self.mydraw,"动态数据")
        self.label1=QLabel("请选择电池模组：")

        self.mysplitter=QSplitter(0x04,self)
        self.mysplitter.addWidget(self.label1)
        self.mysplitter.addWidget(self.select_bettery)
        self.mysplitter.addWidget(self.tab_top)
        self.mysplitter.addWidget(self.tab_down)
        self.mysplitter.move(10,30)
        self.mysplitter.resize(self.maxwidth-50,self.maxheight-50)
        self.tab_top.resize(self.maxwidth-100,self.maxheight/2-100)
        self.tab_down.resize(self.maxwidth-100,self.maxheight/2-100)


    def About(self):
        QMessageBox.about(self,"About","梯次利用锂电池管理系统\n浙江省科技厅项目\n动力锂离子电池在储能系统中再利用的关键技术研究\n主持单位：浙江工业职业技术学院\nEMAIL：wzp1216@163.com")


    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        opt = QtWidgets.QStyleOption()
        opt.initFrom(self)
        painter = QtGui.QPainter(self)
        #painter.setRenderHint(QtGui.QPainter.Antialiasing) # 反锯齿
        self.style().drawPrimitive(QtWidgets.QStyle.PE_Widget, opt, painter, self)


        



