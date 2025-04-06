# Program that concerns devising a set of tests for a Python function that cumulatively achieve statement coverage
# Makanaka Mangwanda 
# 10 April 2024

"""
>>> import palindrome
>>> palindrome.is_palindrome('5 6 7 5')
False
>>> palindrome.is_palindrome('civic')
True
>>> palindrome.is_palindrome('')
True
>>> palindrome.is_palindrome('a')
True
>>> palindrome.is_palindrome('Civic')
False

"""


import doctest
doctest.testmod(verbose=True)