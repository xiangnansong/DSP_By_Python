from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import sys
import numpy as np


class Widget(QtGui.QWidget):
    def __init__(self):
        self.list = []
        QtGui.QWidget.__init__(self)
        mainlayout = QtGui.QVBoxLayout()
        pw = pg.PlotWidget()
        pw.setBackground(QtGui.QColor(43, 43, 43))
        p1 = pw.plot()
        x1 = np.linspace(0, 2 * np.pi, 100)
        listy = []
        for i in x1:
            listy.append(self.integral(i))
        y1 = np.array(listy)
        p1.setData(x1, y1)
        mainlayout.addWidget(pw)
        self.setLayout(mainlayout)

    def integral(self, up):
        x = np.linspace(0, up, 100)
        y = 0
        for i in x:
            y += x[1] * np.abs(np.cos(i))
        return y


app = QtGui.QApplication(sys.argv)
pg.setConfigOptions(antialias=True)
qb = Widget()
qb.show()
sys.exit(app.exec_())

