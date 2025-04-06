# Program devising a set of tests for a Python function that cumulatively achieve path coverage.
# Makanaka Mangwanda
# 09 April 2024

"""
>>> import numberutil

>>> numberutil.aswords(300)
'three hundred'
>>> numberutil.aswords(90)
'ninety'
>>> numberutil.aswords(303)
'three hundred and three'
>>> numberutil.aswords(300)
'three hundred'
>>> numberutil.aswords(320)
'three hundred and twenty'
>>> numberutil.aswords(330)
'three hundred and thirty'
>>> numberutil.aswords(300)
'three hundred'
>>> numberutil.aswords(8)
'eight'
"""

import doctest
doctest.testmod(verbose=True)