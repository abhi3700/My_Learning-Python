# Dash

## Installation
Steps:
1. Open __Anaconda command prompt_.
2. `pip install dash==0.39.0` [Refer for latest](https://dash.plot.ly/installation)
3. DONE!

## Getting Started
* Create a `.py` file in ST3.
* Build using Anaconda Compiler inside ST3 (provided Anaconda is installed in ST3) using `Tools >> Build System >> Anaconda Python Builder` and then <kbd>ctrl + b</kbd> to build the `.py` file.
	<p align="center">
	  <img src="./libs/Dash/images/console.png" alt="console Image" width="" height="">
	</p>
> Note: If the console is pressed (by mistake) with <kbd>ESC</kbd> button, then just <kbd>ctrl + b</kbd> to bring it again.
* Open the http url by selecting the http url in console. It is shown below:	
	<p align="center">
	  <img src="./libs/Dash/images/console_open_url.png" alt="console_open_url Image" width="" height="">
	</p>

## Utility
* #### Network ports
	- Show all ports using `netstat -a -o -n`
	- Kill a port using `taskkill /F /PID 28344`

* #### Upload and Download files to/from Dash - [Refer this](https://docs.faculty.ai/user-guide/apps/examples/dash_file_upload_download.html)
* #### Convert into a Package for distribution (to users)
	Steps (all will be available in a batch file):
	- Install Python
	- Install pip
	- Install a list of Dash packages (used in your project) using `pip install -r requirements.txt`
	- Open the server (with `app.py` file) in your browser using `python app.py`

