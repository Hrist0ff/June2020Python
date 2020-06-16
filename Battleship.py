from random import randint
def a():
    board = []
    num=[]
    for i in range(5):
        board.append(5 * ["O"])
       
    remaining=6
    guessed=0

    print ("-" * 50)
    print ("- Нека играем на параходи! ")
    print ("- Изберете между 0 и 4 ред и колона")
    print ("- Имате " + str(remaining) + " останали опита,за да победите играта") 
    print ("-" * 50)
    print("Поле за игра")
    print("-" * 16)

    print(" ", " ".join("12345"))
    for letter, row in zip("ABCDE", board):
        print(letter, " ".join(row))

    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board[0]) - 1)

    turn = 1
    for attempt in range(1,remaining):
      print ("\n")
      guess_row = int(input("Познайте ред (0 - 4) :"))
      guess_col = int(input("Познайте колона (0 - 4) :"))

      if guess_row == ship_row and guess_col == ship_col:
          print ("Поздравления! Вие потопихте моя параход!")
          break
      else:
          if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
              print ("Числото е твърде голямо.")
          if(board[guess_row][guess_col] == "X"):
              print ("Вече е познато!!!")
          else:
              print ("Изпуснахте кораба!")
              board[guess_row][guess_col] = "X"

          print ("Опит %d \n" % (turn)) 
          print("Игра на параходи")
          print("-" * 16)
          print(" ", " ".join("12345"))
          for letter, row in zip("ABCDE", board):
            print(letter, " ".join(row))

          turn = turn + 1
          
          if turn == remaining:
              print ("Играта свърши")
