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

"""
Database Interface
"""

from sqlalchemy.orm import sessionmaker


Session = sessionmaker()
