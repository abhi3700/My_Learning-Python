class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")
        
        widget = QSpinBox()
        # Or: widget = QDoubleSpinBox()
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # Or: widget.setRange(-10,3)
        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3) # Or e.g. 0.5 for QDoubleSpinBox
        widget.valueChanged.connect(self.value_changed)
        widget.valueChanged[str].connect(self.value_changed_str)
        
        self.setCentralWidget(widget)
        
        
    def value_changed(self, i):
        print(i)
        
    def value_changed_str(self, s):
        print(s)

