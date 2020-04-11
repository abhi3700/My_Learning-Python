from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    progress
        int progress complete,from 0-100
    '''
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals
    and wrap-up.
    '''

    def __init__(self):
        super(Worker, self).__init__()

        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        total_n = 1000
        for n in range(total_n):
            progress_pc = int(100*float(n)/total_n)  # Progress 0-100% as int
            self.signals.progress.emit(progress_pc)
            time.sleep(0.01)


class MainWindow(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        layout = QVBoxLayout()

        self.bar = QProgressBar()

        button = QPushButton("START IT UP")
        button.pressed.connect(self.execute)

        layout.addWidget(self.bar)
        layout.addWidget(button)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def execute(self):
        worker = Worker()
        worker.signals.progress.connect(self.update_progress)

        # Execute
        self.threadpool.start(worker)

    def update_progress(self, progress):
        self.bar.setValue(progress)



app = QApplication([])
window = MainWindow()
app.exec_()
