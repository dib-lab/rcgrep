[![PyPI version](https://img.shields.io/pypi/v/rcgrep.svg)](https://pypi.python.org/pypi/rcgrep)
![Supported Python versions](https://img.shields.io/pypi/pyversions/rcgrep.svg)
[![rcgrep build status](https://img.shields.io/travis/dib-lab/rcgrep.svg)](https://travis-ci.org/dib-lab/rcgrep)
[![Test coverage](https://img.shields.io/codecov/c/github/dib-lab/rcgrep.svg)](https://codecov.io/github/dib-lab/rcgrep)
[![MIT licensed](https://img.shields.io/pypi/l/rcgrep.svg)](https://github.com/dib-lab/rcgrep/blob/master/LICENSE)

# rcgrep

Search text files for DNA sequences and their reverse complements!

> **ME**: *I just need to search for a sequence in this file real quick. I'll use `grep`.*
>
> **ALSO ME**: *Oh, the file is bzip2-compressed. Use `bzgrep`.*
>
> **ME AGAIN**: *Oops, I forgot to search for the sequence's reverse complement as well. Try again.*
>
> **ME, 5 MINUTES LATER**: *This time I want to search the file for 3 sequences and their reverse complements. Invoke `bzgrep` with multiple `-e` flags.*
>
> **ME, HEAD ON DESK**: *Uggghh, `bzgrep` on Linux doesn't support multiple `-e` flags. Pipe output of `bzcat` to `grep`.*

Like many problems in computational biology, searching for DNA sequences in text files is a very simple task that is unnecessarily complicated by a variety of technical details.
**rcgrep** is a lightweight wrapper for the `grep` command intended to make these irrelevant details disappear as much as possible.

- **rcgrep** searches not only for the supplied sequence(s) but also for the corresponding reverse complement(s).
- **rcgrep** supports searching for multiple query sequences simultaneously.
- **rcgrep** detects and handles .gz and .bz2 files automatically.
- **rcgrep** is implemented in pure Python (no compilation required), has no non-standard dependencies, supports Python versions 2 and 3, and can be easily installed via a package manager.


## Quick install

The `rcgrep` command is easily installed from PyPI.

```
pip install rcgrep
```

Recommended: to make sure `rcgrep` is installed correctly, run the tests like so.

```
pip install pytest
pytest --pyargs rcgrep.tests
```


## Contact

This project was originally written by Daniel Standage in the [Lab for Data Intensive Biology](http://ivory.idyll.org/lab/) at UC Davis.
If you have any questions, feedback, or suggestions, feel free to contact us via the [issue tracker](https://github.com/dib-lab/rcgrep/issues).

Even better, send us a pull request!
Contributions from the wider community are welcomed!
See [DEVNOTES.md](DEVNOTES.md) for a quick start guide to development.


## License

**rcgrep** is Copyright Regents of the University of California, 2017.
All the code is freely available for use and re-use under the MIT License.
Distribution, modification and redistribution, incorporation into other software, and pretty much everything else is allowed.
