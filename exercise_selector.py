import random


def get_coding_challenges(coding_challenges):
    """ Get 3 random coding challenge problems
    Input: List of coding challenge problems
    Output: List of 3 random coding challenge problems from the input list
    """

    random.shuffle(coding_challenges)
    return coding_challenges[0:3]


coding_challenge_probs = ['Anagram of Palindrome', 'Binary Search',
                          'Count List Recursively', 'Decode a String',
                          'Lazy Lemmings', 'Leaping Lemur',
                          'Missing Number', 'Pangram', 'Pig Latin',
                          'Prime Number Generator', 'Print Digits Backwards',
                          'Print List Recursively', 'Recursive Index',
                          'Remove Duplicates', 'Remove Linked List Node',
                          'Reverse Linked List',
                          'Reverse Linked List In Place',
                          'Reverse a String Recursively', 'Show Even Numbers',
                          'Sort Sorted Lists', 'Split a String',
                          'Sum List Recursively']

print get_coding_challenges(coding_challenge_probs)
