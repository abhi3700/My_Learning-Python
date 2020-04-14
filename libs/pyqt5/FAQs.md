# PyQt5 FAQs
* #### `app.exec()` vs `app.exec_()` ?
	- both valid for PyQt5 & older PyQt (earlier versions i.e. <= 4)
	- Conclusion: Maintain a single codebase for PyQt5 using `app.exec()`

* #### `sys.exit(app.exec())` vs `app.exec()` ?
	- The `exec()` call starts the event-loop and will block until the application quits.
	- It is good practice to pass on this exit code to `sys.exit()` - but it is not strictly necessary.
	- Without the explicit call to `sys.exit()`, the script will automatically exit with a code of 0 after the last line of code has been executed.
	- A non-zero exit code is usually used to inform the calling process that an error occurred.
	- By convention, a returnCode of 0 means success, and any non-zero value indicates an error.