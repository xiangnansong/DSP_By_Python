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
        pw1 = pg.PlotWidget()
        pw.setBackground(QtGui.QColor(43, 43, 43))
        pw1.setBackground(QtGui.QColor(43, 43, 43))
        p1 = pw.plot()
        p2 = pw1.plot()

        x1 = np.linspace(0, 10, 100)
        y1 = np.sin(x1)
        p1.setData(x1, y1)

        for i in y1:
            listc = []
            if i > 0:
                listc.append(1)
            else:
                listc.append(0)
                i = i * -1

            c = int(i * 2048)
            listc += self.f1(c)

            operator = {'000': self.f000, '001': self.f001, '010': self.f010,
                        '011': self.f011,
                        '100': self.f100,
                        '101': self.f101,
                        '110': self.f110,
                        '111': self.f111}

            tmp = [str(i) for i in listc[1:4]]
            strt = ''.join(tmp)
            listc += operator.get(strt)(c)
            self.list.append(listc)

        listy = []
        for l in self.list:

            listy.append(self.unlock(l))

        nyy = np.array(listy)

        p2.setData(x1, nyy)
        mainlayout.addWidget(pw)
        mainlayout.addWidget(pw1)
        self.setLayout(mainlayout)

    def unlock(self, lista):

        tmp = [str(i) for i in lista[1:4]]
        strt = ''.join(tmp)

        operator = {'000': self.f000i, '001': self.f001i, '010': self.f010i,
                    '011': self.f011i,
                    '100': self.f100i,
                    '101': self.f101i,
                    '110': self.f110i,
                    '111': self.f111i}

        value = operator.get(strt)(lista)
        if lista[0] == 0:
            value *= -1
        return value

    def f000i(self, list):
        tmp = 8 * list[4] + 4 * list[5] + 2 * list[6] + list[7]
        return tmp

    def f001i(self, list):
        tmp = 8 * list[4] + 4 * list[5] + 2 * list[6] + list[7]
        tmp += 16
        return tmp

    def f010i(self, list):
        tmp = (8 * list[4] + 4 * list[5] + 2 * list[6] + list[7]) * 2
        tmp += 32
        return tmp

    def f011i(self, list):
        tmp = (8 * list[4] + 4 * list[5] + 2 * list[6] + list[7]) * 4
        tmp += 64
        return tmp

    def f100i(self, list):
        tmp = (8 * list[4] + 4 * list[5] + 2 * list[6] + list[7]) * 8
        tmp += 128
        return tmp

    def f101i(self, list):
        tmp = (8 * list[4] + 4 * list[5] + 2 * list[6] + list[7]) * 16
        tmp += 256
        return tmp

    def f110i(self, list):
        tmp = (8 * list[4] + 4 * list[5] + 2 * list[6] + list[7]) * 32
        tmp += 512
        return tmp

    def f111i(self, list):
        tmp = (8 * list[4] + 4 * list[5] + 2 * list[6] + list[7]) * 64
        tmp += 1024
        return tmp

    def f000(self, c):

        list = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0],
                [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1],
                [1, 1, 1, 0], [1, 1, 1, 1]]

        return list[c]


    def f001(self, c):
        c -= 16
        list = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0],
                [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1],
                [1, 1, 1, 0], [1, 1, 1, 1]]

        return list[c]


    def f010(self, c):

        c -= 32
        c = int(c / 2)
        list = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0],
                [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1],
                [1, 1, 1, 0], [1, 1, 1, 1]]

        return list[c]


    def f011(self, c):
        c -= 64
        c = int(c / 4)
        list = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0],
                [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1],
                [1, 1, 1, 0], [1, 1, 1, 1]]

        return list[c]


    def f100(self, c):
        c -= 128
        c = int(c / 8)
        list = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0],
                [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1],
                [1, 1, 1, 0], [1, 1, 1, 1]]

        return list[c]


    def f101(self, c):
        c -= 256
        c = int(c / 16)
        list = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0],
                [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1],
                [1, 1, 1, 0], [1, 1, 1, 1]]

        return list[c]


    def f110(self, c):
        c -= 512
        c = int(c / 32)
        list = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0],
                [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1],
                [1, 1, 1, 0], [1, 1, 1, 1]]

        return list[c]

    def f111(self, c):
        c -= 1024
        c = int(c / 64)
        list = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1], [0, 1, 1, 0],
                [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1],
                [1, 1, 1, 0], [1, 1, 1, 1]]

        return list[c]

    def f1(self, c):
        list = []
        if c >= 128:
            list.append(1)
            if c >= 512:
                list.append(1)
                if c >= 1024:
                    list.append(1)
                else:
                    list.append(0)
            else:
                list.append(0)
                if c >= 256:
                    list.append(1)
                else:
                    list.append(0)
        else:
            list.append(0)
            if c >= 32:
                list.append(1)
                if c >= 64:
                    list.append(1)
                else:
                    list.append(0)
            else:
                list.append(0)
                if c >= 16:
                    list.append(1)
                else:
                    list.append(0)

        return list


app = QtGui.QApplication(sys.argv)
pg.setConfigOptions(antialias=True)
qb = Widget()
qb.show()
sys.exit(app.exec_())
