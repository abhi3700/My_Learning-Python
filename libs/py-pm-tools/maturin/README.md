# Maturin

## Description

- It is a `cargo`-like tool for python projects that helps in integrating Rust into python project.
- It can be combined with any project manager

## Install

For macOS, install using `brew`:

```sh
brew install maturin
```

## Quickstart

1. Create a rust project (say, lib) using `cargo`:

```sh
cargo new --lib guessing-game
```

2. Add the following to the `Cargo.toml` file:

```toml
[package]
name = "guessing-game"
version = "0.1.0"
edition = "2021"

[lib]
name = "guessing_game"
# "cdylib" is necessary to produce a shared library for Python to import from.
crate-type = ["cdylib"]

[dependencies]
rand = "0.8.4"

[dependencies.pyo3]
version = "0.20.0"
# "abi3-py38" tells pyo3 (and maturin) to build using the stable ABI with minimum Python version 3.8
features = ["abi3-py38"]
```

3. Add `pyproject.toml` file to the root of the project with the following content:

```toml
[build-system]
requires = ["maturin>=1.0,<2.0"]
build-backend = "maturin"

[tool.maturin]
# "extension-module" tells pyo3 we want to build an extension module (skips linking against libpython.so)
features = ["pyo3/extension-module"]
```

4. Keep the virtual environment activated by running:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip maturin
pip freeze
# pip freeze > requirements.txt
```

This would create a `.venv` folder that contains the virtual environment with all 'site-packages'.

Now, your terminal looks like this with `.venv` activated:

```sh
(.venv) $
```

5. Now, edit the `src/lib.rs` file with this content:

<details><summary><b>Code:</b></summary>

```rust
use pyo3::prelude::*;
use rand::Rng;
use std::cmp::Ordering;
use std::io;

#[pyfunction]
fn guess_the_number() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..101);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn guessing_game(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(guess_the_number, m)?)?;

    Ok(())
}
```

</details>

6. Build the project (w/o `.whl` file generation):

```sh
maturin develop                                                                                                                           ⏎
🔗 Found pyo3 bindings with abi3 support for Python ≥ 3.8
🐍 Not using a specific python interpreter
📡 Using build options features from pyproject.toml
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
📦 Built wheel for abi3 Python ≥ 3.8 to /var/folders/cw/dc7mkcsd6yx76lscv6w1hpcw0000gn/T/.tmpukl13b/guessing_game-0.1.0-cp38-abi3-macosx_11_0_arm64.whl
🛠 Installed guessing-game-0.1.0
```

7. Try the module in venv:

```sh
(.venv) 
$ python3
Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import guessing_game as gg
>>> gg.guess
gg.guess_the_number() gg.guessing_game     
>>> gg.guess_the_number()
Guess the number!
Please input your guess.
45
You guessed: 45
Too small!
Please input your guess.
34
You guessed: 34
Too small!
Please input your guess.
^Z
[2]  + 81801 suspended  python3
```

8. In order to locally install the package (module) into my python interpreter lib (site-packages) path via `pip`, run:

```sh
maturin build
pip install target/wheels/guessing_game-0.1.0-cp38-abi3-macosx_11_0_arm64.whl
```

Now, this can be integrated with other project management tools like `poetry`, `huak`, etc. My personal favourite is `huak` ❤️.

## Commands

- <u>Build</u>: To build the project (inclusive of producing wheel that can be distributed), run:

```sh
maturin build
```

This generates a `.whl` file in the `target/wheels` directory like this:

```sh
target
└── wheels
    └── guessing_game-0.1.0-cp38-abi3-macosx_11_0_arm64.whl
```

- <u>Develop</u>: To build without the wheel file (`.whl`) generation:

```sh
maturin develop                                                                                                                           ⏎
🔗 Found pyo3 bindings with abi3 support for Python ≥ 3.8
🐍 Not using a specific python interpreter
📡 Using build options features from pyproject.toml
    Finished dev [unoptimized + debuginfo] target(s) in 0.02s
📦 Built wheel for abi3 Python ≥ 3.8 to /var/folders/cw/dc7mkcsd6yx76lscv6w1hpcw0000gn/T/.tmpukl13b/guessing_game-0.1.0-cp38-abi3-macosx_11_0_arm64.whl
🛠 Installed guessing-game-0.1.0
```

> This is normally done inside the virtual environment.

- <u>Publish</u>: To publish the package to PyPI:

```sh
maturin publish
```

> Ensure there is no published package with same name.
>
> Sample: <https://pypi.org/project/guessing-game-abhi/>

In case of any error during the publish, use `username`: __token__, password: __<api-token>__. <br />
Get the token from the PyPI account settings [here](https://pypi.org/manage/account/token/).
