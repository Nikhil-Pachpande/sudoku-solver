def find_empty_space(puzzle):
    # find an empty space and return -1 if it exists
    # this function will return row, col tuple
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == -1:
                return i, j
            
    # if there's no empty space
    return None, None

def guess_is_valid(puzzle, guess, row, col):
    # this function will return True if guess is valid, else False
    row_values = puzzle[row]
    if guess in row_values:
        return False
    
    # row index will vary but col index will remain same within each row
    col_values = []
    for x in range(9):
        col_values.append(puzzle[x][col])
    
    if guess in col_values:
        return False
    
    # to get the start of our 3x3 matrix
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    # iterate through the 3 values
    for a in range(row_start, row_start + 3):
        for b in range(col_start, col_start + 3):
            if puzzle[a][b] == guess:
                return False
            
    return True

def sudoku_solver(puzzle):
    # input is a list of lists 
    # returns whether a solution exists or not
    
    # choosing an entry point or blank space
    row, col = find_empty_space(puzzle)

    # edge case - check for either row or col is None (no empty space)
    if row is None:
        return True
    
    for guess in range(1, 10):
        if guess_is_valid(puzzle, guess, row, col):
            # if guess is valid, place it on the puzzle
            puzzle[row][col] = guess
            # recursive call
            if sudoku_solver(puzzle):
                return True
            
        # if guess is incorrect, then backtrack and try again
        # reset the guess to empty space i.e. -1
        puzzle[row][col] = -1

    # if no guess is correct, then provided puzzle can't be solved and return False
    return False

if __name__ == '__main__':
    sample_puzzle = [
        [3, 9, -1,      -1, 5, -1,      -1, -1, -1],
        [-1, -1, -1,    2, -1, -1,      -1, -1, 5],
        [-1, -1, -1,    7, 1, 9,        -1, 8, -1],
        
        [-1, 5, -1,     -1, 6, 8,       -1, -1, -1],
        [2, -1, 6,      -1, -1, 3,      -1, -1, -1],
        [-1, -1, -1,    -1, -1, -1,     -1, -1, 4],
        
        [5, -1, -1,     -1, -1, -1,     -1, -1, -1],
        [6, 7, -1,      1, -1, 5,       -1, 4, -1],
        [1, -1, 9,      -1, -1, -1,     2, -1, -1]
    ]
    print(sudoku_solver(sample_puzzle))
    print(sample_puzzle)
