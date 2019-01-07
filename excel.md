# Excel

## Installation
* **Tools:** ST3, xlwings, conda
* Steps:
  - `$ conda install xlwings`
  - `$ xlwings quickstart <project-name>`: start a excel with python project. E.g. `$ xlwings quickstart abhi`
  - `$ xlwings addin install`: install xlwings into excel. If needs to upgrade, then use `$ xlwings addin upgrade`.
  - Enable macro settings in the MS Excel
    + enable <kbd>Enable all macros</kbd> button in the `Trust Center >> Macro Settings >> Macro Settings`
    + enable <kbd>Trust access to the VBA project object model</kbd> button in the `Trust Center >> Macro Settings >> Developer Macro Settings`

## Projects
* ### Hello:
  This prints text - "Hello xlwings!" into A1 cell in sheet 1 of the workbook.
  
  **Steps:**
  - `$ xlwings quickstart abhi` in any preferable directory. It gives:

    ```bash
    .
    ├── abhi.py
    ├── abhi.xlsm
    ```
  - goto `"Developer"` tab in excel.
  - goto "Module1" and run.
  - It shows the output.

## Shortcut keys
* <kbd>ctrl + backspace</kbd> - bring the cursor near the word, you get to see the dialog with its features. <br/>
  NOTE: Anaconda package in ST3 has to be installed first.
  
## Commands, Syntax
* [Refer this file](https://github.com/abhi3700/My_learning-Python/blob/master/xlwings_commands.md)

## References
* xlwings - https://www.xlwings.org/
* Common Excel Tasks Demonstrated in Pandas - http://pbpython.com/excel-pandas-comp.html
* Common Excel Tasks Demonstrated in Pandas part 2 - http://pbpython.com/excel-pandas-comp-2.html
* Combining Data From Multiple Excel Files - http://pbpython.com/excel-file-combine.html
* Generating Excel Reports from a Pandas Pivot Table - http://pbpython.com/pandas-pivot-report.html
* Improving Pandas’s Excel Output - http://pbpython.com/improve-pandas-excel-output.html
* Creating Advanced Excel Workbooks with Python - http://pbpython.com/advanced-excel-workbooks.htmlCreating Advanced Excel Workbooks with Python - 
