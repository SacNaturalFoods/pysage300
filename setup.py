# -*- coding: utf-8 -*-
################################################################################
#
#  pySage300 -- Python Interface to Sage 300 ERP
#  Copyright © 2014 Sacramento Natural Foods Co-op, Inc
#
#  This file is part of pySage300.
#
#  pySage300 is free software: you can redistribute it and/or modify it under
#  the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#  pySage300 is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  pySage300.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

from __future__ import unicode_literals

import os.path
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
execfile(os.path.join(here, 'sage300', '_version.py'))
README = open(os.path.join(here, 'README.rst')).read()


requires = [
    #
    # Version numbers within comments below have specific meanings.
    # Basically the 'low' value is a "soft low," and 'high' a "soft high."
    # In other words:
    #
    # If either a 'low' or 'high' value exists, the primary point to be
    # made about the value is that it represents the most current (stable)
    # version available for the package (assuming typical public access
    # methods) whenever this project was started and/or documented.
    # Therefore:
    #
    # If a 'low' version is present, you should know that attempts to use
    # versions of the package significantly older than the 'low' version
    # may not yield happy results.  (A "hard" high limit may or may not be
    # indicated by a true version requirement.)
    #
    # Similarly, if a 'high' version is present, and especially if this
    # project has laid dormant for a while, you may need to refactor a bit
    # when attempting to support a more recent version of the package.  (A
    # "hard" low limit should be indicated by a true version requirement
    # when a 'high' version is present.)
    #
    # In any case, developers and other users are encouraged to play
    # outside the lines with regard to these soft limits.  If bugs are
    # encountered then they should be filed as such.
    #
    # package                           # low                   high

    'pyodbc',                           # 2.1.11
    'SQLAlchemy',                       # 0.9.7
    ]


setup(
    name = "pySage300",
    version = __version__,
    author = "Sacramento Natural Foods Co-op, Inc",
    author_email = "developer@sacfoodcoop.com",
    url = "https://github.com/SacNaturalFoods/pysage300",
    license = "GNU GPL v3",
    description = "Python Interface to Sage 300 ERP",
    long_description = README,

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

    install_requires = requires,
    packages = find_packages(),
    )
