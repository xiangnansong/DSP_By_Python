from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import sys
import numpy as np


class Widget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        # declear variable
        self.L = 41
        self.A = 1.5
        self.omega = 1
        self.phi = 0

        # declear layouts
        mainlayout = QtGui.QVBoxLayout()

        self.pw = pg.PlotWidget()
        self.pw.setBackground(QtGui.QColor(43, 43, 43))
        self.p1 = self.pw.plot()
        self.p2 = self.pw.plot(pen=None, symbol='o', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 100))
        n = np.arange(0, self.L)
        N = np.linspace(0, self.L, 1000)
        y = self.A * np.cos(self.omega * n * np.pi + self.phi)
        Y = self.A * np.cos(self.omega * N * np.pi + self.phi)
        self.p1.setData(N, Y)
        self.p2.setData(n, y)

        # declear widgets
        lengthSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        amplitudeSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        omegaSlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        phiSlider = QtGui.QSlider(QtCore.Qt.Horizontal)

        self.lengthBox = QtGui.QSpinBox()
        self.amplitudeBox = QtGui.QDoubleSpinBox()
        self.omegaBox = QtGui.QDoubleSpinBox()
        self.phiBox = QtGui.QDoubleSpinBox()

        lengthLabel = QtGui.QLabel("长度")
        amplitudeLabel = QtGui.QLabel("幅度")
        omegaLabel = QtGui.QLabel("频率")
        phiLabel = QtGui.QLabel("相位")

        # init widgets
        lengthSlider.setMaximum(100)
        lengthSlider.setValue(41)

        amplitudeSlider.setMaximum(20)
        amplitudeSlider.setValue(15)

        omegaSlider.setMaximum(20)
        omegaSlider.setValue(1)

        phiSlider.setMaximum(20)
        phiSlider.setValue(0)

        self.lengthBox.setValue(41)
        self.amplitudeBox.setValue(1.5)
        self.omegaBox.setValue(0.1)
        self.phiBox.setValue(0)

        vBox1 = QtGui.QVBoxLayout()
        hCBox1 = QtGui.QHBoxLayout()
        hCBox1.addWidget(self.amplitudeBox)
        hCBox1.addWidget(amplitudeSlider)
        vBox1.addWidget(amplitudeLabel)
        vBox1.addLayout(hCBox1)

        vBox2 = QtGui.QVBoxLayout()
        hCBox2 = QtGui.QHBoxLayout()
        hCBox2.addWidget(self.lengthBox)
        hCBox2.addWidget(lengthSlider)
        vBox2.addWidget(lengthLabel)
        vBox2.addLayout(hCBox2)

        vBox3 = QtGui.QVBoxLayout()
        hCBox3 = QtGui.QHBoxLayout()
        hCBox3.addWidget(self.omegaBox)
        hCBox3.addWidget(omegaSlider)
        vBox3.addWidget(omegaLabel)
        vBox3.addLayout(hCBox3)

        vBox4 = QtGui.QVBoxLayout()
        hCBox4 = QtGui.QHBoxLayout()
        hCBox4.addWidget(self.phiBox)
        hCBox4.addWidget(phiSlider)
        vBox4.addWidget(phiLabel)
        vBox4.addLayout(hCBox4)

        mainlayout.addWidget(self.pw)
        hBox1 = QtGui.QHBoxLayout()
        hBox1.addLayout(vBox1)
        hBox1.addLayout(vBox2)
        hBox2 = QtGui.QHBoxLayout()
        hBox2.addLayout(vBox3)
        hBox2.addLayout(vBox4)
        mainlayout.addLayout(hBox1)
        mainlayout.addLayout(hBox2)

        self.setLayout(mainlayout)

        lengthSlider.valueChanged.connect(self.lengthChange)
        amplitudeSlider.valueChanged.connect(self.amplitudeChange)
        omegaSlider.valueChanged.connect(self.omegaChange)
        phiSlider.valueChanged.connect(self.phiChange)

    @QtCore.pyqtSlot(int)
    def lengthChange(self, L):
        self.L = L
        n = np.arange(0, self.L)
        N = np.linspace(0, self.L, 1000)
        y = self.A * np.cos(self.omega * n * np.pi + self.phi)
        Y = self.A * np.cos(self.omega * N * np.pi + self.phi)
        self.p1.setData(N, Y)
        self.p2.setData(n, y)
        self.lengthBox.setValue(L)

    @QtCore.pyqtSlot(int)
    def amplitudeChange(self, A):
        self.A = A / 10
        n = np.arange(0, self.L)
        N = np.linspace(0, self.L, 1000)
        y = self.A * np.cos(self.omega * n * np.pi + self.phi)
        Y = self.A * np.cos(self.omega * N * np.pi + self.phi)
        self.p1.setData(N, Y)
        self.p2.setData(n, y)
        self.amplitudeBox.setValue(self.A)

    @QtCore.pyqtSlot(int)
    def omegaChange(self, omega):
        self.omega = omega / 10
        n = np.arange(0, self.L)
        N = np.linspace(0, self.L, 1000)
        y = self.A * np.cos(self.omega * n * np.pi + self.phi)
        Y = self.A * np.cos(self.omega * N * np.pi + self.phi)
        self.p1.setData(N, Y)
        self.p2.setData(n, y)
        self.omegaBox.setValue(self.omega)

    @QtCore.pyqtSlot(int)
    def phiChange(self, phi):
        self.phi = phi / 10 * np.pi
        n = np.arange(0, self.L)
        N = np.linspace(0, self.L, 1000)
        y = self.A * np.cos(self.omega * n * np.pi + self.phi)
        Y = self.A * np.cos(self.omega * N * np.pi + self.phi)
        self.p1.setData(N, Y)
        self.p2.setData(n, y)
        self.phiBox.setValue(self.phi)


app = QtGui.QApplication(sys.argv)
pg.setConfigOptions(antialias=True)
qb = Widget()
qb.show()
sys.exit(app.exec_())
