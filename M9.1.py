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

        self.ws = 0.8
        self.wp = 0.7
        self.alphas = 35
        self.alphap = 3

        wsLabel = QtGui.QLabel("ws: ")
        wpLabel = QtGui.QLabel("wp: ")
        alphasLabel = QtGui.QLabel("alphas: ")
        alphapLabel = QtGui.QLabel("alphap: ")

        self.wsBox = QtGui.QDoubleSpinBox()
        self.wpBox = QtGui.QDoubleSpinBox()
        self.alphapBox = QtGui.QSpinBox()
        self.alphasBox = QtGui.QSpinBox()

        self.wsBox.setValue(self.ws)
        self.wpBox.setValue(self.wp)
        self.alphapBox.setValue(self.alphap)
        self.alphasBox.setValue(self.alphas)

        wsSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        wpSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        alphapSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        alphasSlider = QtGui.QSlider(QtCore.Qt.Horizontal)

        wpSlider.setMaximum(10)
        wpSlider.setValue(7)
        wsSlider.setMaximum(10)
        wsSlider.setValue(8)
        alphapSlider.setMaximum(10)
        alphapSlider.setValue(3)
        alphasSlider.setMaximum(100)
        alphasSlider.setValue(35)

        mainLayout.addWidget(pw)
        vBox1 = QtGui.QVBoxLayout()
        vBox2 = QtGui.QVBoxLayout()
        hBox1 = QtGui.QHBoxLayout()
        hBox2 = QtGui.QHBoxLayout()
        hBox3 = QtGui.QHBoxLayout()
        hBox4 = QtGui.QHBoxLayout()
        bottomLayout = QtGui.QHBoxLayout()

        hBox1.addWidget(wpLabel)
        hBox1.addWidget(self.wpBox)
        hBox1.addWidget(wpSlider)

        hBox2.addWidget(wsLabel)
        hBox2.addWidget(self.wsBox)
        hBox2.addWidget(wsSlider)

        hBox3.addWidget(alphapLabel)
        hBox3.addWidget(self.alphapBox)
        hBox3.addWidget(alphapSlider)

        hBox4.addWidget(alphasLabel)
        hBox4.addWidget(self.alphasBox)
        hBox4.addWidget(alphasSlider)

        vBox1.addLayout(hBox1)
        vBox1.addLayout(hBox2)
        vBox2.addLayout(hBox3)
        vBox2.addLayout(hBox4)

        bottomLayout.addLayout(vBox1)
        bottomLayout.addLayout(vBox2)

        mainLayout.addLayout(bottomLayout)
        self.setLayout(mainLayout)

        wsSlider.valueChanged.connect(self.onWsChange)
        wpSlider.valueChanged.connect(self.onWpChange)
        alphapSlider.valueChanged.connect(self.onAlphapChange)
        alphasSlider.valueChanged.connect(self.onAlphasChange)

        n1, wn1 = sig.buttord(self.wp, self.ws, self.alphap, self.alphas)
        B, A = sig.butter(n1, wn1)
        w2, h2 = sig.freqz(B, A, 1000)
        self.p1.setData(w2, np.abs(h2))

    @QtCore.pyqtSlot(int)
    def onWsChange(self, ws):
        self.ws = ws / 10
        n1, wn1 = sig.buttord(self.wp, self.ws, self.alphap, self.alphas)
        B, A = sig.butter(n1, wn1)
        w2, h2 = sig.freqz(B, A, 1000)
        self.p1.setData(w2, np.abs(h2))
        self.wsBox.setValue(self.ws)

    @QtCore.pyqtSlot(int)
    def onWpChange(self, wp):
        self.wp = wp / 10
        n1, wn1 = sig.buttord(self.wp, self.ws, self.alphap, self.alphas)
        B, A = sig.butter(n1, wn1)
        w2, h2 = sig.freqz(B, A, 1000)
        self.p1.setData(w2, np.abs(h2))
        self.wpBox.setValue(self.wp)

    @QtCore.pyqtSlot(int)
    def onAlphasChange(self, alphas):
        self.alphas = alphas
        n1, wn1 = sig.buttord(self.wp, self.ws, self.alphap, self.alphas)
        B, A = sig.butter(n1, wn1)
        w2, h2 = sig.freqz(B, A, 1000)
        self.p1.setData(w2, np.abs(h2))
        self.alphasBox.setValue(self.alphas)

    @QtCore.pyqtSlot(int)
    def onAlphapChange(self, alphap):
        self.alphap = alphap
        n1, wn1 = sig.buttord(self.wp, self.ws, self.alphap, self.alphas)
        B, A = sig.butter(n1, wn1)
        w2, h2 = sig.freqz(B, A, 1000)
        self.p1.setData(w2, np.abs(h2))
        self.alphapBox.setValue(self.alphap)


app = QtGui.QApplication(sys.argv)
pg.setConfigOptions(antialias=True)
qb = Widget()
qb.show()
sys.exit(app.exec_())
