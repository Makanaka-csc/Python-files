# Program that accepts an integer (0-999) as a parameter and returns the English language equivalent
# Makanaka Mangwanda
# 11 April 2024

"""
>>> import timeutil
>>> timeutil.validate(':59 a.m.')
False
>>> timeutil.validate('112:59 a.m.')
False
>>> timeutil.validate('02:59 a.m.')
False
>>> timeutil.validate('12:59 a.J.')
False
>>> timeutil.validate('12:5 a.m.')
False
>>> timeutil.validate('12:59 a.m.')
True

"""

import doctest
doctest.testmod(verbose=True)