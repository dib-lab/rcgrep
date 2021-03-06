# ------------------------------------------------------------------------------
# Copyright (c) 2017 The Regents of the University of California
#
# This file is part of rcgrep (http://github.com/dib-lab/rcgrep) and is
# licensed under the MIT license: see LICENSE.
# ------------------------------------------------------------------------------

test:
	pytest -v --cov=rcgrep rcgrep/tests/*.py

style:
	pep8 rcgrep/*.py rcgrep/tests/*.py setup.py

devenv:
	pip install --upgrade pytest pytest-cov pep8

clean:
	rm -rf .cache/ .coverage rcgrep/__pycache__/ rcgrep/tests/__pycache__/
	rm -rf build/ dist/ *.egg-info/
	rm -f *.pyc rcgrep/*.pyc
