'''
Given: - An array of arrays passed in, representing a grid of 1s and 0s. 
- 1 represents land.
 - 0 represents water. 
- Any spot outside the grid can be assumed to be water (in other words, imagine 0s all around the grid)
- A land mass (aka island) is defined as a group of contiguous pieces of land.
- “contiguous” can be defined as: All pieces of land that are accessible from each other, 
without having to travel over water. Each piece of land is can be considered accessible of all 
pieces of land within one space of it. That space can be: - left - right - up - down - diagonally across in any direction
- This means each cell has 8 neighbors (except the cells at the border) 

Problem:
- Return the size of the largest island.
- Function signature should be: def get_largest_island(grid: List[List[int]]) -> int:
The following table (given to function as `[[0, 0, 1, 1, 0], [1, 0, 0, 1, 0], [0, 0, 1, 1, 0], [0, 1, 0, 0, 1], [0, 0, 0, 0, 0], [1, 1, 1, 0, 1]]`):
| Column 1 | Column 2 | Column 3 | Column 4 | Column 5 |
| :------: | :------: | :------: | :------: | :------: |
| 0        | 0        | 1        | 1        | 0        || 1        | 0        | 0        | 1        | 0        || 0        | 0        | 1        | 1        | 0        || 0        | 1        | 0        | 0        | 1        || 0        | 0        | 0        | 0        | 0        || 1        | 1        | 1        | 0        | 1        |
Should return 7, as it can trace an island consisting of (x, y) `(1, 3), (1, 4), (2, 4), (3, 3), (3, 4), (4, 2), (4, 5)` (one-based indexing)
'''

from typing import List

def get_largest_island(grid: List[List[int]]) -> int:
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    max_island_size = 0

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
            return 0
        size = 1
        grid[row][col] = 0  # mark current cell as visited
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r != row or c != col:
                    size += dfs(r, c)
        return size

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                island_size = dfs(i, j)
                max_island_size = max(max_island_size, island_size)

    return max_island_size

grid = [[0, 0, 1, 1, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1]]

print(get_largest_island(grid))
