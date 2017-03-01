#!/usr/bin/env python
#
# -----------------------------------------------------------------------------
# Copyright (c) 2017 The Regents of the University of California
#
# This file is part of rcgrep (http://github.com/dib-lab/rcgrep) and is
# licensed under the MIT license: see LICENSE.
# -----------------------------------------------------------------------------

import pytest
import rcgrep


def test_parser():
    parser = rcgrep.cli.get_parser()

    args = parser.parse_args(['--query', 'ATTA', '-q', 'TTTT', 'file.fa'])
    assert args.query == ['ATTA', 'TTTT']
    assert args.file == ['file.fa']

    args = parser.parse_args(['-q', 'SNNS', '--grepargs', '-A 2', 'file.fa'])
    assert args.query == ['SNNS']
    assert args.grepargs == '-A 2'

    with pytest.raises(SystemExit):
        args = parser.parse_args(['-q', 'SNNS', 'ATTA', '-v', 'file.fa'])
