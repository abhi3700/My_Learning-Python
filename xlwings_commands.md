# xlwings Commands
<p align="center">
  <img src="http://pbpython.com/images/article-overview.png" alt="xlwings_infographics" width="550" height="200">
</p>

## [Installation](https://github.com/abhi3700/My_learning-Python/blob/master/excel.md#installation)

## Troubleshooting
* Sometimes, when Excel (in 2016 version) macros may not run (while the excel is open) on pressing <kbd>F5</kbd>, then try using this:
```vba
Private Sub Workbook_Open()
		mymodule = Left(ThisWorkbook.name, (InStrRev(ThisWorkbook.name, ".", -1, vbTextCompare) - 1))
		RunPython ("import " & mymodule & ";" & mymodule & ".main()")
End Sub
```
instead of the default code during project generation
```vba
Sub SampleCall()
		mymodule = Left(ThisWorkbook.Name, (InStrRev(ThisWorkbook.Name, ".", -1, vbTextCompare) - 1))
		RunPython ("import " & mymodule & ";" & mymodule & ".hello_xlwings()")
End Sub
```
	> Note: Basically, one should use module name as `Workbook_Open()`
	
* If the `xlwings` tab doesn't appear in Excel, then there might be version incompatibility like 
	- Latest `Excel` with older `Python` version
	- Latest `Python` version with older `Excel`
	
	Also, Anaconda version incompatibility might be the issue. 
	> Try using latest versions of all the tools, Latest Anaconda => Python is the latest, also, xlwings is the latest as well.
* If there is any error like this:
	```
	Error 440:
	Automation error
	```
	**Meaning:**
	Check if any variable/function created and referenced to any sheet, which exists or not.	
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

## File
* Read excel file and copy its sheet into current workbook's sheet. <br/>
	**Code:**
```py
excel_file = pd.ExcelFile("H:\\excel\\dryetch\\macro_enabled_logbooks\\ASH09_QC_LOG_BOOK\\ASH09_QC_LOG_BOOK.xlsm")
df1 = excel_file.parse('ASFE1-ER')
sht.range('A1').options(index=False).value = df1
```

#### Description:
	- While pasting, start cell: A1
	- Copying the sheet of an Excel file into current workbook's desired sheet


## Cell, Row, Column
* single cell with a value: 
  - `wb.sheets[0].range('A1').value = "abhijit"` or 
  - `wb.sheets['Sheet1'].range('A1').value = "abhijit"` 
* multiple cells with values:
  - `wb.sheets[0].range('A1:B2').value = "abhijit"` or 
  - `wb.sheets['Sheet1'].range('A1:B2').value = "abhijit"`
* set color cell(s):
  - `wb.sheets[0].range('A1').color = (0, 255, 0)` or 
  - `wb.sheets['Sheet1'].range('A1').color = (0, 255, 0)`
* set color cell as None (no color):
  - `sht.range('D31').color = None`
* get color cell
  ```py
  if sht_prod.range('A2').color == (153, 204, 0):
		sht_prod.range('C3').value = "Light Green"
  ```
* get color cell as None
  ```py
  if sht_prod.range('A2').color is None:
		sht_prod.range('C3').value = "No color"
  ```
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
## Display, Message, Alert
* [MessageBox](http://docs.activestate.com/activepython/2.4/pywin32/win32api__MessageBox_meth.html)
```py
import xlwings as xw
import win32api
wb = xw.Book.caller()
win32api.MessageBox(wb.app.hwnd, "display message", "Title", )
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
* printing w/o index column
```py
df = pd.read_csv('H:\\excel\\abhi\\countries.csv')
sht_countries = wb.sheets['countries_data']
# sht_countries.range('A1').value = df		# printing with index col.
sht_countries.range('A1').options(index= False).value = df 		# printing w/o index col.
```
> NOTE: here the data starts with 'A1' cell

## Database
* Import sqlalchemy (can be used with postgreSQL, NoSQL, MongoDB, etc.):
  - `from sqlalchemy import create_engine`

## References
* Interactive Data Analysis with Python and Excel - http://pbpython.com/xlwings-pandas-excel.html
