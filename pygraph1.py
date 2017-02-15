from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import sys
import numpy as np


def rand(n):
    data = np.random.random(n)
    data[int(n * 0.1):int(n * 0.13)] += .5
    data[int(n * 0.18)] += 2
    data[int(n * 0.1):int(n * 0.13)] *= 5
    data[int(n * 0.18)] *= 20
    data *= 1e-12
    return data, np.arange(n, n + len(data)) / float(n)


class Widget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.pw = pg.PlotWidget()
        vBox = QtGui.QVBoxLayout()

        # palette = QtGui.QPalette()
        # palette.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QColor(43, 43, 43)))
        # self.setPalette(palette)

        btn = QtGui.QPushButton("adjust")
        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        vBox.addWidget(self.pw)

        self.slider.setMaximum(20)
        self.slider.setValue(15)

        vBox.addWidget(self.slider)

        # vBox.addWidget(btn)
        self.setLayout(vBox)

        # palette = QtGui.QPalette()
        # palette.setBrush(self.pw.backgroundRole(), QtGui.QBrush(QtGui.QColor(100, 200, 100)))

        self.pw.setBackground(QtGui.QColor(43, 43, 43))

        self.pw.setLabel('left', 'Value', 'V')
        self.pw.setLabel('bottom', 'Time', 's')
        self.p1 = self.pw.plot()
        self.p2 = self.pw.plot(pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 100))
        self.p1.setPen((200, 200, 100))
        # yd, xd = rand(10000)


        self.L = 10
        self.A = 1.5
        self.omega = 20
        self.phi = 0
        self.n = np.arange(0, self.L)
        self.N = np.linspace(0, self.L, 1000)
        x = self.A * np.cos(self.omega * self.n + self.phi)
        x1 = self.A * np.cos(self.omega * self.N + self.phi)
        self.p1.setData(x=self.N, y=x1)
        self.p2.setData(self.n, x)
        self.slider.valueChanged.connect(self.onAdjust)

    @QtCore.pyqtSlot()
    def onAdjust(self):
        x1 = self.slider.value() / 10 * np.cos(20 * self.N + self.phi)
        self.p1.setData(self.N, x1)


app = QtGui.QApplication(sys.argv)
pg.setConfigOptions(antialias=True)
qb = Widget()
qb.show()
sys.exit(app.exec_())
