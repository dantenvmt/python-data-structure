maze = [
        [".",".",".",".",".",".",],
        [".","x","x","x",".","x",],
        [".","x",".","x",".","x",],
        [".","x",".","x","x",".",],
        [".",".",".",".",".",".",],
        [".","x","x","x",".",".",],
        ["x",".",".",".","x",".",],
        [".",".",".",".","x",".",],
        [".",".",".",".","x",".",],
		  ]
	#print maze in a fasion way
def print_maze(maze):
  for row in maze:
    output = ""
    for col in row:
      output += col + " "
    print(output)
def solve_maze(maze, sol, pos_row, pos_col):
  #sizeofmaze
  maze_row = len(maze)
  maze_col = len(maze[0])

  #basecase
  #at goal
  if pos_row == maze_row-1 and pos_col == maze_col-1:
    return sol
  #outofmaze
  if pos_row >= maze_row or pos_col >= maze_col:
    return None
  #in x
  if maze[pos_row][pos_col] == "x":
    return None

  #recursive cases
  sol.append("right")
  sol_right = solve_maze(maze, sol, pos_row, pos_col+1)
  #fail then backtrack
  if sol_right is not None:
    return sol_right
  #go down
  sol.pop()
  sol.append("down")
  sol_down = solve_maze(maze,sol,pos_row +1, pos_col)
  if sol_down is not None:
    return sol_down

  #if all else fail
  sol.pop()
  return None
  return


    
