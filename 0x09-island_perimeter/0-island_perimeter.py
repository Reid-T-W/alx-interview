#!/usr/bin/python3
""" Calculates the perimeter of an island """


def populate_dict(dicti, i, j):
    """ populates dict with key 0 and 1 """
    if dicti.get(grid[i][j]):
        dicti.get(grid[i][j]).append(str(i) + str(j))
    else:
        dicti[grid[i][j]] = [(str(i) + str(j))]
    return dicti


def island_perimeter(grid):
    """ Calculates the perimeter of an island located in grid """
    # Setting the border of the grid to 2 (indicates we are sure
    # it is water)
    numberOfCols = len(grid[0])
    numberOfRows = len(grid)
    # Setting first and last row to 2
    # for i in range(0, numberOfCols):
    #     grid[0][i] = 2;
    #     grid[numberOfRows - 1][i] = 2;
    # # Setting first and last col to 2
    # for i in range(0, numberOfRows):
    #     grid[i][0] = 2;
    #     grid[i][numberOfCols - 1] = 2;

    # seen = set()
    perimeter = 0
    dicti = {}
    for i in range(0, numberOfRows):
        for j in range(0, numberOfCols):
            # On border (which is water for sure)
            if grid[i][j] == 0:
                continue
            if grid[i][j] == 1:
                populate_dict(dicti, i, j + 1)
                populate_dict(dicti, i, j - 1)
                populate_dict(dicti, i + 1, j)
                populate_dict(dicti, i - 1, j)
                # seen.add(str(i) + str(j))
            if (dicti.get(1) is None):
                perimeter += 0
    if dicti.get(0) is not None:
        zeros = dicti.get(0)
        perimeter += len(zeros)
    return perimeter


# if __name__ == "__main__":
#     grid = [
#         [0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0],
#         [0, 1, 1, 1, 0, 0],
#         [0, 0, 0, 0, 0, 0]
#     ]
#     print(island_perimeter(grid))
