def constboard(board):

  for i in range(0, 9):
    if ((i > 0) and (i % 3 == 0)):
      print("\n")
    if (board[i] == 0):
      print("_", end=" ")
    if (board[i] == -1):
      print("X", end=" ")
    if (board[i] == 1):
      print("O", end=" ")
  print("\n")


def analyzeboard(board):
  list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
          [0, 4, 8], [2, 4, 6]]
  for i in range(0, 8):
    #if(board[list[i][0]]!=0 and (board[list[i][0]]==board[list[i][1]] and board[list[i][0]]==board[list[i][2]])):
    if (board[list[i][0]] != 0
        and (board[list[i][0]] == board[list[i][1]] == board[list[i][2]])):
      return board[list[i][0]]
  return 0


def user1turn(board):
  pos = int(input("enter the position of X within 1 to 9: "))
  if (board[pos - 1] == 0):
    board[pos - 1] = -1
  else:
    print("wrong input")


def user2turn(board):
  pos = int(input("enter the position of O within 1 to 9: "))
  if (board[pos - 1] == 0):
    board[pos - 1] = 1
  else:
    print("wrong input")


def minmax(board, player):
  x = analyzeboard(board)
  if (x != 0):
    return (x * player)
  else:
    pos = -1
    value = -2
    for i in range(0, 9):
      if (board[i] == 0):
        board[i] = player
        score = -minmax(board, player * -1)
        board[i] = 0
        if (score > value):
          value = score
          pos = i
    if (pos == -1):
      return 0
    else:
      return value


def compturn(board):
  pos = -1
  value = -2
  for i in range(0, 9):
    if (board[i] == 0):
      board[i] = 1
      score = -minmax(board, -1)
      board[i] = 0
      if (score > value):
        value = score
        pos = i
  board[pos] = 1


def main():
  choice = int(input("1 for single player and 2 for multiplayer: "))
  board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  if (choice == 1):
    print("computer O and user1 X")
    player = int(input("1 for 1st and 2 for 2nd: "))
    for i in range(0, 9):
      if (analyzeboard(board) != 0):
        break
      if ((i + player) % 2 == 0):
        constboard(board)
        compturn(board)
      else:
        constboard(board)
        user1turn(board)

  else:
    print("user1 X and user2 O")
    player = int(input("1 for 1st and 2 for 2nd: "))
    for i in range(0, 9):
      if (analyzeboard(board) != 0):
        break
      if (i % 2 == 0):
        constboard(board)
        user1turn(board)
      else:
        constboard(board)
        user2turn(board)

  x = analyzeboard(board)
  if (x == 0):
    constboard(board)
    print("match draw!!!")
  if (x == -1):
    constboard(board)
    print("x wins")
  if (x == 1):
    constboard(board)
    print("O wins")


game = main()
print("game over")
