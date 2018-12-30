# xlwings Commands

## Header
* `import xlwings as xw`
* `from xlwings import Range, Book`

## Book
* Calling current book:
  - `wb = xw.Book.Caller()` 

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

