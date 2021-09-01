import sys
import random
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class demo(QWidget):
    def __init__(self):
        super(demo, self).__init__()
        self.resize(600, 400)
        pg.setConfigOptions(leftButtonPan=False)
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        x = np.random.normal(size=1000)
        y = np.random.normal(size=1000)
        r_symbol = random.choice(['o', 's', 't', 'd', 'p', 'h', 'stat'])
        r_color = random.choice(['b', 'r', 'k'])

        self.pw = pg.PlotWidget(self)
        self.plot_data = self.pw.plot(x, y, pen=None, symbol=r_symbol, symbolBrush=r_color)
        self.plot_btn = QPushButton("change plot", self)
        self.plot_btn.clicked.connect(self.change_plot)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pw)
        self.layout.addWidget(self.plot_btn)
        self.setLayout(self.layout)

    def change_plot(self):
        x = np.random.normal(size=1000)
        y = np.random.normal(size=1000)
        r_symbol = random.choice(['o', 's', 't', 't1', 't2', 'd', '+', 'x', 'p', 'h', 'stat'])
        r_color = random.choice(['b', 'r', 'k', 'g', 'c', 'm', 'y', 'd', 'l', 's'])
        self.plot_data.setData(x, y, pen=None, symbol=r_symbol, symbolBrush=r_color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = demo()
    demo.show()
    sys.exit(app.exec_())
