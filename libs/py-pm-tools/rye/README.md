# Rye

Write Python rustically 🧑🏻‍💻🦀 using Rye package manager

## Installation

Install rye using curl:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

<!-- Check if poetry is installed:

```sh
poetry --version
```

## Usage

### New project

Create a new project

```sh
poetry new demo
```

This is the file directory structure:

```sh
demo
├── README.md
├── demo
│   ├── __init__.py
│   └── __pycache__
├── dist
│   ├── demo-0.1.0-py3-none-any.whl
│   └── demo-0.1.0.tar.gz
├── poetry.lock
├── pyproject.toml
└── tests
    └── __init__.py
```

### Check

To check without building in order to save:

> Like `$ cargo check` command in Rust.

```sh
poetry check
All set!
```

### Build

```sh
poetry build
Building demo (0.1.0)
  - Building sdist
  - Built demo-0.1.0.tar.gz
  - Building wheel
  - Built demo-0.1.0-py3-none-any.whl
```

### Scripts

Define scripts for easy run using `poetry` as done in `package.json` in Node.js.
  
```toml
[tool.poetry.scripts]
city = "demo:city"  # defined in "__init__.py"
village = "demo:village"  # defined in "__init__.py"
```

Now, run the following command to run the `city` script:

```sh
poetry run city
```

> NOTE: Need to run `poetry build` >> `poetry install` >> `poetry run city` to run the script.

### Install

Before running the scripts, install the dependencies after `poetry build`:

```sh
poetry install
```

Then, the `pyproject.toml` file will be updated with the dependencies:

### Lock

Generate a `poetry.lock` file:

```sh
poetry lock
```

Like `Cargo.lock`, `poetry.lock` is a file that records the exact versions of the dependencies that were used for a particular build.
And then one can use `$ poetry install` to install the exact versions of the dependencies.

### Run

Referring to the above directory structure, the following command will run the `main.py` file:

```sh
poetry run python3 -m rusty_python.main
```

And the following command will run the `greet.py` file:

```sh
poetry run python3 -m rusty_python.greet
```

Another way to urn

### Test

```sh
poetry test
```

## Coding

Here are the things to note:

- `__init__.py` is a file that makes the directory a python package.
- In the following code within `demo/demo/greet.py`

```python
def say_hello(name: str) -> str:
    return f"Hello, {name} from greet.py!"

def main():
    print(say_hello("Abhijit"))

if __name__ == "__main__":
    main()
```

  there are 2 ways to run this file from terminal at [demo](./poetry/demo/) directory:

- Using `python3` binary: `$ python3 demo/greet.py`
- Using `poetry`: `$ poetry run python3 -m demo.greet`
- Using `poetry` script: `$ poetry run greet` where `greet` is defined in `pyproject.toml` file:
  
  ```toml
  [tool.poetry.scripts]
  greet = "demo.greet:main"
  ```

  > NOTE: `if __name__ == "__main__":` is not called from script, but instead `main()` function is called from the script.

- `greet.py`: a module that is a part of package [`demo`](./poetry/demo/) project.
  > DEFINITION: A module is a single file (or files) that are imported under one import and used. Package is a collection of modules in directories that give a package hierarchy.
- `main.py`: a module that is a part of package  [`demo`](./poetry/demo/) project.

## References

- [Github](https://github.com/python-poetry/poetry) with 28k+ ⭐
- [Poetry Documentation](https://python-poetry.org/docs/) -->
