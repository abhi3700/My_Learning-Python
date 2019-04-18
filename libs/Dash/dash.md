# Dash

## Installation
In Dash, following packages are installed:
* dash
* dash-core-components
* dash-html-components
* dash-renderer
* dash-table
* flask-compress

### M-1:
1. Open __Anaconda command prompt__.
2. `pip install dash==0.39.0` [Refer for latest](https://dash.plot.ly/installation)
3. DONE!
### M-2:
1. Open __Anaconda command prompt__
2. Type `conda install -c conda-forge dash` and enter.
	```console
	The following packages will be downloaded:

			package                    |            build
			---------------------------|-----------------
			conda-4.6.13               |           py37_0         2.1 MB  conda-forge
			dash-0.41.0                |             py_0          39 KB  conda-forge
			dash-core-components-0.46.0|             py_0         3.6 MB  conda-forge
			dash-html-components-0.15.0|             py_0         334 KB  conda-forge
			dash-renderer-0.22.0       |             py_0         719 KB  conda-forge
			dash-table-3.6.0           |             py_0         410 KB  conda-forge
			flask-compress-1.4.0       |             py_0           6 KB  conda-forge
			------------------------------------------------------------
																						 Total:         7.1 MB

	The following NEW packages will be INSTALLED:

		dash               conda-forge/noarch::dash-0.41.0-py_0
		dash-core-compone~ conda-forge/noarch::dash-core-components-0.46.0-py_0
		dash-html-compone~ conda-forge/noarch::dash-html-components-0.15.0-py_0
		dash-renderer      conda-forge/noarch::dash-renderer-0.22.0-py_0
		dash-table         conda-forge/noarch::dash-table-3.6.0-py_0
		flask-compress     conda-forge/noarch::flask-compress-1.4.0-py_0
	```
## Utility
* #### Upload and Download files to/from Dash - [Refer this](https://docs.faculty.ai/user-guide/apps/examples/dash_file_upload_download.html)
* #### Convert into a Package for distribution (to users)
	Steps (all will be available in a batch file):
	- Install Python
	- Install pip
	- Install a list of Dash packages (used in your project) using `pip install -r requirements.txt`
	- Open the server (with `app.py` file) in your browser using `python app.py`
* 
