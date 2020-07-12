from pprint import pprint as pp
import copy, random

def create_grid(Rows, Columns):
   #Creates the 2D Data Grid
   grid = []
   for row in range(Rows):
       row = []
       for col in range(Columns):
           row.append('0')
       grid.append(row)
   return grid

def computer_place_ships(board, ships):
    for ship in ships.keys():

        # generate random coordinates and validate the postion
        valid = False
        while (not valid):

            x = random.randint(1, 10) - 1
            y = random.randint(1, 10) - 1
            o = random.randint(0, 1)
            if o == 0:
                ori = "v"
            else:
                ori = "h"
            valid = validate(board, ships[ship], x, y, ori)

        # place the ship
        print
        "Placing a/an " + ship
        board = place_ship(board, ships[ship], ship[0], ori, x, y)

    return board


def place_ship(board, ship, s, ori, x, y):
    # place ship based on orientation
    if ori == "v":
        for i in range(ship):
            board[x + i][y] = s
    elif ori == "h":
        for i in range(ship):
            board[x][y + i] = s

    return board



def display_grid(grid, Columns):
    # Prints the labels for the grid
    print("User Grid")
    column_names = 'abcdefghijklmnopqrstuvwxyz'[:Columns]
    print('  | ' + ' | '.join(column_names.upper()) + ' |')
    for number, row in enumerate(grid):
        print(number + 1, '| ' + ' | '.join(row) + ' |')

def display_computer(grid, Columns):
   #Prints the labels for the grid
   print("Computer Grid")
   column_names = 'abcdefghijklmnopqrstuvwxyz'[:Columns]
   print('  | ' + ' | '.join(column_names.upper()) + ' |')
   for number, row in enumerate(grid):
      print(number + 1, '| ' + ' | '.join(row) + ' |')


def validate(board, ship, x, y, ori):
    # validate the ship can be placed at given coordinates
    if ori == "v" and x + ship > 10:
        return False
    elif ori == "h" and y + ship > 10:
        return False
    else:
        if ori == "v":
            #ship length, strip will remove all leading and trailing spaces
            for i in range(ship):
                if board[x + i][y].strip() != '0':
                    return False
        elif ori == "h":
            for i in range(ship):
                if board[x][y + i].strip() != '0':
                    return False

    return True

def random_row(grid):
   #Makes a random row integer
   return random.randint(1,len(grid))

def random_col(grid):
   #Makes a random column integer
   return random.randint(1,len(grid[0]))

def update_gridHit(usergrid, GuessRow, GuessColumn, compgrid, shiphit):
       usergrid[GuessRow-1][GuessColumn-1] = 'X'
       #check if ship is sunk
       if shiphit == 'B*':
           compgrid[GuessRow - 1][GuessColumn - 1] = 'B*'
           if check_ship_sunk(compgrid, shiphit, 3):
               print("You sunk the Battleship! Congratulations!")
       if shiphit == 'S*':
           compgrid[GuessRow - 1][GuessColumn - 1] = 'S*'
           if check_ship_sunk(compgrid, shiphit, 2):
               print("You sunk the Submarine! Congratulations!")
       if shiphit == 'D*':
           compgrid[GuessRow - 1][GuessColumn - 1] = 'D*'
           print("You sunk the Destroyer! Congratulations!")

def check_ship_sunk(compgrid, shiphit, shiplen):
    hitb = 0
    #check all rows and columns to if the length of ship is equal to the hitb
    for row in range(10):
        for col in range(10):
            if hitb == shiplen:
                return True
            if compgrid[row][col] == shiphit:
               hitb +=1


    return False



def update_gridMiss(grid, GuessRow, GuessColumn):
        grid[GuessRow-1][GuessColumn-1] = '-'

def play(player, compgrid, usergrid):
   print(player + "'s turn")
   guessrow = int(input("What row do you guess? \n"))
   guesscolumn = int(input("What column do you guess? \n"))
   hitB = ''

   hit = 0
   #check which ship is hit and and update the computer grid  and user grid
   if (compgrid[guessrow- 1][guesscolumn - 1] == 'B') or (compgrid[guessrow - 1][guesscolumn- 1] == 'S') or (compgrid[guessrow - 1][guesscolumn - 1] == 'D'):
       if(compgrid[guessrow-1][guesscolumn-1] == 'B'):
           hitB = 'B*'
       if (compgrid[guessrow - 1][guesscolumn - 1] == 'S'):
           hitB = 'S*'
       if (compgrid[guessrow - 1][guesscolumn - 1] == 'D'):
           hitB = 'D*'
       update_gridHit(usergrid, guessrow, guesscolumn, compgrid,hitB)
       display_grid(usergrid, 10)
       print("You hit the battleship! Congratulations!")
       hit = 1
   else:
       if (guessrow  < 1 or guessrow > 10) or (guesscolumn < 1 or guesscolumn > 10):
           # Warning if the guess is out of the board
           print("Outside the set grid. Please pick a number within it your Rows and Columns.")

       elif usergrid[guessrow - 1][guesscolumn - 1] == '-':
           # If "X" is there than print that it missed
           print("You guessed that already.")

       else:
           # Updates the grid with an "-" saying that you missed the ship

           print("You missed the ship.")
           update_gridMiss(usergrid, guessrow, guesscolumn)
           display_grid(usergrid, 10)
   return hit


def main():
    Answer = "NaN"
    playerstart = 1
    #ships array of different lengths
    ships = {"Battleship": 3,
             "Submarine": 2,
             "Destroyer": 1}
    print("Welcome to battleship!")
    player_1 = input("Enter first name: ")

    grid = create_grid(10, 10)
    display_grid(grid, 10)


    comp_board = copy.deepcopy(grid)
    comp_board = computer_place_ships(comp_board,ships)
    display_computer(comp_board, 10)
    turns = 0
    turns = 0
#play the game for 12 turns
    while turns != 12:
       play(player_1, comp_board, grid)
       turns += 1
       if turns >= 12:
         print("Game over! You ran out of tries")


if __name__ == "__main__":
     main()

