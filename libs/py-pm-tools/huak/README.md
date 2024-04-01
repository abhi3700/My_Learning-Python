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

If the `pyproject.toml` is already present, then `huak init` downloads the packages & installs into `./.venv/lib/python3.11/site-packages` folder so as to run `$ huak run <script_name>` smoothly.

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

### Add/Remove dependency

This is to add/remove dependencies to the project.

```sh
huak add <package-name>
huak remove <package-name>
```

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

### Script

> Run `huak init` to download the packages into  `/lib/python3.x`/site-packages

```toml
[tool.huak.task]
counter = ".venv/bin/python3 src/flet_demo/counter.py"
todo = ".venv/bin/python3 src/flet_demo/todo.py"
```

Now, you can run:

```sh
huak run counter
huak run todo
```

### Code quality

```sh
pylyzer src/demo/main.py
```

### Generate `requirements.txt`

`requirements.txt` is list of dependencies for the project. On top of `huak`, one might need to install all the required dependencies in their machine to support proper code suggestion in their Code Editor.

Generate/Update `requirements.txt`:

```sh
huak freeze
```

I submitted a [PR](https://github.com/cnpryer/huak/pull/897) for this feature. One can install it via:

1. M-1 | Using `pip`: `$ pip install git+https://github.com/abhi3700/huak@add-freeze-cmd#egg=huak`
2. M-2 | In forked [`huak`](https://github.com/abhi3700/huak) repo, run `$ cp ./target/release/huak /usr/local/bin/` to copy into the folder which is added in `$PATH`.
3. M-3 | Install via `cargo`: `$ cargo install --path <path/to/project/cargo.toml>`

---

Now, one can install (globally) packages from the generated `requirements.txt` & run Jupyter in their local kernel containing the installed packages (thereby without using `huak` as it is for project management unlike Jupyter notebook):

```sh
pip install -r requirements.txt
```

## My projects

Projects done with `huak`:

- [Semantic Hashing Demo](https://github.com/abhi3700/semantic-hashing-demo)

## Integrate with Rust

Follow this [boilerplate](https://github.com/abhi3700/rusty-py-boilerplate).

## References

- [Github](https://github.com/cnpryer/huak/)
- [User guide](https://github.com/cnpryer/huak/blob/master/docs/user_guide.md)
