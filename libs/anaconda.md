# Anaconda

## Installation
* https://www.anaconda.com/
* tick the checkbox corresponding to "Add to path". This will enable using `conda` in the terminal.

## Shortcuts
* Open Jupyter notebook using `$ jupyter notebook` on terminal (win 10) in a preferable directory.
  E.g.:
  - goto "F:\Coding\jupyter-notebook"
  - open cmd here
  - type `jupyter notebook` on terminal.
* All the packages installed using conda present in this directory - `"F:\Softwares\Anaconda3\Lib\site-packages"`
* Various environments created inside conda are present in this directory - `"F:\Softwares\Anaconda3\envs"`
* JUPYTER NOTEBOOK shortcut keys - 
  https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/
* <kbd>D + D</kbd> - to delete cell
* <kbd>A</kbd> - add a cell above selected cell
* <kbd>B</kbd> - add a cell below selected cell
* <kbd>M</kbd> - cell as **Markdown**.
* <kbd>shift + enter</kbd> - to run the cell and goto the next cell below.
* To import `beautifulsoup` package, use this - `import bs4`, NOT this - ~`import beautifulsoup4`~

## Conda
* `conda list` - shows the list of packages installed
* `conda list --revisions` - shows the revisions of the installation since first installation.
  ```
  2019-01-30 17:14:43  (rev 4)
     beautifulsoup4  {4.6.0 -> 4.7.1}
    +soupsieve-1.7.1

  2019-02-07 20:57:34  (rev 5)
     ca-certificates  {2018.12.5 -> 2019.1.23}
     conda  {4.6.1 -> 4.6.2}
     pandas  {0.20.3 -> 0.24.1}

  2019-02-08 19:26:01  (rev 6)
     pandas  {0.24.1 -> 0.20.3}
  ```
* ##### `conda install pandas=0.20.3` - install a specific version of a package
* #### install/uninstall packages using internet with a proxy 
  Follow this steps: <br/>
  - `> conda config` - would create a file: `.condarc` in directory - "C:\Users\abhijit"
  - write the snippet following [YAML](http://www.yamllint.com/) syntax
  ```yaml
  # Proxy settings: http://[username]:[password]@[server]:[port]
  proxy_servers:
  http: http://abhijit:CL00102@192.9.200.22:8080
  https: http://abhijit:CL00102@192.9.200.22:8080
  ```
* ##### `conda info -e`: List all Environments inside Anaconda(Installaed): 

* ##### `conda create -n <yourenvname> python=<x.x> anaconda`: Create a Virtual Environment 
* ##### `source activate <yourenvname>`: Activate virtual environment. Do this before installing packages.
* ##### `source deactivate`: Deactivate virtual environment. Do this after installing packages.
* ##### `conda install -n <yourenvname> [package]`: Install package(s) in virtual environment.
* ##### `conda remove -n yourenvname -all`: Delete a no longer needed virtual environment.
* SSL Error:
  ```console
  Solving environment: failed

  CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/r/noarch/repodata.json.bz2>
  Elapsed: -

  An HTTP error occurred when trying to retrieve this URL.
  HTTP errors are often intermittent, and a simple retry will get you on your way.

  If your current network has https://www.anaconda.com blocked, please file
  a support request with your network engineering team.

  SSLError(MaxRetryError('HTTPSConnectionPool(host=\'repo.anaconda.com\', port=443): Max retries exceeded with url: /pkgs/r/noarch/repodata.json.bz2 (Caused by SSLError(SSLError("bad handshake: Error([(\'SSL routines\', \'tls_process_server_certificate\', \'certificate verify failed\')])")))'))
  ```
  
  __Solution:__
  Do this on Anaconda prompt - `conda config --set ssl_verify no`
  > Warning: Note that this opens you up to some pretty serious attacks.
  
## Packages
#### NOTE: all packages here are not installed by default
* **Html2Text** 
  - M-1: https://anaconda.org/akode/html2text [NOT Successful]
  - M-2: Install using `pip` in conda environment
    + On Windows, open "Anaconda Prompt"
    + `> pip install html2text`
    + Now, check if `html2text` package is installed: try `conda list` on same/separate terminal.
    + DONE!
* **PLotly** - https://anaconda.org/plotly/plotly
* **conda-env**
  - conda env export lists all conda and pip packages in an environment. `conda-env` must be installed in the conda root (`conda install -c conda conda-env`).
