import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    l1 = QtWidgets.QLabel(w)
    l2 = QtWidgets.QLabel(w)
    l1.setText('Hello World')
    l2.setPixmap(QtGui.QPixmap('globe.png'))
    w.setWindowTitle('PyQt Lesson 2')
    w.setGeometry(1400, 1000, 600, 600)
    l1.move(250, 20)
    l2.move(250, 50)
    w.show()
    sys.exit(app.exec_())

window()
