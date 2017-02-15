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

        pw1 = pg.PlotWidget()
        pw2 = pg.PlotWidget()
        pw3 = pg.PlotWidget()
        pw.setBackground(QtGui.QColor(43, 43, 43))
        pw1.setBackground(QtGui.QColor(43, 43, 43))
        pw2.setBackground(QtGui.QColor(43, 43, 43))
        pw3.setBackground(QtGui.QColor(43, 43, 43))

        pw.setLabel('left', 'xa(n)')
        pw1.setLabel('left', 'xb(b)')
        pw2.setLabel('left', 'xa(n) xb(n)')

        pw3.setLabel('left', '')

        self.p1 = pw.plot(pen=None, symbol='o', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 100))
        self.p2 = pw1.plot(pen=None, symbol='o', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 100))
        self.p3 = pw2.plot(pen=None, symbol='o', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 100))
        self.p4 = pw3.plot(pen=None, symbol='o', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 100))


        self.numLine = QtGui.QLineEdit()
        self.denLine = QtGui.QLineEdit()
        checkBtn = QtGui.QPushButton("确认")
        numLabel = QtGui.QLabel("xa: ")
        denLabel = QtGui.QLabel("xb: ")

        hBox1 = QtGui.QHBoxLayout()
        hBox2 = QtGui.QHBoxLayout()

        hBox1.addWidget(numLabel)
        hBox1.addWidget(self.numLine)

        hBox2.addWidget(denLabel)
        hBox2.addWidget(self.denLine)

        vBox = QtGui.QVBoxLayout()
        vBox.addLayout(hBox1)
        vBox.addLayout(hBox2)

        bottomLayout = QtGui.QHBoxLayout()
        bottomLayout.addLayout(vBox)
        bottomLayout.addWidget(checkBtn)

        topLayout = QtGui.QGridLayout()
        topLayout.addWidget(pw, 0, 0)
        topLayout.addWidget(pw1, 0, 1)
        topLayout.addWidget(pw2, 1, 0)
        topLayout.addWidget(pw3, 1, 1)

        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)
        self.setLayout(mainLayout)

        lista = [1] * 21
        listb = [1]
        num = np.array(lista)
        den = np.array(listb)
        n = np.arange(0, 7, 1)
        w = np.linspace(-1 * np.pi, np.pi, 1024)
        x, y = sig.freqz(0.5 * n, 1, w)
        y = y * np.exp(complex(0, 1) * (num.size / 2) * w)
        self.p1.setData(x, np.abs(y))
        self.p2.setData(x, np.angle(y))
        self.p3.setData(x, np.real(y))
        self.p4.setData(x, np.imag(y))

        checkBtn.clicked.connect(self.onCheck)

    @QtCore.pyqtSlot()
    def onCheck(self):
        a = self.numLine.text()
        b = self.denLine.text()
        listTmpa = a.split(" ")
        listTmpb = b.split(" ")
        lista = [eval(i) for i in listTmpa]
        listb = [eval(i) for i in listTmpb]
        xa = np.array(lista)
        xb = np.array(listb)

        xak = np.fft.fft(xa, 8)
        xbk = np.fft.fft(xb, 8)

        xak1 = np.fft.fft(xb, 16)
        xbk1 = np.fft.fft(xb, 16)

        f = np.fft.ifft(xak * xbk, 8)
        h = np.fft.ifft(xak1 * xbk1, 16)

        x = np.arange(0, 8, 1)
        x1 = np.arange(0, 15, 1)
        h = [i for i in h[1:16]]

        self.p1.setData(x, xa)
        self.p2.setData(x, xb)
        self.p3.setData(x, f)
        self.p4.setData(x1, h)


app = QtGui.QApplication(sys.argv)
pg.setConfigOptions(antialias=True)
qb = Widget()
qb.show()
sys.exit(app.exec_())
