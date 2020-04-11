class MainWindow(QMainWindow):

    # def __init__ etc.
    # ... not shown for clarity

    def onMyToolBarButtonClick(self, s):
        print("click", s)
        
        
        dlg = QDialog(self)
        dlg.setWindowTitle("HELLO!")
        dlg.exec_()
        
