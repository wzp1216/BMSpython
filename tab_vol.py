# -*- coding: utf-8 -*-
# BMS tabU_widget   show the voltage of battery;
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class tab_vol(QWidget):
    def __init__(self):
        super().__init__()
        self.batteryvol=[4.2,3.6,2.8,1.9,3.2,4.6,3.8,1.9,4.2,3.6,3.8,0.9,4.2,3.6,3.8,3.9]
    
    def paintEvent(self,QPaintEvent):
        p = QPainter(self)    
        apoint=30
        bpoint=50
        p.begin(self)
        for i in range(16):
            self.mydraw(p,apoint,bpoint,self.batteryvol[i])
            apoint=apoint+110;
        p.end()
    
    def mydraw(self,p,a,b,vol):
        voldraw=(int)(vol*100/4.2)
        if voldraw>100:    voldraw=100
        if voldraw<1:    voldraw=1
        pen=QPen(Qt.black,1,Qt.SolidLine)
        p.setPen(pen)

        head0=QRectF(a+15,b-5,20,5)
        brush0=QBrush(Qt.gray,Qt.SolidPattern)
        p.setBrush(brush0)
        p.drawRect(head0)       #draw   battery vol
        
        head1=QRectF(a,b,50,100-voldraw)
        brush0=QBrush(Qt.gray,Qt.SolidPattern)
        p.setBrush(brush0)
        p.drawRect(head1)       #draw   battery vol

        cc=b+100-voldraw
        batterybody=QRectF(a,cc,50,voldraw)
        brush1=QBrush(Qt.green,Qt.SolidPattern)
        p.setBrush(brush1)
        p.drawRect(batterybody)       #draw   battery vol

        pen1=QPen(Qt.black,3,Qt.SolidLine)
        p.setPen(pen1)
        p.setFont(QFont('SimSun',12))
        text1=str(vol)+'V'
        p.drawText(a,b+150,text1)



