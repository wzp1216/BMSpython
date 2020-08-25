# -*- coding: utf-8 -*-
# BMS tabU_widget   show the voltage of battery;
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

class tab_tmp(QWidget):
    def __init__(self):
        super().__init__()
    def __init__(self):
        super().__init__()
        self.batterytmp=[42,36,28,9,32,46,38,19,4,83,38,-19,-42,36,38,39]
    
    def paintEvent(self,QPaintEvent):
        p = QPainter(self)    
        apoint=30
        bpoint=50
        p.begin(self)
        for i in range(16):
            self.mydrawtmp(p,apoint,bpoint,self.batterytmp[i])
            apoint=apoint+110;
        p.end()
    
    def mydrawtmp(self,p,a,b,tmp):
        tmp=tmp+20;
        if tmp>80:tmp=80;
        if tmp<0:tmp=0;
        pen=QPen(Qt.black,1,Qt.SolidLine)
        p.setPen(pen)
        #draw lines
        tmpa=a;
        tmpb=b+20;
        for i in range(8):
            p.drawLine(tmpa,tmpb,tmpa+10,tmpb)
            tmpb=tmpb+10
        #draw arc;
        arcrect=QRectF(a+20,b+8,10,10)
        startAngle = 30 * 16;
        spanAngle = 120 * 16;
        p.drawArc(arcrect,startAngle,spanAngle)

        #draw recttop;
        longrect1=QRectF(a+20,b+10,10,80-tmp)
        brush0=QBrush(Qt.gray,Qt.SolidPattern)
        p.setBrush(brush0)
        p.drawRect(longrect1)
        #draw rectdown;
        longrect2=QRectF(a+20,b+90-tmp,10,tmp)
        p.setBrush(brush0)
        brush1=QBrush(Qt.red,Qt.SolidPattern)
        p.setBrush(brush1)
        p.drawRect(longrect2)

        #draw circle;
        circle1=QRectF(a+15,b+85,20,20)
        p.drawEllipse(circle1)

        #draw text
        pen1=QPen(Qt.black,3,Qt.SolidLine)
        p.setPen(pen1)
        p.setFont(QFont('SimSun',12))
        text1=str(tmp-20)+'℃'
        p.drawText(a,b+150,text1)
