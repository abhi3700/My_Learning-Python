class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")


        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.East)
        tabs.setMovable(True)

        for n, color in enumerate(['red','green','blue','yellow']):
            tabs.addTab( Color(color), color)

        self.setCentralWidget(tabs)
