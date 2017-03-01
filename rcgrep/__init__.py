#!/usr/bin/env python
#
# -----------------------------------------------------------------------------
# Copyright (c) 2017 The Regents of the University of California
#
# This file is part of rcgrep (http://github.com/dib-lab/rcgrep) and is
# licensed under the MIT license: see LICENSE.
# -----------------------------------------------------------------------------

import pkg_resources
from . import search
from . import cli

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__complement = {
    'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A',  # canonical bases
    'Y': 'R', 'R': 'Y',  # Y=pyrimidine, R=purine
    'S': 'S', 'W': 'W',  # S=strong (3 h-bonds), W=weak (2 h-bonds)
    'K': 'M', 'M': 'K',  # K=keto, M=amino
    'B': 'V', 'V': 'B',  # B=not A, V=not T
    'H': 'D', 'D': 'H',  # D=not C, H=not G
    'N': 'N',  # N=unknown
}


def revcom(dna):
    return "".join(__complement[n.upper()] for n in reversed(dna))


def test_data_file(basename):
    datadir = pkg_resources.resource_filename('rcgrep', 'tests/data')
    return datadir + '/' + basename
