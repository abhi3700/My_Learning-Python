# xlwings Commands
<p align="center">
  <img src="http://pbpython.com/images/article-overview.png" alt="xlwings_infographics" width="550" height="200">
</p>

## [Installation](https://github.com/abhi3700/My_learning-Python/blob/master/excel.md#installation)

## Header
* `import xlwings as xw`
* `from xlwings import Range, Book`

## Book
* Calling current book:
  - `wb = xw.Book.Caller()`
* Calling a book by full name:
  - `wb = xw.Book(r'C:/path/to/file.xlsx')`
> NOTE: When specifying file paths on Windows, you should either use raw strings by putting an r in front of the string or use double back-slashes like so: C:\\path\\to\\file.xlsx.
* [Official link](https://docs.xlwings.org/en/stable/connect_to_workbook.html#python-to-excel)

## Sheet
* Add a sheet named 'main' after 'Sheet1': 
  - `wb.sheets.add('main', after = 'Sheet1')`
* Add a sheet named 'pre' before 'Sheet1':
  - `wb.sheets.add('pre', before = 'Sheet1')`

## Cell, Row, Column
* single cell with a value: 
  - `wb.sheets[0].range('A1').value = "abhijit"` or 
  - `wb.sheets['Sheet1'].range('A1').value = "abhijit"` 
* multiple cells with values:
  - `wb.sheets[0].range('A1:B2').value = "abhijit"` or 
  - `wb.sheets['Sheet1'].range('A1:B2').value = "abhijit"`
* color cell(s):
  - `wb.sheets[0].range('A1').color = (0, 255, 0)` or 
  - `wb.sheets['Sheet1'].range('A1').color = (0, 255, 0)`
* color cell as None (no color):
  - `sht.range('D31').color = None`
* Autofit column
  - `sht_pr.range('A1:A10').columns.autofit()   # sht_pr - name of a 'practice' sheet`
* Autofit table from 'A1' to 'Z1600'
  - `sht_prod.range('A1:Z1600').columns.autofit()`
  
## Date, time
* Current datetime
  ```py
  import datetime as dt
  dt.datetime.now()
  ```
* datetime notation [Refer this](http://strftime.org/)
  ```py
  import datetime as dt
  curr_dt = dt.datetime.now()
  print(curr_dt.strftime("%A"))
  ```


## Macro
* Create python User-defined functions (UDFs): <br/>
  Steps:
  - Open `.py` file (created during a project quickstart using xlwings)
  - Follow this code sample to create your UDFs:
  ```py
  @xw.func
  def sumtwice(x, y):
    return 2 * (x + y)
  ```
  - Press this button <kbd>"Import Functions"</kbd> in the `xlwings` tab in Excel Book. Here, if found error in dialog box, enable <kbd>Trust access to the VBA project object model</kbd> button in the `Trust Center >> Developer Macro Settings`
  - Now access the UDFs from inside a cell.
  - DONE!!

## Plot

## Pandas
* import pandas:
  - `import pandas as pd`

## Database
* Import sqlalchemy (can be used with postgreSQL, NoSQL, MongoDB, etc.):
  - `from sqlalchemy import create_engine`

## References
* Interactive Data Analysis with Python and Excel - http://pbpython.com/xlwings-pandas-excel.html
