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
    boxes_index = []
    # Populating the boxes_index
    # This list will later be used
    # to identify if all boxes are open
    for index in range(len(boxes)):
        boxes_index.append(index)
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
        if (len(value) != 0):
            for item in value:
                if current.count(item) == 0:
                    current.append(item)
        index += 1
    # Appending 0 to current, so that the comparison can be
    # done correctly. This does not have any logical issues
    # as box 0 is always open.
    # Checking if 0 does not exist in current
    if current.count(0) == 0:
        current.append(0)
    if (sorted(current) == sorted(boxes_index)):
        return True
    else:
        return False
