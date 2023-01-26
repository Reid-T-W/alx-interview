#!/usr/bin/python3
"""Computes value for the pascal triangle"""


def pascal_triangle(n):
    """function for computing values of pascal triangle"""
    pascals_triangle = []
    counter = 1
    if n <= 0:
        return pascals_triangle
    if n == 1:
        pascals_triangle.append([1])
        return(pascals_triangle)
    else:
        pascals_triangle.append([1])
        row_add = []
        for row in pascals_triangle:
            # Controling number of rows in traingle
            if counter == n:
                break
            # Appending the first element in the row
            # which is always 1
            row_add.append(0 + row[0])
            for i in range(0, len(row)):
                # Adding elements in the last row of pascals_triangle
                # and appending them to the new row, this is done for
                # all middle elements
                if (i != len(row) - 1):
                    row_add.append(row[i] + row[i + 1])
                else:
                    # Appeding the last element (1) to the new row
                    row_add.append(0 + row[len(row) - 1])
            pascals_triangle.append(row_add)
            row_add = []
            counter = counter + 1
        return pascals_triangle
