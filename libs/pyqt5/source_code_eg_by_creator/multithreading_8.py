def execute_this_fn(self):
    for n in range(0, 5):
        time.sleep(1)
    return "Done."

def print_output(self, s):
    print(s)

def thread_complete(self):
    print("THREAD COMPLETE!")

def oh_no(self):
    # Pass the function to execute
    worker = Worker(self.execute_this_fn) # Any other args, kwargs are passed to the run function
    worker.signals.result.connect(self.print_output)
    worker.signals.finished.connect(self.thread_complete)

    # Execute
    self.threadpool.start(worker)