# xlwings Commands

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

## Cell
* single cell with a value:
  - `Range('A1').value = "abhijit"` or 
  - `wb.sheets[0].range('A1').value = "abhijit"` or 
  - `wb.sheets['Sheet1'].range('A1').value = "abhijit"` 
* multiple cells with values:
  - `Range('A1:B2').value = "abhijit"`  or 
  - `wb.sheets[0].range('A1:B2').value = "abhijit"` or 
  - `wb.sheets['Sheet1'].range('A1:B2').value = "abhijit"`

