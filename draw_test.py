# -*- coding: utf-8 -*-
# test pyqt drawing 
import sys
from PyQt5.QtWidgets import QApplication

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class mytest(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("test draw")
        self.a=[27,41,20,38]
        self.show()

    def paintEvent(self,QPaintEvent):
        p = QPainter(self)    
        apoint=30
        bpoint=50
        p.begin(self)
        for i in range(4):
            self.mydrawtmp(p,apoint,bpoint,self.a[i])
            apoint=apoint+110;
        p.end()
    def mydrawtmp(self,p,a,b,tmp):
        if tmp>60:tmp=60;
        if tmp<-20:tmp=-20;
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
        text1=str(tmp)+'℃'
        p.drawText(a,b+150,text1)
    
    def mydraw(self,p,a,b,vol):
        voldraw=(int)(vol*100/4.2)
        if voldraw>100:    voldraw=100
        if voldraw<1:    voldraw=1
        pen=QPen(Qt.black,1,Qt.SolidLine)
        p.setPen(pen)

        head0=QRectF(a,b,50,100-voldraw)
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


class StockDialog(QWidget):
    def __init__(self, parent=None):
        super(StockDialog, self).__init__(parent)
        self.setWindowTitle("利用QPainter绘制各种图形")
        
        mainSplitter = QSplitter(Qt.Horizontal)
        mainSplitter.setOpaqueResize(True)
                  
        frame = QFrame(mainSplitter)
        mainLayout = QGridLayout(frame)
        #mainLayout.setMargin(10)
        mainLayout.setSpacing(6)

        label1=QLabel("形状：")
        label2=QLabel("画笔线宽：")
        label3=QLabel("画笔颜色：")
        label4=QLabel("画笔风格：")
        label5=QLabel("画笔顶端：")
        label6=QLabel("画笔连接点：")
        label7=QLabel("画刷风格：")
        label8=QLabel("画刷颜色：")
    
        self.shapeComboBox = QComboBox()
        self.shapeComboBox.addItem("Line", "Line")
        self.shapeComboBox.addItem("Rectangle", "Rectangle")
        self.shapeComboBox.addItem('Rounded Rectangle','Rounded Rectangle')
        self.shapeComboBox.addItem('Ellipse','Ellipse')
        self.shapeComboBox.addItem('Pie','Pie')
        self.shapeComboBox.addItem('Chord','Chord')
        self.shapeComboBox.addItem('Path','Path')
        self.shapeComboBox.addItem('Polygon','Polygon')
        self.shapeComboBox.addItem('Polyline','Polyline')
        self.shapeComboBox.addItem('Arc','Arc')
        self.shapeComboBox.addItem('Points','Points')
        self.shapeComboBox.addItem('Text','Text')
        self.shapeComboBox.addItem('Pixmap','Pixmap')
        
        self.widthSpinBox = QSpinBox()
        self.widthSpinBox.setRange(0,20)
        
        self.penColorFrame = QFrame()
        self.penColorFrame.setAutoFillBackground(True)
        self.penColorFrame.setPalette(QPalette(Qt.blue))
        self.penColorPushButton = QPushButton("更改")
        
        self.penStyleComboBox = QComboBox()
        self.penStyleComboBox.addItem("Solid",Qt.SolidLine)
        self.penStyleComboBox.addItem('Dash',  Qt.DashLine)
        self.penStyleComboBox.addItem('Dot',  Qt.DotLine)
        self.penStyleComboBox.addItem('Dash Dot',  Qt.DashDotLine)
        self.penStyleComboBox.addItem('Dash Dot Dot',  Qt.DashDotDotLine)
        self.penStyleComboBox.addItem('None',  Qt.NoPen)
        
        self.penCapComboBox = QComboBox()
        self.penCapComboBox.addItem("Flat",Qt.FlatCap)
        self.penCapComboBox.addItem('Square', Qt.SquareCap)
        self.penCapComboBox.addItem('Round', Qt.RoundCap)
        
        self.penJoinComboBox = QComboBox()
        self.penJoinComboBox.addItem("Miter",Qt.MiterJoin)
        self.penJoinComboBox.addItem('Bebel', Qt.BevelJoin)
        self.penJoinComboBox.addItem('Round', Qt.RoundJoin)
        
        self.brushStyleComboBox = QComboBox()
        self.brushStyleComboBox.addItem("Linear Gradient",Qt.LinearGradientPattern)
        self.brushStyleComboBox.addItem('Radial Gradient', Qt.RadialGradientPattern)
        self.brushStyleComboBox.addItem('Conical Gradient', Qt.ConicalGradientPattern)
        self.brushStyleComboBox.addItem('Texture', Qt.TexturePattern)
        self.brushStyleComboBox.addItem('Solid', Qt.SolidPattern)
        self.brushStyleComboBox.addItem('Horizontal', Qt.HorPattern)
        self.brushStyleComboBox.addItem('Vertical', Qt.VerPattern)
        self.brushStyleComboBox.addItem('Cross', Qt.CrossPattern)
        self.brushStyleComboBox.addItem('Backward Diagonal', Qt.BDiagPattern)
        self.brushStyleComboBox.addItem('Forward Diagonal', Qt.FDiagPattern)
        self.brushStyleComboBox.addItem('Diagonal Cross', Qt.DiagCrossPattern)
        self.brushStyleComboBox.addItem('Dense 1', Qt.Dense1Pattern)
        self.brushStyleComboBox.addItem('Dense 2', Qt.Dense2Pattern)
        self.brushStyleComboBox.addItem('Dense 3', Qt.Dense3Pattern)
        self.brushStyleComboBox.addItem('Dense 4', Qt.Dense4Pattern)
        self.brushStyleComboBox.addItem('Dense 5', Qt.Dense5Pattern)
        self.brushStyleComboBox.addItem('Dense 6', Qt.Dense6Pattern)
        self.brushStyleComboBox.addItem('Dense 7', Qt.Dense7Pattern)
        self.brushStyleComboBox.addItem('None', Qt.NoBrush)
        
        self.brushColorFrame = QFrame()
        self.brushColorFrame.setAutoFillBackground(True)
        self.brushColorFrame.setPalette(QPalette(Qt.green))
        self.brushColorPushButton = QPushButton("更改")
                                                              
        labelCol=0
        contentCol=1
        
        #建立布局
        mainLayout.addWidget(label1,1,labelCol)
        mainLayout.addWidget(self.shapeComboBox,1,contentCol)
        mainLayout.addWidget(label2,2,labelCol)
        mainLayout.addWidget(self.widthSpinBox,2,contentCol)
        mainLayout.addWidget(label3,4,labelCol)
        mainLayout.addWidget(self.penColorFrame,4,contentCol)
        mainLayout.addWidget(self.penColorPushButton,4,3)
        mainLayout.addWidget(label4,6,labelCol)
        mainLayout.addWidget(self.penStyleComboBox,6,contentCol)
        mainLayout.addWidget(label5,8,labelCol)
        mainLayout.addWidget(self.penCapComboBox,8,contentCol)
        mainLayout.addWidget(label6,10,labelCol)
        mainLayout.addWidget(self.penJoinComboBox,10,contentCol)
        mainLayout.addWidget(label7,12,labelCol)
        mainLayout.addWidget(self.brushStyleComboBox,12,contentCol)
        mainLayout.addWidget(label8,14,labelCol)
        mainLayout.addWidget(self.brushColorFrame,14,contentCol)
        mainLayout.addWidget(self.brushColorPushButton,14,3)
        mainSplitter1 = QSplitter(Qt.Horizontal)
        mainSplitter1.setOpaqueResize(True)
        
        stack1 = QStackedWidget()
        stack1.setFrameStyle(QFrame.Panel|QFrame.Raised)
        self.area = PaintArea()
        stack1.addWidget(self.area)        
        frame1 = QFrame(mainSplitter1)
        mainLayout1 = QVBoxLayout(frame1)
        #mainLayout1.setMargin(10)
        mainLayout1.setSpacing(6)
        mainLayout1.addWidget(stack1)

        layout = QGridLayout(self)
        layout.addWidget(mainSplitter1,0,0)
        layout.addWidget(mainSplitter,0,1)
        self.setLayout(layout)
        
        #信号和槽函数
        self.shapeComboBox.activated.connect(self.slotShape)
        self.widthSpinBox.valueChanged.connect(self.slotPenWidth)
        self.penColorPushButton.clicked.connect(self.slotPenColor)
        self.penStyleComboBox.activated.connect(self.slotPenStyle)
        self.penCapComboBox.activated.connect(self.slotPenCap)
        self.penJoinComboBox.activated.connect(self.slotPenJoin)
        self.brushStyleComboBox.activated.connect(self.slotBrush)
        self.brushColorPushButton.clicked.connect(self.slotBrushColor)
        
        self.slotShape(self.shapeComboBox.currentIndex())
        self.slotPenWidth(self.widthSpinBox.value())
        self.slotBrush(self.brushStyleComboBox.currentIndex())        
        
    def slotShape(self,value):
        shape =  self.area.Shape[value]
        self.area.setShape(shape)
    
    def slotPenWidth(self,value):
        color = self.penColorFrame.palette().color(QPalette.Window)
        style = Qt.PenStyle(self.penStyleComboBox.itemData(self.penStyleComboBox.currentIndex(),Qt.UserRole))
        cap = Qt.PenCapStyle(self.penCapComboBox.itemData(self.penCapComboBox.currentIndex(),Qt.UserRole))
        join = Qt.PenJoinStyle(self.penJoinComboBox.itemData(self.penJoinComboBox.currentIndex(),Qt.UserRole))
        self.area.setPen(QPen(color,value,style,cap,join))
    
    def slotPenStyle(self,value):
        self.slotPenWidth(value)
    
    def slotPenCap(self,value):
        self.slotPenWidth(value)
    
    def slotPenJoin(self,value):
        self.slotPenWidth(value)
    
    def slotPenColor(self):
        color = QColorDialog.getColor(Qt.blue)
        self.penColorFrame.setPalette(QPalette(color))
        self.area.setPen(QPen(color))
        
    def slotBrushColor(self):
        color = QColorDialog.getColor(Qt.blue)
        self.brushColorFrame.setPalette(QPalette(color))
        self.slotBrush(self.brushStyleComboBox.currentIndex())
    
    def slotBrush(self,value):
        color = self.brushColorFrame.palette().color(QPalette.Window)
        style = Qt.BrushStyle(self.brushStyleComboBox.itemData(value,Qt.UserRole))
        
        if(style == Qt.LinearGradientPattern):
            linearGradient = QLinearGradient(0,0,400,400)
            linearGradient.setColorAt(0.0,Qt.white)
            linearGradient.setColorAt(0.2,color)
            linearGradient.setColorAt(1.0,Qt.black)
            self.area.setBrush(linearGradient)
        elif style ==Qt.RadialGradientPattern:
            radialGradient = QRadialGradient(200, 200, 80, 70, 70);
            radialGradient.setColorAt(0.0, Qt.white)
            radialGradient.setColorAt(0.2, Qt.green)
            radialGradient.setColorAt(1.0, Qt.black)
            self.area.setBrush(radialGradient)
        elif(style == Qt.ConicalGradientPattern):
            conicalGradient = QConicalGradient(200,200,30)
            conicalGradient.setColorAt(0.0,Qt.white)
            conicalGradient.setColorAt(0.2,color)
            conicalGradient.setColorAt(1.0,Qt.black)
            self.area.setBrush(conicalGradient)
        elif(style == Qt.TexturePattern):
            self.area.setBrush(QBrush(QPixmap("images/brick.png")))
        else:
            self.area.setBrush(QBrush(color,style))
        
    
class PaintArea(QWidget):
    def __init__(self):
        super(PaintArea,self).__init__()
        self.Shape = ["Line","Rectangle", 'Rounded Rectangle', "Ellipse", "Pie", 'Chord', 
    "Path","Polygon", "Polyline", "Arc", "Points", "Text", "Pixmap"]
        self.setPalette(QPalette(Qt.white))
        self.setAutoFillBackground(True)
        self.setMinimumSize(400,400)
        self.pen = QPen()
        self.brush = QBrush()        
    
    def setShape(self,s):
        self.shape = s
        self.update()
        
    def setPen(self,p):
        self.pen = p
        self.update()
    
    def setBrush(self,b):
        self.brush = b
        self.update()
    
    def paintEvent(self,QPaintEvent):
        p = QPainter(self)
        p.setPen(self.pen)
        p.setBrush(self.brush)
        
        rect = QRect(50,100,300,200) 
        points = [QPoint(150,100),QPoint(300,150),QPoint(350,250),QPoint(100,300)]
        startAngle = 30 * 16
        spanAngle = 120 * 16
        
        path = QPainterPath();
        path.addRect(150,150,100,100)
        path.moveTo(100,100)
        path.cubicTo(300,100,200,200,300,300)
        path.cubicTo(100,300,200,200,100,100)
        
        if self.shape == "Line":
            p.drawLine(rect.topLeft(),rect.bottomRight())
        elif self.shape == "Rectangle":
            p.drawRect(rect)
        elif self.shape == 'Rounded Rectangle':
            p.drawRoundedRect(rect, 25, 25, Qt.RelativeSize)
        elif self.shape == "Ellipse":
            p.drawEllipse(rect)
        elif self.shape == "Polygon":
            p.drawPolygon(QPolygon(points),Qt.WindingFill)
        elif self.shape == "Polyline":
            p.drawPolyline(QPolygon(points))
        elif self.shape == "Points":
            p.drawPoints(QPolygon(points))
        elif self.shape == "Pie":
            p.drawPie(rect, startAngle, spanAngle)
        elif self.shape == "Arc":
            p.drawArc(rect,startAngle,spanAngle)
        elif self.shape == "Chord":
            p.drawChord(rect, startAngle, spanAngle)
        elif self.shape == "Path":
            p.drawPath(path)
        elif self.shape == "Text":
            p.drawText(rect,Qt.AlignCenter,"Hello Qt!")
        elif self.shape == "Pixmap":
            p.drawPixmap(150,150,QPixmap("images/qt-logo.png"))
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    #form = StockDialog()
    form = mytest()
    form.show()
    app.exec_()

