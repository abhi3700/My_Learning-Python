# PyQt5 FAQs
* #### `app.exec()` vs `app.exec_()` ?
	- both valid for PyQt5 & older PyQt (earlier versions i.e. <= 4)
	- Conclusion: Maintain a single codebase for PyQt5 using `app.exec()`