# xlwings Commands

![](../../img/xlwings_infographics.png)

## [Installation](https://github.com/abhi3700/My_Learning-Python/blob/master/libs/xlwings/xlwings.md#installation)

## Troubleshooting

- Sometimes, when Excel (in 2016 version) macros may not run (while the excel is open) on pressing <kbd>F5</kbd>, then try using this:

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

- If the `xlwings` tab doesn't appear in Excel, then there might be version incompatibility like

  - Latest `Excel` with older `Python` version
  - Latest `Python` version with older `Excel`

  Also, Anaconda version incompatibility might be the issue.

  > Try using latest versions of all the tools, Latest Anaconda => Python is the latest, also, xlwings is the latest as well.

- If there is any error like this:
  ```
  Error 440:
  Automation error
  ```
  **Meaning:**
  Check if any variable/function created and referenced to any sheet, which exists or not.
- If any error like this - `exceeds Locator.MAXTICKS`:
  - In case of date-axis, check if any date is wrongly enterred like 1906 in range-> (2016-2018)
  - FYI, the locator.maxticks == 1000
  - Define a new, if required:

```py
import matplotlib.ticker as mticker
mticker.Locator.MAXTICKS = 2000		# set max ticks
```

- If any error like this

```py
---------------------------
Error
---------------------------
Traceback (most recent call last):

  File "<string>", line 1, in <module>

  File "i:\github_repos\autoplot\examples\dry_etch\ash09_qc_log_book\ASH09_QC_LOG_BOOK.py", line 245, in button_run

    wb, sht_asfe1_cp, sht_asfe1_er, sht_run, x_coord_pr, y_coord_pr, excel_file = init()

  File "i:\github_repos\autoplot\examples\dry_etch\ash09_qc_log_book\ASH09_QC_LOG_BOOK.py", line 239, in init

    excel_file = pd.ExcelFile(excel_file_directory)

  File "F:\Softwares\Anaconda3\lib\site-packages\pandas\io\excel\_base.py", line 821, in __init__

    self._reader = self._engines[engine](self._io)

  File "F:\Softwares\Anaconda3\lib\site-packages\pandas\io\excel\_xlrd.py", line 21, in __init__

    super().__init__(filepath_or_buffer)

  File "F:\Softwares\Anaconda3\lib\site-packages\pandas\io\excel\_base.py", line 353, in __init__

    self.book = self.load_workbook(filepath_or_buffer)

  File "F:\Softwares\Anaconda3\lib\site-packages\pandas\io\excel\_xlrd.py", line 36, in load_workbook

    return open_workbook(filepath_or_buffer)

  File "F:\Softwares\Anaconda3\lib\site-packages\xlrd\__init__.py", line 111, in open_workbook

    with open(filename, "rb") as f:

FileNotFoundError: [Errno 2] No such file or directory: 'ASH09_QC_LOG_BOOK.xlsm'



Press Ctrl+C to copy this message to the clipboard.
---------------------------
OK
---------------------------
```

**Solution:** Don't use relative path. Always use absolute path for the buttons (inside Excel) to work properly.

```md
Just redefine the **excel_file_directory**
FROM
excel_file_directory = "ASH09_QC_LOG_BOOK.xlsm"
TO
excel_file_directory = "I:\\github_repos\\AutoPlot\\examples\\dry_etch\\ASH09_QC_LOG_BOOK\\ASH09_QC_LOG_BOOK.xlsm"
```

## Header

- `import xlwings as xw`
- `from xlwings import Range, Book`

## Book

- ### Create (& open) an Excel file:
  ```py
  import xlwings as xw
  wb = xw.Book()
  wb.save('test.xlsx')
  ```
- ### Read an Excel file:
  ```py
  import xlwings as xw
  wbtest = xw.Book('test.xlsx')
  ```
- ### Calling current book:
  - `wb = xw.Book.Caller()`
- ### Calling a book by full name:
  - `wb = xw.Book(r'C:/path/to/file.xlsx')`
    > NOTE: When specifying file paths on Windows, you should either use raw strings by putting an r in front of the string or use double back-slashes like so: C:\\path\\to\\file.xlsx.
- [Official link](https://docs.xlwings.org/en/stable/connect_to_workbook.html#python-to-excel)
- From `v0.16.0` version onwards, the python function can be build using **M-1: <kbd>ctrl+b</kbd> in ST3 editor** or **M-2:using the <kbd>RUN</kbd> button inside Excel**.

```py
def button_run():
    # Fetch Dataframe for CP Plot
    df_repl1a_cp = sht_repl1a_cp.range('A9').options(
        pd.DataFrame, header=1, index=False, expand='table'
        ).value                                                         # fetch the data from sheet- 'ASBE1-CP'
    df_repl1a_cp['Remarks'].fillna('..', inplace=True)        # replacing the empty cells with 'NIL'


if __name__ == "__main__":
    button_run()
```

- In order to create an User Interface (UI) into an Excel, just add a <kbd>RUN</kbd> button via adding an Active button from **Developer** Tab. And then execute python macro using either of the 2 methods:

  - M-1: this is for updating the charts in the same folder.

    - 1. Create a `run.bat` file and add this code:

    ```bat
    Sub RUN_Click()
      Shell "cmd.exe /k cd /d" & ThisWorkbook.Path & "&& run.bat" & "&& exit"
    End Sub
    ```

    - 2. Now, there will be no progress circle shown in the excel. Instead, a CMD terminal opens up and shows the status - **ERROR** or **NO ERROR**.

    > NOTE: Demerit: Doesn't work for fetching files from local network (due to **UNIX** directory not compatible in **Windows**). In this situation tried with `os`, `shutil`, `getpass` packages, but couldn't copy & replace the files. Inherently incompatible due to **Windows** - **UNIX**. But when it was run with <kbd>ctrl+b</kbd> inside **ST3**, then the copy, replace happened. This implies that there is some incompatibility issue of **DOS-UNIX**.

  - M-2: Use it especially when there is no chart creation.

  ```bat
  Sub RUN_Click()
    mymodule = Left(ThisWorkbook.Name, (InStrRev(ThisWorkbook.Name, ".", -1, vbTextCompare) - 1))
    RunPython ("import " & mymodule & ";" & mymodule & ".button_run()")
  End Sub
  ```

  In this case, in order to update the charts,

  - M-1: create `run.sh` for any file location (local PC or local network). [RECOMMENDED]

  ```bash
  python CNT01_Ch_A_QC_LOG_BOOK.py
  tskill excel
  ```

  > NOTE: Here, `tskill excel` command has been used for closing the excel file while running from `run.sh` file created in the same directory.

  - M-2: create `run.bat` for any files in local PC.

## Sheet

- ### Add a sheet named 'main' after 'Sheet1':
  - `wb.sheets.add('main', after = 'Sheet1')`
- ### Add a sheet named 'pre' before 'Sheet1':
  - `wb.sheets.add('pre', before = 'Sheet1')`
- ### Delete a sheet

```py
import xlwings as xw
wbtest = xw.Book('QT-2019 ACTION FLOW SUPPLY.xlsx')
wbtest.sheets.add('main', after= 'Customers')

# delete sheet - 'main'
for sht in wbtest.sheets:
    if 'main' in sht.name:
        sht.delete()
```

## File

- ### Read excel file and copy its sheet into current workbook's sheet.
  **Code:**

```py
excel_file = pd.ExcelFile("H:\\excel\\dryetch\\macro_enabled_logbooks\\ASH09_QC_LOG_BOOK\\ASH09_QC_LOG_BOOK.xlsm")   # from a hard drive

# pull excel data from a server
excel_file = pd.ExcelFile("\\\\vmfg\\VFD FILE SERVER\\SECTIONS\\DRY ETCH\\QC Log Book\\Final QC Log Book\\ASH_09_10_LOG_BOOK\\ASH09_QC_LOG_BOOK_macro\\ASH09_QC_LOG_BOOK.xlsm")

df1 = excel_file.parse('ASFE1-ER')
sht.range('A1').options(index=False).value = df1
```

#### Description:

    - While pasting, start cell: A1
    - Copying the sheet of an Excel file into current workbook's desired sheet

## Cell, Row, Column

- ### check if cell value is empty
  - `if sht_quotation.range('I5').value is None:`
- ### single cell with a value:
  - `wb.sheets[0].range('A1').value = "abhijit"` or
  - `wb.sheets['Sheet1'].range('A1').value = "abhijit"`
- ### multiple cells with values:
  - `wb.sheets[0].range('A1:B2').value = "abhijit"` or
  - `wb.sheets['Sheet1'].range('A1:B2').value = "abhijit"`
- ### set color cell(s):
  - `wb.sheets[0].range('A1').color = (0, 255, 0)` or
  - `wb.sheets['Sheet1'].range('A1').color = (0, 255, 0)`
- ### set color cell as None (no color):
  - `sht.range('D31').color = None`
- ### get color cell
  ```py
  if sht_prod.range('A2').color == (153, 204, 0):
  	sht_prod.range('C3').value = "Light Green"
  ```
- ### get color cell as None
  ```py
  if sht_prod.range('A2').color is None:
  	sht_prod.range('C3').value = "No color"
  ```
- ### Autofit column
  - `sht_pr.range('A1:A10').columns.autofit() # sht_pr - name of a 'practice' sheet`
- ### Autofit row, column, both

```py
# define 'sht_prod' as wb.sheet['prod']
sht_prod.range('A2').autofit()  # autofit column(s) and row(s)
sht_prod.range('A2').autofit('c') # or Range('A2').autofit('columns')
sht_prod.range('A2').autofit('r') # or Range('A2').autofit('rows')
```

- ### Autofit table from 'A1' to 'Z1600'
  - `sht_prod.range('A1:Z1600').columns.autofit()`
- ### Make cell bold
  ```py
  import xlwings as xw
  wb = xw.Book()
  wb.sheets[0].range('A1').api.Font.Bold = True
  ```
- ### Change font size

```py
wb.sheets[0].range('A1').api.Font.Size = 20
```

- ### Change font (i.e. text) color

```py
wb.sheets[0].range('A1').api.Font.ColorIndex = 2
```

- ### Change font name type (calibri, arial, ...)

```py
wb.sheets[0].range('A1').api.Font.Name = "Calibri"
```

- ### Merge/Unmerge cells

```py
wb.sheets[0].range('J12:K12').api.MergeCells = True
wb.sheets[0].range('J12:K12').api.MergeCells = False
```

- ### Auto fill formula

```py
from xlwings import constants
import win32com.client as win32
wb.sheets[0].range('B1').api.AutoFill(Range('B1:B10').api, constants.AutoFillType.xlFillDefault)

# formula till last cell, create last_variable
last_cell = Range('B2:J2').current_region.last_cell.get_address(False, False)
wb.sheets[0].range('B2:J2').api.AutoFill(Range('B2:'+last_cell).api, constants.AutoFillType.xlFillDefault)
```

[Reference](https://nbviewer.jupyter.org/github/pybokeh/jupyter_notebooks/blob/master/xlwings/Excel_Formatting.ipynb#Autofill-Formula)

- ### Searching for a text

```py
for x in sht_prod.range('A1:F22'):
    if x.value == 'Found me':
        print(x.get_address())
```

- ### Conditional formatting:

```py
# Let's say we have a column containing numbers, highlight the background color if number is > 5
for x in Range('A1').vertical:
    if x.value > 5:
        x.color = (160,160,160)  # set background color to gray
```

## Date, time

- ### Current datetime
  ```py
  import datetime as dt
  dt.datetime.now()
  ```
- ### datetime notation [Refer this](http://strftime.org/)
  ```py
  import datetime as dt
  curr_dt = dt.datetime.now()
  print(curr_dt.strftime("%A"))
  ```

## Display, Message, Alert

- ### [MessageBox](http://docs.activestate.com/activepython/2.4/pywin32/win32api__MessageBox_meth.html)

```py
import xlwings as xw
import win32api
wb = xw.Book.caller()
win32api.MessageBox(wb.app.hwnd, "display message", "Title", )
```

## Protect, Unprotect

- `mysheet.api.Unprotect()`
  [Github issue](https://github.com/ZoomerAnalytics/xlwings/issues/1032)

## Macro

- ### Create python User-defined functions (UDFs): <br/>
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

- import pandas:
  - `import pandas as pd`
- ### printing w/o index column

```py
df = pd.read_csv('H:\\excel\\abhi\\countries.csv')
sht_countries = wb.sheets['countries_data']
# sht_countries.range('A1').value = df		# printing with index col.
sht_countries.range('A1').options(index= False).value = df 		# printing w/o index col.
```

> NOTE: here the data starts with 'A1' cell

## Database

- Import sqlalchemy (can be used with postgreSQL, NoSQL, MongoDB, etc.):
  - `from sqlalchemy import create_engine`

## References

- Interactive Data Analysis with Python and Excel - http://pbpython.com/xlwings-pandas-excel.html
- Jupyter notebook with xlwings functions - https://nbviewer.jupyter.org/github/pybokeh/jupyter_notebooks/blob/master/xlwings/Excel_Formatting.ipynb
