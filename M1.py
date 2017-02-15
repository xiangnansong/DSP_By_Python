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

        pw.setBackground(QtGui.QColor(43, 43, 43))
        x = np.linspace(0, 10, 100)
        y = 1 - np.exp(x * -0.5) * np.cos(2 * x)
        self.p1.setData(x, y)
        mainLayout.addWidget(pw)
        self.setLayout(mainLayout)


app = QtGui.QApplication(sys.argv)
pg.setConfigOptions(antialias=True)
qb = Widget()
qb.show()
sys.exit(app.exec_())
