#!/usr/bin/env python
#
# -----------------------------------------------------------------------------
# Copyright (c) 2017 The Regents of the University of California
#
# This file is part of rcgrep (http://github.com/dib-lab/rcgrep) and is
# licensed under the MIT license: see LICENSE.
# -----------------------------------------------------------------------------

import argparse
import rcgrep


def get_parser():
    d = 'search text files for DNA sequences and their reverse complements'
    epilog = (
        'Example:\n\n    rcgrep --grepargs "-B 1 -A 2" --query GATTACA \\\n'
        '           --query AGGACAAATAGGATTTTGGTATATGT \\\n'
        '           reads.1.fq.gz reads.2.fq.gz longreads.fa.bz2'
    )
    parser = argparse.ArgumentParser(
        description=d,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-v', '--version', action='version',
                        version='rcgrep v{}'.format(rcgrep.__version__))
    parser.add_argument('-q', '--query', action='append', metavar='SEQ',
                        help='sequence(s) for which to search; this argument '
                        'can be declared more than once to search for multiple'
                        ' sequences')
    parser.add_argument('--grepargs', metavar='ARGS', type=str,
                        help='arguments to pass directly to the grep command; '
                        'when passing multiple arguments, enclose in double '
                        'quotes')
    parser.add_argument('-V', '--verbose', action='store_true',
                        help='print grep command(s) invoked to stderr')
    parser.add_argument('file', nargs='+', help='file(s) to search; gzip- and '
                        'bzip2-compressed files with conventional extensions '
                        '(.gz and .bz2) are detected and handled '
                        'automatically')
    return parser
