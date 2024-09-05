def is_valid_move(grid, row, col, number):
    # Check if the number is already in the row
    for x in range(9):
        if grid[row][x] == number:
            return False

    # Check if the number is already in the column
    for x in range(9):
        if grid[x][col] == number:
            return False

    # Check if the number is already in the 3x3 subgrid
    corner_row = row - row % 3
    corner_col = col - col % 3

    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    return True

def solve(grid, row, col):
    # If we have reached the last column of the current row
    if col == 9:
        # Move to the next row
        if row == 8:
            return True
        row += 1
        col = 0

    # If the current position already contains a value, skip to the next column
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    # Try numbers 1 to 9 in the current cell
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True
            # Backtrack
            grid[row][col] = 0

    return False

# Example grid for testing
grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("No solution for this Sudoku")
