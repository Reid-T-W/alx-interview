#!/usr/bin/python3
""" Module to rotate a 2d martrix 90 degree clockwise """


def rotate_2d_matrix(matrix):
    """ Given an nxn martix rotates it 90 degree clockwise """
    # Transposing the matrix
    for row_ind, row in enumerate(matrix):
        for col_ind in range(row_ind, len(row)):
            if row_ind != col_ind:
                temp = matrix[row_ind][col_ind]
                matrix[row_ind][col_ind] = matrix[col_ind][row_ind]
                matrix[col_ind][row_ind] = temp
        if row_ind == len(matrix) // 2:
            break

    # Correctin the every row
    for row_ind, row in enumerate(matrix):
        end_index = len(row) - 1
        for col_ind in range(len(row)):
            if col_ind != len(row) // 2:
                temp = matrix[row_ind][col_ind]
                matrix[row_ind][col_ind] = matrix[row_ind][end_index]
                matrix[row_ind][end_index] = temp
                end_index = end_index - 1
            else:
                break
