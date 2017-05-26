"""
Count the number of items in a list, using recursion.

"""

def count_recursively(items):
    """
    >>> count_recursively([])
    0
    >>> count_recursively([1, 2, 3])
    3
    """

    if not items: 
        return 0

    return 1 + count_recursively(items[1:])

if __name__ == '__main__':
    import doctest 
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. DANCE IT OUT!"



