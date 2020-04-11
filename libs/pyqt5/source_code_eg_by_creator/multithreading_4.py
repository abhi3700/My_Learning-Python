class Worker(QRunnable):
    '''
    Worker thread

    :param fn: The function to be executed
    :param args: Arguments to make available to the run code
    :param kwargs: Keywords arguments to make available to the run
    :code
    :
    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        '''
        Execute the runner function with passed self.args,
        self.kwargs.
        '''
        self.fn(args, kwargs)