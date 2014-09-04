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
Database Models
"""

from __future__ import unicode_literals

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def stripped(column):
    """
    Convenience function to create a property which returns a "stripped"
    version of the underlying column.
    """
    def getter(self):
        value = getattr(self, column)
        if value is None:
            return None
        return value.strip()
    return property(getter)


class APVendor(Base):
    """
    Represents an A/P vendor.
    """
    __tablename__ = 'APVEN'

    VENDORID = sa.Column(
        'VENDORID', sa.String(length=12), primary_key=True, nullable=False)

    SHORTNAME = sa.Column(
        'SHORTNAME', sa.String(length=10), nullable=False)

    short_name = stripped('SHORTNAME')

    VENDNAME = sa.Column(
        'VENDNAME', sa.String(length=60), nullable=False)

    name = stripped('VENDNAME')

    TEXTSTRE1 = sa.Column(
        'TEXTSTRE1', sa.String(length=60), nullable=False)

    street1 = stripped('TEXTSTRE1')

    TEXTSTRE2 = sa.Column(
        'TEXTSTRE2', sa.String(length=60), nullable=False)

    street2 = stripped('TEXTSTRE2')

    TEXTSTRE3 = sa.Column(
        'TEXTSTRE3', sa.String(length=60), nullable=False)

    street3 = stripped('TEXTSTRE3')

    TEXTSTRE4 = sa.Column(
        'TEXTSTRE4', sa.String(length=60), nullable=False)

    street4 = stripped('TEXTSTRE4')

    NAMECITY = sa.Column(
        'NAMECITY', sa.String(length=30), nullable=False)

    city = stripped('NAMECITY')

    CODESTTE = sa.Column(
        'CODESTTE', sa.String(length=30), nullable=False)

    state = stripped('CODESTTE')

    CODEPSTL = sa.Column(
        'CODEPSTL', sa.String(length=20), nullable=False)

    postal_code = stripped('CODEPSTL')

    CODECTRY = sa.Column(
        'CODECTRY', sa.String(length=30), nullable=False)

    country = stripped('CODECTRY')

    NAMECTAC = sa.Column(
        'NAMECTAC', sa.String(length=60), nullable=False)

    contact = stripped('NAMECTAC')

    TEXTPHON1 = sa.Column(
        'TEXTPHON1', sa.String(length=30), nullable=False)

    phone1 = stripped('TEXTPHON1')

    TEXTPHON2 = sa.Column(
        'TEXTPHON2', sa.String(length=30), nullable=False)

    phone2 = stripped('TEXTPHON2')

    GLACCNT = sa.Column(
        'GLACCNT', sa.String(length=45), nullable=False)

    general_ledger_account = stripped('GLACCNT')

    TERMSCODE = sa.Column(
        'TERMSCODE', sa.String(length=6), nullable=False)

    terms_code = stripped('TERMSCODE')

    EMAIL1 = sa.Column(
        'EMAIL1', sa.String(length=50), nullable=False)

    email1 = stripped('EMAIL1')

    EMAIL2 = sa.Column(
        'EMAIL2', sa.String(length=50), nullable=False)

    email2 = stripped('EMAIL2')

    WEBSITE = sa.Column(
        'WEBSITE', sa.String(length=100), nullable=False)

    website = stripped('WEBSITE')

    CTACPHONE = sa.Column(
        'CTACPHONE', sa.String(length=30), nullable=False)

    contact_phone = stripped('CTACPHONE')
