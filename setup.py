#!/usr/bin/env python
#
# -----------------------------------------------------------------------------
# Copyright (c) 2017 The Regents of the University of California
#
# This file is part of rcgrep (http://github.com/dib-lab/rcgrep) and is
# licensed under the MIT license: see LICENSE.
# -----------------------------------------------------------------------------

from setuptools import setup
import versioneer


d = 'Search text files for DNA sequences and their reverse complements'
setup(name='rcgrep',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description=d,
      long_description: open("README.md").read(),
      url='http://github.com/dib-lab/rcgrep',
      author='Daniel Standage',
      author_email='daniel.standage@gmail.com',
      license='MIT',
      packages=['rcgrep', 'rcgrep.tests'],
      package_data={'rcgrep': ['tests/data/*']},
      entry_points={'console_scripts': ['rcgrep = rcgrep.search:main']},
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Scientific/Engineering :: Bio-Informatics'
      ],
      zip_safe=True)
