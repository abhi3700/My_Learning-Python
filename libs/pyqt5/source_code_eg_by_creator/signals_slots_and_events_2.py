from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        layout = QVBoxLayout()
        
        for n in range(10):
            btn = QPushButton(str(n))
            btn.pressed.connect( lambda: self.my_custom_fn(n) )
 
            layout.addWidget(btn)
        
        widget = QWidget()
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        
    def my_custom_fn(self, n):
        print("Button %d was clicked" % n)      


app = QApplication([])

window = MainWindow()
window.show()
app.exec_()






