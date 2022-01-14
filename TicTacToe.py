import random

def print_board(board):
  print(board[0]+board[1]+board[2])
  print(board[3]+board[4]+board[5])
  print(board[6]+board[7]+board[8])
  
def open_spots(board):
  new = []
  for i in range(9):
    if board[i] == '-':
      new.append(i)
  return new

def random_move(board, symbol):
  choice = random.choice(open_spots(board))
  board[choice] = symbol
  print_board(board)

def check_three(board, idx1, idx2, idx3):
  if board[idx1] == board[idx2] and board[idx2] == board[idx3]: 
    if board[idx1] == "O":
      return "O"
    elif board[idx1] == "X":
      return "X"
  return "-"

def winner(board):
  if check_three(board, 0, 1, 2) in ['X', 'O']:
    return check_three(board, 0, 1, 2)
    
  elif check_three(board, 3,4,5) in ['X', 'O']:
    return check_three(board, 3, 4, 5)

  elif check_three(board, 6,7,8) in ['X', 'O']:
    return check_three(board, 6, 7, 8)
    
  elif check_three(board, 0, 3, 6) in ['X', 'O']:
    return check_three(board, 0, 3, 6)

  elif check_three(board, 1, 4, 7) in ['X', 'O']:
    return check_three(board, 1, 4, 7)
    
  elif check_three(board, 2, 5, 8) in ['X', 'O']:
    return check_three(board, 2, 5, 8)

  elif check_three(board, 0, 4, 8) in ['X', 'O']:
    return check_three(board, 0, 4, 8)

  elif check_three(board, 2, 4, 6) in ['X', 'O']:
    return check_three(board, 2, 4, 6)

  elif open_spots(board) == []:
    return "D"

  else:
    return "-"

def tic_tac_toe():
  board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
  turn = 1
  while winner(board) == "-":
    if (turn % 2) == 1:
      player = "X"
      random_move(board, player)
    else:
      player = "O"
      random_move(board, player)
    turn += 1
    print()
  return winner(board)
