def solve_sudoku(board):
    """
    Solves the Sudoku board using backtracking algorithm

    Args:
        board (list): A 9x9 list of integers representing the Sudoku board

    Returns:
        list: Solved sudoku board
    """    
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for number in range(1, 10):
                    if is_valid(board, row, col, number):
                        board[row][col] = number
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return board
            
def is_valid(board, row, col, number):
    """
    Checks if the given number is valid at the given row and column

    Args:
        board (list): 9x9 sudoku board
        row (int): row number
        col (int): column number
        number (int): number in cell

    Returns:
        bool: whether the number is valid in its position
    """    
    # Check the row
    for x in range(9):
        if board[row][x] == number:
            return False

    # Check the column
    for x in range(9):
        if board[x][col] == number:
            return False

    # Check the 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == number:
                return False
    return True