import numpy as np
import time

def create_numpy_array():
    """Create numpy array from user input"""
    
    matrix = []
    
    print("Enter the sudoku puzzle row by row:")
    for i in range(9):
        row_input = input()
        
        row = list(map(int,row_input.split()))
        
        if len(row) != 9:
            print(f"Oops! You have made an error: Row {i+1} must have 9 numbers")
            return None
        
        matrix.append(row)
        
    
    array = np.array(matrix)
    return array

def check_safe(board, row, col, num):
    """Check if num can be placed on the board at given row and column and in the 3x3 sub-grid"""
    
    if num in board[row, :]:
        return False
    
    if num in board[: ,col]:
        return False
    
    start_row, start_col = 3 * (row //3), 3 * (col // 3)
    if num in board[start_row:start_row+3, start_col:start_col+3]:
        return False
    
    return True

def solve_sudoku(board):
    
    empty_cell = np.argwhere(board == 0)
    
    if len(empty_cell) == 0:
        #No more empty cells => puzzle solved
        return True
    
    row, col = empty_cell[0]
    
    for num in range(1,10):
        if check_safe(board, row, col, num):
            #Place number
            board[row,col] = num
            
            #Attemp to solve the rest of the puzzle, recursively
            if solve_sudoku(board):
                return True
            
            #If failed, backtrack and unod placement
            board[row,col] = 0
            
    return False
    
    
def print_board(board):
    for row in board:
        print(" ".join(str(x) if x != 0 else '.' for x in row))

sudoku_puzzle = create_numpy_array()

print("Original Sudoku Puzzle:")
print_board(sudoku_puzzle)

start_time = time.time()

if solve_sudoku(sudoku_puzzle):
    print("\nSolved Sudoku Puzzle:")
    print_board(sudoku_puzzle)
else:
    print("No solution exists.")
    
end_time = time.time() 

solve_time = end_time - start_time
print(f"Sudoku Solver took {solve_time} seconds to solev the puzzle. How much time did it take you to do it by hand?")
