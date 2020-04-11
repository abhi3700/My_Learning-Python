class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")
        
        label = QLabel("THIS IS AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)





