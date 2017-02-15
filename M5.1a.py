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
        pw.setBackground(QtGui.QColor(43, 43, 43))
        self.p1 = pw.plot()
        self.p2 = pw.plot(pen=None, symbol='o', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 100))
        self.value = 10

        checkBtn = QtGui.QPushButton("确认")
        valueLabel = QtGui.QLabel("value:  ")
        self.valueLine = QtGui.QLineEdit()

        bottomLayout = QtGui.QHBoxLayout()
        bottomLayout.addWidget(valueLabel)
        bottomLayout.addWidget(self.valueLine)
        bottomLayout.addWidget(checkBtn)
        mainLayout.addWidget(pw)
        mainLayout.addLayout(bottomLayout)
        self.setLayout(mainLayout)

        checkBtn.clicked.connect(self.onCheck)

    @QtCore.pyqtSlot()
    def onCheck(self):
        self.value = eval(self.valueLine.text())
        n = [1] * (2 * self.value + 1)
        w = np.linspace(0, 2 * np.pi, 256)
        x, y = sig.freqz(n, 1, w)
        y1 = np.fft.fft(n)
        self.p1.setData(w / np.pi, np.abs(y))
        x1 = np.arange(0, 2, 2 / (2 * self.value + 1))
        self.p2.setData(x1, np.abs(y1))


app = QtGui.QApplication(sys.argv)
pg.setConfigOptions(antialias=True)
qb = Widget()
qb.show()
sys.exit(app.exec_())
