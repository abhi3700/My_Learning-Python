class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        # QHBoxLayout is a horizontally stacking layout with new widgets
        # added to the right of previous widgets.
        layout = QVBoxLayout()
        
        for n in range(10):
            # Create a push button labeled with the loop number 0-9
            btn = QPushButton(str(n))
            # SIGNAL: The .pressed signal fires whenever the button is pressed.
            # We connect this to self.my_custom_fn via a lambda to pass in
            # additional data.
            # IMPORTANT: You must pass the additional data in as a named 
            # parameter on the lambda to create a new namespace. Otherwise
            # the value of n will be bound to the final value in the parent
            # for loop (always 9).
            btn.pressed.connect( lambda n=n: self.my_custom_fn(n) )
 
            # Add the button to the layout. It will go to the right by default.
            layout.addWidget(btn)
        
        # Create a empty widget to hold the layout containing our buttons.
        widget = QWidget()
        
        # Set the layout containing our buttons onto the blank widget. We only
        # need to do this here because we can't set a layout on a QMainWindow.
        # So instead we're setting a layout on a widget, and then adding that 
        # widget to the window(!)
        widget.setLayout(layout)
        
        self.setCentralWidget(widget)
        

    # SLOT: This function will receive the single value passed from the signal
    def my_custom_fn(self, n):
        print("Button %d was clicked" % n)      
