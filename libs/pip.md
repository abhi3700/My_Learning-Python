# Pip

## Installation

For macOS, install `pip` using `python`:

```sh
python get-pip.py
```

| NOTE | Ensure `python` is `python3`, else use `python3` instead of `python`. |
| --- | --- |

- Upgrade all installed packages via `pip`:

```sh
# outputs the list of installed packages
pip freeze > requirements.txt

# After this, replace "==" with ">=" in the file.

# updates all packages
pip install -r requirements.txt --upgrade
```

## Usage

> Some of the commands might be valid for Windows. So, apply your due diligence.

- Install Package at a custom location using `pip install <package> -t <directory>`. <br/>
  e.g. `pip install XlsxWriter -t F:\Softwares\Python\Python37\Lib`
- Install a specific version of a package: `pip install xlwings==0.15.7`
- Install a min. version of a package: `pip install xlwings>=0.15.7`
- Install a min. & max. version of a package: `pip install "xlwings>=0.15.7,<0.16.0"`
- Upgrade an existing package: `pip install <package-name> -U`
- Install list of packages at once:
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
    - Open Anaconda prompt
    - type `pip install -r requirements.txt` and enter
    - Otherwise, type `pip install -r requirements.txt` and enter in the command prompt.
- Install offline package
  - Download in `-.tar.gz` | `-.whl` format. E.g.- __package.tar.gz__, __package.whl__
  - `pip install package.tar.gz` (in default directory)
  - `pip install package.tar.gz -t 'F:\Softwares\Python\Python37\Lib'` (in preferred directory)

## Troubleshooting

### 1. SSL Error

SSL Error: add trusted sites to pip's config file like this:

- M-I:

```sh
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org excalibur-py
```

- M-II:

  - locate the `pip.ini` file using

```sh
$ pip config list -v
For variant 'global', will try loading 'C:\ProgramData\pip\pip.ini'
For variant 'user', will try loading 'C:\Users\Abhijitroy\pip\pip.ini'
For variant 'user', will try loading 'C:\Users\Abhijitroy\AppData\Roaming\pip\pip.ini'
```

- create file correspondingly for __global__ or __user__ level and then feed this:

```sh
[global]
trusted-host = pypi.python.org
              pypi.org
              files.pythonhosted.org
```
