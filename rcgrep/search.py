#!/usr/bin/env python
#
# -----------------------------------------------------------------------------
# Copyright (c) 2017 The Regents of the University of California
#
# This file is part of rcgrep (http://github.com/dib-lab/rcgrep) and is
# licensed under the MIT license: see LICENSE.
# -----------------------------------------------------------------------------

from __future__ import print_function
import subprocess
from sys import stderr
import rcgrep


def build_grep_expressions(query_args):
    exp_list = list()
    for q in query_args:
        exp_list.extend(['-e', q, '-e', rcgrep.revcom(q)])
    return exp_list


def program_by_filename(file_to_search):
    if file_to_search.endswith('.gz'):
        return 'zgrep'
    elif file_to_search.endswith('.bz2'):
        return 'bzgrep'
    return 'grep'


def main(args, log=stderr):
    expressions = build_grep_expressions(args.query)

    if args.grepargs:
        greparg_strings = args.grepargs.split()

    for file_to_search in args.file:
        program = program_by_filename(file_to_search)

        command = [program] + expressions
        if args.grepargs:
            command += greparg_strings
        command += [file_to_search]

        if args.verbose:
            print(' '.join(command), file=log)
        subprocess.call(command)


if __name__ == '__main__':  # pragma: no cover
    main(rcgrep.cli.get_parser().parse_args())
