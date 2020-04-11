def execute_this_fn(self):
    print("Hello!")

def oh_no(self):
    # Pass the function to execute
    worker = Worker(self.execute_this_fn) # Any other args, kwargs are passed to the run function

    # Execute
    threadpool.start(worker)