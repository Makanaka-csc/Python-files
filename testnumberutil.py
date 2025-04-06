# Program devising a set of tests for a Python function that cumulatively achieve path coverage.
# Makanaka Mangwanda
# 09 April 2024

"""
>>> import numberutil

>>> numberutil.aswords(90)
'ninety'
>>> numberutil.aswords(300)
'three hundred'
>>> numberutil.aswords(318)
'three hundred and eighteen'
>>> numberutil.aswords(180)
'one hundred and eighty'
>>> numberutil.aswords(25)
'twenty five'
>>> numberutil.aswords(131)
'one hundred and thirty one'
>>> numberutil.aswords(18)
'eighteen'
>>> numberutil.aswords(0)
'zero'

"""

import doctest
doctest.testmod(verbose=True)