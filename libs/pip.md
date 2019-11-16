# Pip
## Installation
* `conda install pip`
* Upgrade - `pip install --upgrade pip`

## Notes
* Install Package at a custom location using `pip install <package> -t <directory>`. <br/>
  e.g. `pip install XlsxWriter -t F:\Softwares\Python\Python37\Lib`
* Install a specific version of a package: `pip install xlwings==0.15.7`
* Upgrade an existing package: `pip install <package-name> -U`
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
* Troubleshooting SSL Error: add trusted sites to pip's config file like this
	- M-I:
```console
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org excalibur-py
```
	- M-II:
		+ locate the `pip.ini` file using
```console
$ pip config list -v
For variant 'global', will try loading 'C:\ProgramData\pip\pip.ini'
For variant 'user', will try loading 'C:\Users\Abhijitroy\pip\pip.ini'
For variant 'user', will try loading 'C:\Users\Abhijitroy\AppData\Roaming\pip\pip.ini'
```
		+ create file correspondingly for __global__ or __user__ level and then feed this:
```console
[global]
trusted-host = pypi.python.org
               pypi.org
               files.pythonhosted.org
```	