#!/usr/bin/python3

""" Module for checking if all boxes can be unlocked """


def canUnlockAll(boxes):
    """
    - Determines if all boxes can be unlocked
    - A list of lists representing
    - True if all boxes can be unlocked, False otherwise.
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be unlocked, False otherwise.
    """
    canUnlockAll = False
    keys = {0: True}
    n_boxes = len(boxes)
    while(True):

        n_keys = len(keys)

        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < n_boxes:
                        keys[j] = True
                    boxes[i] = None

        if not(len(keys) > n_keys):
            break

    if n_keys == len(boxes):
        canUnlockAll = True

    return canUnlockAll
