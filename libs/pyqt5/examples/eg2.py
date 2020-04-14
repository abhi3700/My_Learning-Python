import sys
from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("eg2.ui")
window.show()
app.exec()
