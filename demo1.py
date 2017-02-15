from PyQt5 import QtWidgets, QtCore
import sys


class Boxlayout(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setWindowTitle('box')
        vBox = QtWidgets.QVBoxLayout()
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setMaximum(100)
        self.slider.setValue(10)

        self.edit = QtWidgets.QLineEdit()
        vBox.addWidget(self.edit)
        vBox.addWidget(self.slider)
        self.setLayout(vBox)
        self.resize(300, 150)

        # the usage of connect in qt5, the argument of the slot should not be showed
        self.slider.valueChanged.connect(self.onValueChange)
        # the usage of connect in qt4, like connect in c++
        # self.connect(self.slider, QtCore.SIGNAL('valueChanged(int)'), self, QtCore.SLOT('onValueChange(int)'))
        # there is also a key point, signal.the format to declaration a signal is trigger = pyqtSignal(type)


    @QtCore.pyqtSlot(int)
    def onValueChange(self, value):
        self.edit.setText(str(value))


app = QtWidgets.QApplication(sys.argv)
qb = Boxlayout()
qb.show()
sys.exit(app.exec_())
