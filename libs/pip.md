# Pip
## Installation
* `conda install pip`

## Notes
* Install Package at a custom location using `pip install <package> -t <directory>`. <br/>
  e.g. `pip install XlsxWriter -t F:\Softwares\Python\Python37\Lib`
* Install a specific version of a package: `pip install xlwings==0.15.7`
* Install list of packages at once:
	Steps:
	- create a file - `requirements.txt` <br/>
		E.g. 
		```txt
		dash
		plotly
		matplotlib
		pandas
		numpy
		```
	- For Anaconda environment:
		+ Open Anaconda prompt
		+ type `pip install -r requirements.txt` and enter
	- Otherwise, type `pip install -r requirements.txt` and enter in the command prompt.
* Install offline package 
	- Download in `*.tar.gz` | `*.whl` format. E.g.- __package.tar.gz__, __package.whl__
	- `pip install package.tar.gz` (in default directory)
	- `pip install package.tar.gz -t 'F:\Softwares\Python\Python37\Lib'` (in preferred directory)
