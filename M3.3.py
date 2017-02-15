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

        pw1 = pg.PlotWidget()
        pw2 = pg.PlotWidget()
        pw3 = pg.PlotWidget()
        pw.setBackground(QtGui.QColor(43, 43, 43))
        pw1.setBackground(QtGui.QColor(43, 43, 43))
        pw2.setBackground(QtGui.QColor(43, 43, 43))
        pw3.setBackground(QtGui.QColor(43, 43, 43))


        pw.setLabel('left', '幅值')
        pw1.setLabel('left', '角度')
        pw2.setLabel('left', '实部')
        pw3.setLabel('left', '虚部')

        self.p2 = pw1.plot()
        self.p3 = pw2.plot()
        self.p4 = pw3.plot()

        self.numLine = QtGui.QLineEdit()
        self.denLine = QtGui.QLineEdit()
        checkBtn = QtGui.QPushButton("确认")
        numLabel = QtGui.QLabel("分子")
        denLabel = QtGui.QLabel("分母")

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
        w = np.linspace(-1 * np.pi, np.pi, 256)
        x, y = sig.freqz(num, den, w)
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
        num = np.array(lista)
        den = np.array(listb)
        w = np.linspace(-1 * np.pi, np.pi, 256)
        x, y = sig.freqz(num, den, w)
        self.p1.setData(x, np.abs(y))
        self.p2.setData(x, np.angle(y))
        self.p3.setData(x, np.real(y))
        self.p4.setData(x, np.imag(y))


app = QtGui.QApplication(sys.argv)
pg.setConfigOptions(antialias=True)
qb = Widget()
qb.show()
sys.exit(app.exec_())

