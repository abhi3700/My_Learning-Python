# huak

pronounced as "hwok" is a `cargo`-like package manager for Python.

## Install

Recommended to install using `pip` with git.

```sh
pip install git+https://github.com/cnpryer/huak@master#egg=huak
```

For auto-completion, follow this:

1. Add autocompletion script to a file

```sh
mkdir -p ~/.zsh/completions
huak completion --shell zsh > ~/.zsh/completion/_huak
```

2. Add the following line to your `.zshrc` file

```sh
# add this line to your .zshrc
eval "$(huak completion --shell zsh)"
```

3. Activate the changes

```sh
source ~/.zshrc
```

## Docs

For more, refer the user guide [here](https://github.com/cnpryer/huak/blob/master/docs/user_guide.md).

## Usage

### Init/New

```sh
huak init --app
# or
huak new --app
```

For new:

```sh
huak new demo --app
# or
huak new demo --lib
```

By default, it's a library. If you want to create an app, then use `--app` flag.

### Build

Build tarball and wheel for the project.

```sh
huak build
```

This step helps in adding required packages (defined in `pyproject.toml`) to `.venv` folder at the root of the project. So, it's going to be self-contained and can be run anywhere. Doesn't have to depend on the system's Python environment lib folder like `/opt/homebrew/lib/python3.11/site-packages`. Helpful to run CI/CD on different machines.

### Run

Define the tasks:

```toml
...

[tool.huak.task]
main = "python3 src/demo/main.py"
```

> Don't forget to add this main function in `main.py`:

```python
if __name__ == "__main__":
main()
```

Now, run (use interpreter):

```sh
huak run main
```

Please note that the packages used in the code is searched via `$ huak run <task-name>` in this location. So, it is mandatory to `build` before `run`ning any task.

```sh
$ huak run which python3
/Users/abhi3700/F/coding/github_repos/My_Learning-Python/libs/openai/demo/.venv/bin/python3
```

> This would take 0.03s more than running `$ python3 src/demo/main.py` due to the overhead of `huak`. It is even worse with `poetry` (takes 0.6s vs standard 0.06s using `python3`).

### Test

```sh
huak test
```

### Format, Lint

```sh
huak fmt
huak lint
```

> It's using [ruff](https://github.com/astral-sh/ruff) that is used for both linting & code formatting. <br/>
> Underneath, it's doing this: `$ ruff format .` & `$ ruff lint .` <br/>
>
> NOTE: `ruff` is way better than any tool that I know of for lint, format in Python. <br/>

### Code quality

```sh
pylyzer src/demo/main.py
```

### Generate `requirements.txt`

`requirements.txt` is list of dependencies for the project. On top of `huak`, one might need to install all the required dependencies in their machine to support proper code suggestion in their Code Editor.

Generate/Update `requirements.txt`:

```sh
huak build
huak activate
pip freeze > requirements.txt
```

Install `requirements.txt`:

```sh
pip install -r requirements.txt
```

## Integrate with Rust

Follow this [boilerplate](https://github.com/abhi3700/rusty-py-boilerplate).

## References

- [Github](https://github.com/cnpryer/huak/)
- [User guide](https://github.com/cnpryer/huak/blob/master/docs/user_guide.md)
