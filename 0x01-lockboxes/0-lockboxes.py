#!/usr/bin/python3
""" Checks if all boxes are unlockable """


def canUnlockAll(boxes):
    """
    Function for checking if all boxes
    are unlockable
    """
    open_close = []
    current = []
    size = len(boxes)
    if size == 1:
        return True  # The first box is always open
    # Populating current
    # Checking if the first box does not have any keys
    if len(boxes[0]) == 0:
        return False
    for key in boxes[0]:
        current.append(key)
    index = 0
    while index < len(current):
        value = boxes[current[index]]
        if (len(value) == 0 and current[index] == size - 1):
            # Randomly appended 0 since its always open
            # Look for better ways
            current.append(0)
        elif (len(value) == 0):
            pass
        else:
            for item in value:
                if current.count(item) == 0:
                    current.append(item)
        index += 1
    if len(boxes) == len(current):
        return True
    else:
        return False
