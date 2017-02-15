from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import sys
import numpy as np
import scipy.signal as sig


class Widget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        mainLayout = QtGui.QVBoxLayout()
        pw = pg.PlotWidget()
        self.p1 = pw.plot()

        self.p2 = pw.plot(pen=None, symbol='o', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 100))

        pw.setBackground(QtGui.QColor(43, 43, 43))
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        for i in range(100):
            if y[i] > 0.8:
                y[i] = 0.8

            if y[i] < 0:
                y[i] = 0

        z = np.sin(x)
        self.p1.setData(x, y)
        self.p2.setData(x, z)
        mainLayout.addWidget(pw)
        self.setLayout(mainLayout)

app = QtGui.QApplication(sys.argv)
pg.setConfigOptions(antialias=True)
qb = Widget()
qb.show()
sys.exit(app.exec_())
