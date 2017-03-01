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
from rcgrep.search import program_by_filename


@pytest.mark.parametrize('testseq,filename', [
    ('ATGCCTTGGCATAGTTTGTCAAGGTACGACAGG', 'mrj.gdna.fa'),
    ('CCTGTCGTACCTTGACAAACTATGCCAAGGCAT', 'mrj.gdna.fa'),
    ('TAATGCACGAAAACTATAACAAAA', 'pbar.fa.gz'),
    ('TTTTGTTATAGTTTTCGTGCATTA', 'pbar.fa.gz')
])
def test_simple_search(testseq, filename, capfd):
    argslist = ['--query', testseq, rcgrep.test_data_file(filename)]
    args = rcgrep.cli.get_parser().parse_args(argslist)
    rcgrep.search.main(args)
    out, err = capfd.readouterr()
    assert testseq in out or rcgrep.revcom(testseq) in out


@pytest.mark.parametrize('testseq,readname', [
    ('TTTTGTTATAGTTTTCGTGCATTA', '@seq1'),
    ('CGTATATGGAAGAAAATTCACTTT', '@seq2')
])
def test_search_with_args(testseq, readname, capfd):
    argslist = ['--query', testseq, '--grepargs', '-B 1', '--verbose',
                rcgrep.test_data_file('reads.fq.bz2')]
    args = rcgrep.cli.get_parser().parse_args(argslist)
    rcgrep.search.main(args)
    out, err = capfd.readouterr()
    assert readname in out


def test_expressions():
    assert rcgrep.search.build_grep_expressions(['AAAA']) == \
        ['-e', 'AAAA', '-e', 'TTTT']
    assert rcgrep.search.build_grep_expressions(['GATTACA', 'ATGCCTT']) == \
        ['-e', 'GATTACA', '-e', 'TGTAATC',
         '-e', 'ATGCCTT', '-e', 'AAGGCAT']


def test_program_by_filename():
    assert program_by_filename('reads.fastq') == ['cat']
    assert program_by_filename('reads.1.fq.gz') == ['gunzip', '-c']
    assert program_by_filename('longreads.fa.bz2') == ['bunzip2', '-c']
    assert program_by_filename('reads.gz.bz2.fasta') == ['cat']


def test_verbose(capfd):
    from sys import stderr
    argslist = ['--query', 'TTTTGTTATAGTTTTCGTGCATTA', '--verbose',
                rcgrep.test_data_file('reads.fq.bz2')]
    args = rcgrep.cli.get_parser().parse_args(argslist)
    rcgrep.search.main(args, log=stderr)
    out, err = capfd.readouterr()
    assert 'bunzip2 -c' in err
    assert '-e TTTTGTTATAGTTTTCGTGCATTA -e TAATGCACGAAAACTATAACAAAA' in err
    assert 'reads.fq.bz2' in err
