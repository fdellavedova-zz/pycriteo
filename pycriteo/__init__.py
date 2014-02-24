# -*- coding: utf-8 -*-

#  _____        _____      _ _
# |  __ \      / ____|    (_) |
# | |__) |   _| |     _ __ _| |_ ___  ___
# |  ___/ | | | |    | '__| | __/ _ \/ _ \
# | |   | |_| | |____| |  | | ||  __/ (_) |
# |_|    \__, |\_____|_|  |_|\__\___|\___/
#         __/ |
#        |___/

"""
Criteo API Library
~~~~~~~~~~~~~~~~~~

PyCriteo is a simple library to access the Criteo API.

Basic usage:
    >>> from pycriteo import Client
    >>> c = Client('username', 'password', 'token')
    >>> c.getCampaigns({'campaignStatus': 'RUNNING'})
    >>> dict(c.campaign[0]).keys()
    ['status',
     'campaignID',
     'categoryBids',
     'budgetID',
     'campaignName',
     'remainingDays',
     'campaignBid']

:copyright: (c) 2014 by Francesco Della Vedova.
:license: Apache 2.0, see http://www.apache.org/licenses/LICENSE-2.0.html
 for more details.
"""

__title__ = 'pycriteo'
__version__ = '0.0.1'
__author = 'Francesco Della Vedova (fdellavedova@gmail.com)'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Francesco Della Vedova'

from .client import Client
