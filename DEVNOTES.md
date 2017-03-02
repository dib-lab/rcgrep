# Development for rcgrep

## Downloading the source code

Create a fork of the [main rcgrep git repository](https://github.com/dib-lab/rcgrep) and clone the fork to your local computer.
See https://help.github.com/articles/fork-a-repo/ for more details.

```
git clone https://github.com/YourGithubUserName/rcgrep.git
cd rcgrep/
```

## Setting up virtualenv

It's best to isolate the development environment in a dedicated virtualenv.
See http://docs.python-guide.org/en/latest/dev/virtualenvs/ for more details.

```
# This command creates the virtual environment. It only needs to be executed once.
virtualenv -p python3 env

# This command "turns on" the virtual environment. It needs to be executed any
# time you open a new terminal.
source env/bin/activate
```

## Installing dependencies

rcgrep doesn't have any runtime dependencies, but requires a couple of common Python packages for development.
After creating and activating your virtualenv, invoke `make devenv` to install the dependencies.

## Checking the code

The Makefile provides a few procedures for checking the code.

- `make test` will execute the automated test suite
- `make style` will check the Python code against the PEP8 style guide

Both of these will have to pass before any changes are merged into to the master branch of the main repository.
