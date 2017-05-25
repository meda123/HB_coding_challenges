"""
BST concept test: make a binary search for a children's guessing game, guessing 
a number between 1-100. 
"""

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.

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

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    # START SOLUTION #

    higher_than = 0
    lower_than = 101
    guess = None

    while guess != val:
        num_guesses += 1
        guess = (lower_than - higher_than) / 2 + higher_than

        if val > guess:
            higher_than = guess

        elif val < guess:
            lower_than = guess

    # END SOLUTION

    return num_guesses


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n"

