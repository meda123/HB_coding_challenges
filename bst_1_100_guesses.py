"""
BST concept test: make a binary search for a children's guessing game, guessing 
a number between 1-100. 
"""
import random 

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

    rand_num = random.randint(0, 100)
    guesses = 0

    #count guesses 

    while val is not rand_num:
        if val is < rand_num:
            print "Guess higher"


    # i = 0 

    # while i is not val:
    #     for i in range(1, 100):
    #         if i == val:
    #             return      


binary_search(5)


##################### DocTests ###########################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

