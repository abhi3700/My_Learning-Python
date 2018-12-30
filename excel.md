# Excel

## Installation
* **Tools:** ST3, xlwings, conda
* Steps:
  - `$ conda install xlwings`
  - `$ xlwings quickstart <project-name>`: start a excel with python project. E.g. `$ xlwings quickstart abhi`
  - `$ xlwings addin install`: install xlwings into excel

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


## References
* xlwings - https://www.xlwings.org/
