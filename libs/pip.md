# Pip
## Installation
* `conda install pip`

## Notes
* **Package**: Install at a custom location using `pip install <package> -t <directory>`. <br/>
  e.g. `pip install XlsxWriter -t F:\Softwares\Python\Python37\Lib`
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

