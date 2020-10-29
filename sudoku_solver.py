board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]]

def print_board(board):
    num_row = len(board)
    num_col = len(board[0])
    for i in range(num_row):
        if i % 3 == 0:
            print("- - - - - - - - - - - - -")
        form_print = ""
        for j in range(num_col):
            if j % 3 == 0:
                form_print += "| "
            form_print += str(board[i][j]) + " "
        form_print += "|"
        print(form_print)
    print("- - - - - - - - - - - - -")
#find zero
def find_zero(board):
    for row in range( len(board) ):
        for column in range( len(board[row]) ):
            if board[row][column] == 0:
                return [row, column]
    return None
      
#check if placement is valid
def is_valid(board,  row,col, value): 
  for i in range( len(board[row]) ):
    if board[row][i] == value and i != col:
      return False
  for i in range( len(board) ):
    if board[i][col] == value and i != row:
      return False

  x = (row//3) * 3 #x represents rows
  y = (col//3) * 3 #y represents columns
  for i in range(3):
    for j in range(3):
      if board[x+i][y+j] == value and (x+i != row and y+j != col):
                return False

    return True
#solve sudoku
def solve(board):
  #base case:
  a = find_zero(board)
  if a is None:
    return board
  #recursive:
  r = a[0]
  c = a[1]
  for i in range(1,10):
    if (is_valid(board,r,c, i)):
      board[r][c] = i
      if solve(board) is not None:
        return solve(board)
      board[r][c] =0
  return None

