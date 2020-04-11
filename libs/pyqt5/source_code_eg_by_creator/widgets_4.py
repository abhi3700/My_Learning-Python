class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")
        
        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        # The default signal from currentIndexChanged sends the index
        widget.currentIndexChanged.connect( self.index_changed )
        
        # The same signal can send a text string
        widget.currentIndexChanged[str].connect( self.text_changed )

        self.setCentralWidget(widget)


    def index_changed(self, i): # i is an int
        print(i)
        
    def text_changed(self, s): # s is a str
        print(s)
