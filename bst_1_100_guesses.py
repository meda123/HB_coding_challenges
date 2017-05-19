
"""
Binary search is one of the most important Computer Science algorithms. 
It allows you to search a sorted list in O(log n) time, a large improvement 
over scanning every item in the list (which would be O(n) time).

In this challenge, you’ll make binary search for the classic children’s guessing
game of “pick a number from 1 to 100”.

"""

def binary_search(val):
    """
    Function returns number of guesses after trying to find val (the number you
    are trying to guess between 1-100)

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7 

    """

    guess = 
    i = 0 

    while i is not val:
        for i in range(1, 100):
            if i == val:
                return      





##################### DocTests ###########################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

