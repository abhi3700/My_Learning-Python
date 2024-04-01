# My_learning-Python

## Description

Learn Python for using in the following domains:

- Object Oriented Programming (OOP), Functional Programming (FP)
- Data Science
- Machine Learning
- Web Development
- Chatbot

## Install

### Windows (with WSL Ubuntu)

- Editor (with suggestion): Sublime Text 3 (Crack version with setup), [suggestion](#sublime-text-3-recommended-editor)
- Interpreter
  - Anaconda (on Windows)
  - Python3 (on Linux (Ubuntu)) (If required)

### Linux

- [Linux (Ubuntu)]: `sudo apt install python3`

  - And use `pip` as package manager. Install `conda` using [this](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html#installing-on-linux).

  > NOTE: Why not Anaconda in Linux?

  > - If already installed in Windows, & Linux is running on WSL. Then, try using anaconda in Windows, so that it will not add (so many approx. 600 MB of) packages additionally in the PC/Laptop.

  > - Anaconda is mainly installed because of built-in IDEs like Jupyter notebook, Spyder.

  > - Also, both `conda` & `pip` package manager comes alongwith.

- **Jupyter Notebook by Anaconda** (used mostly in debugging each module)
- **Sublime text 3** (Install conda packages after Anaconda installation) - Excel-python (with xlwings), Dash (Dashboard), Django (Web App)

> Note: It depends on the project. If it consists of multiple dependent python files, then use ST3, otherwise use Jupyter Notebook.

### macOS

1. python3 comes pre-installed in macOS via **Developer CommandLineTools**. Check using `$ python3 --version` command. Now, needs to superimpose using the python of `brew`.
   1. Using `brew`, `$ brew install python@3.11`, we can have multiple python versions: `python3.12` or `python3.11` etc.
   2. Update: `$ brew upgrade  python@3.11` to update python3.11. Similarly, `$ brew upgrade  python@3.12` for python3.12.
2. Install `pip` (aka `pip3` for some python versions > 3) using your preferred `python3` version.

  ```sh
  python3.11 -m pip install --upgrade pip
  ```

  > It is recommended to install the packages using `pip3` (not `conda`) (aka `pip`). And then check if installed using `pip3 list` or `pip list`.

  In order to know which python3 version is linked to which `pip` or `pip3`, use `$ pip --version` or `$ pip3 --version` command.

  This is the result in my case:

  ```sh
  $ which pip
  /opt/homebrew/bin/pip
  $ pip --version                                                                                                                             ⏎
  pip 24.0 from /opt/homebrew/lib/python3.11/site-packages/pip (python 3.11)

  $ which pip3
  /opt/homebrew/bin/pip3
  $ pip3 --version
  pip 24.0 from /opt/homebrew/lib/python3.12/site-packages/pip (python 3.12)
  ```

  This means `pip` is installed via `python3.11` (via brew). So, install/update via python3.11.
  
3. Project Management tool: `huak` is recommended, but `poetry` is also good, but 10x slow.

4. <u>Editor</u>: VSC (Visual Studio Code)
   - Extensions
     - Python
     - Jupyter extension packages
     - [pylyzer](https://marketplace.visualstudio.com/items?itemName=pylyzer.pylyzer)
     - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) & many others.

3. Enable Auto-complete suggestion: For enabling autocomplete suggestion, add this line in `settings.json`:

  ```json
    "python.analysis.autoImportCompletions": true,
    "python.analysis.extraPaths": ["/opt/homebrew/lib/python3.11/site-packages"]
  ```

---
  
To uninstall, follow this:

1. Open terminal on `~` directory.
2. Run `conda install anaconda-clean`
3. Run `anaconda-clean --yes`
4. Run `rm -rf ~/opt/anaconda3`
5. Close and reopen your terminal to refresh it. You should no longer see `(base)` in your terminal prompt.

## Editors

### Sublime Text 3 [DEPRECATED]

> I don't use it anymore.

- Anaconda installed & added to PATH in Windows.
- **Packages**
  - [Anaconda](https://packagecontrol.io/packages/Anaconda)
- **Build system**
  - default
- **Snippet**
  - None

### [Visual Studio Code](https://github.com/abhi3700/my_coding_toolkit/blob/main/vsc_all.md) [RECOMMENDED]

## Package managers

- [Anaconda](./libs/anaconda.md)
- [Pip](./libs/pip.md)

## Libraries

- [pandas](./libs/pandas.md)
- [xlwings](./libs/xlwings.md)
- [matplotlib](./libs/matplotlib/matplotlib.md)
- [plotly](./libs/Plotly/README.md)
- Formatter: `ruff`, `black`, `autopep8`, `yapf`

## Troubleshoot

### 1. Error while opening jupyterlab on cmd

```sh
Error executing Jupyter command 'lab': [WinError 5] Access is denied
```

- *Cause*: As the jupyterlab is not installed as Admin during the Anaconda installation. That's why need to be either followed: M-1 or M-2.
- *Solution*:
  - M-1:

  ```sh
  python3 -m jupyterlab
  ```

  - M-2:

  ```md
  step-1: open your anaconda navigator
  step-2: click on jupyter lab setting option and then remove it
  step-3: Now open your anaconda prompt and type the following command `conda install -c conda-forge jupyterlab1
  ```

### 2. moduleNotFoundError: No module named '...' on macOS

- Reason: This error is when importing package from anaconda packages on macOS. As the package is not installed in the `pip` environment, but in `conda` environment, `python3` is not able to find the package.
- Solution:
  - M-1: Install the package in `pip` environment.
  - [RECOMMENDED] M-2: If using `zsh`, edit `~/.zshrc` & add this line:

```bash
# import python packages from Anaconda rather than system python
export PATH="$HOME/opt/anaconda3/bin/:$PATH"
```

Now, you can import the package successfully inside Jupyter Notebook & also in a separate python file.

### 3. Jupyter kernel issue on macOS

- Reason: When using jupyter notebook on macOS, it shows the following error:

```console
No kernel found
```

- Solution:

  - M-1: Install the kernel for the python version you are using. For example, if using python3.9, then install the kernel for python3.9.

  ```sh
  python3.9 -m pip install ipykernel
  ```

  - M-2: Connect to a already running jupyter notebook kernel. Just run `$ jupyter notebook` command in the directory where the notebook is present.

## Repositories

### Self

- [Semantic Hashing Demo](https://github.com/abhi3700/semantic-hashing-demo)
- [AutoPlot](https://github.com/abhi3700/AutoPlot)

### Others

- Python Algorithms - <https://github.com/TheAlgorithms/Python>
- HackerRank Problems and Solutions - <https://github.com/juhilsomaiya/HackerRank-Python-Algorithm-Solution>
- Plotly Offline Charts - <https://github.com/SayaliSonawane/Plotly_Offline_Python>
- Plotly Dashboards with Dash - <https://github.com/Pierian-Data/Plotly-Dashboards-with-Dash>
- Plotly Datasets - <https://github.com/plotly/datasets>
- Dash plotly recipes (for discussion forum) - <https://github.com/plotly/dash-recipes>
- Pandas Exercises - <https://github.com/guipsamora/pandas_exercises>
- Zulip (powerful open source team chat) - <https://github.com/zulip/zulip>
- Code Beautify (into Image) - [LINK](<https://carbon.now.sh/?bg=rgba(48%2C127%2C194%2C1)&t=monokai&wt=none&l=yaml&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fm=Hack&fs=14px&lh=133%25&si=false&es=4x&wm=false&code=worker%253A%2520python%2520app%252Fbot.py>)
- Dash Bootstrap Components - <https://dash-bootstrap-components.opensource.faculty.ai/>
- Automate docs with Python - [Documentation](https://python-docx.readthedocs.io/en/latest/), [Github](https://github.com/python-openxml/python-docx), [pip](https://pypi.org/project/python-docx/), [Example](https://pbpython.com/python-word-template.html)
- Automate PPT with Python - [Documentation](https://python-pptx.readthedocs.io/en/latest/), [Github](https://github.com/scanny/python-pptx), [pip](https://pypi.org/project/python-pptx/)
- Python Geocoding Toolbox (location, coordinates, address, street, city, country) - [pip](https://pypi.org/project/geopy/), [example](https://chrisalbon.com/python/data_wrangling/geolocate_a_city_and_country/)
- Geocoding and reverse geocoding using Python - <https://chrisalbon.com/python/data_wrangling/geocoding_and_reverse_geocoding/>
- Beautiful formatting in Console - <https://github.com/willmcgugan/rich>
- Learning Python through test-driven development of games and puzzles - <https://github.com/kyclark/tiny_python_projects>
- Open source home automation that puts local control and privacy first - <https://github.com/home-assistant/core>
- Apprise - Push Notifications that work with just about every platform! - <https://github.com/caronc/apprise>

## Data Visualization

- Dash Plotly - <https://dash.plot.ly/>
- Django with Dash - [Online Documentation](https://django-plotly-dash.readthedocs.io/en/latest/introduction.html), [pip](https://pypi.org/project/django-plotly-dash/)
- Python all charts - <https://python-graph-gallery.com/>

## [Machine Learning](https://github.com/abhi3700/My_Learning_AI)

## References

- [Pandas dropping rows and columns](https://chrisalbon.com/python/data_wrangling/pandas_dropping_column_and_rows/)
- [Python Tips](http://book.pythontips.com/en/latest/index.html)
- [Solving Memory related issues](https://dzone.com/articles/python-memory-issues-tips-and-tricks)
- [Learn Maths in simple way](https://www.mathsisfun.com/index.htm)

# TODO

## Code

- <https://towardsdatascience.com/elements-of-functional-programming-in-python-1b295ea5bbe0>
