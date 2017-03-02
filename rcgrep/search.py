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
        return ['gunzip', '-c']
    elif file_to_search.endswith('.bz2'):
        return ['bunzip2', '-c']
    return ['cat']


def main(args=None, log=stderr):
    if args is None:  # pragma: no cover
        args = rcgrep.cli.get_parser().parse_args()
    expressions = build_grep_expressions(args.query)

    if args.grepargs:
        greparg_strings = args.grepargs.split()

    for file_to_search in args.file:
        program = program_by_filename(file_to_search)

        cat_command = program + [file_to_search]
        catproc = subprocess.Popen(cat_command,
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)

        grep_command = ['grep'] + expressions
        if args.grepargs:
            grep_command += greparg_strings
        if args.verbose:
            print(' '.join(cat_command), '|', ' '.join(grep_command), file=log)
        grepproc = subprocess.Popen(grep_command, stdin=catproc.stdout)
        grepproc.communicate()


if __name__ == '__main__':  # pragma: no cover
    main()
