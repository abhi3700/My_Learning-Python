class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")
        
        widget = QLabel("Hello")
        widget.setPixmap( QPixmap("hrh.jpg") )
        widget.setScaledContents(True)
        
        self.setCentralWidget(widget)

