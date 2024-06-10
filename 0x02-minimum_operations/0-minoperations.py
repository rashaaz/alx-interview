#!/usr/bin/python3

""" 0-minoperations.py """


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly `n`
    'H' characters in a file
    The target number of characters
    Returns int: The minimum number
    If `n` is impossible to achieve, return 0
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    iterator = 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
