"""
In this challenge, you’ll write a decoder.

A valid code is a sequence of numbers and letters, always starting with a 
number and ending with letter(s).Each number tells you how many characters to 
skip before finding a good letter. After each good letter should come the next 
next number.

For example, the string “hey” could be encoded by “0h1ae2bcy”. This means 
“skip 0, find the ‘h’, skip 1, find the ‘e’, skip 2, find the ‘y’”.

A single letter should work:

"""

def decode(word):
    """
    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'
    """