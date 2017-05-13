
"""
Challenge: Is the word an anagram of a palindrome? 

A palindrome is a word that reads the same forward and backwards 
(eg, racecar, tacocat). An anagram is a rescrambling of a word 
(eg for racecar, you could rescramble this as arceace).

Determine if the given word is a re-scrambling of a palindrome.

The word will only contain lowercase letters, a-z.
"""


def is_anagram_of_palindrome(word):
    """ 
    Checks to see if word is anagram of a palindrome

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True
    
    >>> is_anagram_of_palindrome("arceaceb")
    False

    """

    seen = {}

#Count each letter 

    for letter in word:
        count = seen.get(letter, 0)
        seen[letter] = count + 1

# It's a palindrome if the number of odd-counts is either 0 or 1
    
    seen_an_odd = False

    for count in seen.values():
        if count % 2 != 0:
            if seen_an_odd:
                return False
            seen_an_odd = True

    return True    
 

##################### DocTests ###########################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print




