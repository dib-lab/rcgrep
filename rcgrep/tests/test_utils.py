#!/usr/bin/env python
#
# -----------------------------------------------------------------------------
# Copyright (c) 2017 The Regents of the University of California
#
# This file is part of rcgrep (http://github.com/dib-lab/rcgrep) and is
# licensed under the MIT license: see LICENSE.
# -----------------------------------------------------------------------------

import rcgrep


def test_revcom_simple():
    assert rcgrep.revcom('ACGT') == 'ACGT'
    assert rcgrep.revcom('AAAA') == 'TTTT'
    assert rcgrep.revcom('gattaca') == 'TGTAATC'
    assert rcgrep.revcom('NNNN') == 'NNNN'
    assert rcgrep.revcom('ATGCCTTGGCATAGTTTGTCAAGGTACGACAGG') == \
        'CCTGTCGTACCTTGACAAACTATGCCAAGGCAT'


def test_revcom_iupac():
    assert rcgrep.revcom('ATTGGNS') == 'SNCCAAT'
    assert rcgrep.revcom('GATTAKA') == 'TMTAATC'
    assert rcgrep.revcom('ABBA') == 'TVVT'
    assert rcgrep.revcom('DADSBAD') == 'HTVSHTH'
