from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import sys
import numpy as np


class Widget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.frequency = 3
        self.omega = 10

        mainlayout = QtGui.QVBoxLayout()
        self.pw = pg.PlotWidget()
        self.pw.setBackground(QtGui.QColor(43, 43, 43))
        self.p1 = self.pw.plot()
        self.p2 = self.pw.plot(pen=None, symbol='o', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 100))

        self.frequencyBox = QtGui.QSpinBox()
        self.omegaBox = QtGui.QSpinBox()

        frequencySlider = QtGui.QSlider(QtCore.Qt.Horizontal)
        omegaSlider = QtGui.QSlider(QtCore.Qt.Horizontal)

        frequencyLabel = QtGui.QLabel("频率: ")
        omegaLabel = QtGui.QLabel("采样: ")

        hBox1 = QtGui.QHBoxLayout()
        hBox2 = QtGui.QHBoxLayout()

        hBox1.addWidget(frequencyLabel)
        hBox1.addWidget(self.frequencyBox)
        hBox1.addWidget(frequencySlider)

        hBox2.addWidget(omegaLabel)
        hBox2.addWidget(self.omegaBox)
        hBox2.addWidget(omegaSlider)

        mainlayout.addWidget(self.pw)
        mainlayout.addLayout(hBox1)
        mainlayout.addLayout(hBox2)

        self.setLayout(mainlayout)

        frequencySlider.setMaximum(20)
        omegaSlider.setMaximum(20)

        frequencySlider.setValue(self.frequency)
        omegaSlider.setValue(self.omega)

        x = np.linspace(0, 1, 1000)
        x1 = np.arange(0, self.omega, 1)
        y = np.cos(2 * np.pi * self.frequency * x)
        y1 = np.cos(2 * np.pi * self.frequency * (x1 / self.omega))

        self.p1.setData(x, y)
        self.p2.setData(x1 / self.omega, y1)

        frequencySlider.valueChanged.connect(self.onFrequencyChange)
        omegaSlider.valueChanged.connect(self.onOmegaChange)

    @QtCore.pyqtSlot(int)
    def onFrequencyChange(self, frequency):
        self.frequency = frequency
        self.frequencyBox.setValue(frequency)
        x = np.linspace(0, 1, 1000)
        y = np.cos(2 * np.pi * self.frequency * x)
        self.p1.setData(x, y)

    @QtCore.pyqtSlot(int)
    def onOmegaChange(self, omega):
        self.omega = omega
        self.omegaBox.setValue(omega)
        x1 = np.arange(0, self.omega, 1)
        y1 = np.cos(2 * np.pi * self.frequency * (x1 / self.omega))
        self.p2.setData(x1 / self.omega, y1)


app = QtGui.QApplication(sys.argv)
pg.setConfigOptions(antialias=True)
qb = Widget()
qb.show()
sys.exit(app.exec_())
