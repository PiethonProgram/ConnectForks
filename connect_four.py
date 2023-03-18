def print_board(board):
    for i in board[::-1]:
        #loop in reverse direction
        for j in i:
            print(j, end=" ")
        print()

def initialize_board(num_rows, num_cols):
    #one liner that essentially returns an empty board of length num_cols
    #and height num_rows
    return ([["-" for columns in range(num_cols)]for rows in range(num_rows)])

#insert x or o into position on graph
def insert_chip(board, col, chip_type):
    for i,row in enumerate(board):
        if row[col]=="-": #check if empty and replace (goes bottom-up)
            row[col] = chip_type
            return(i)

def check_if_winner(board, col, row, chip_type):
    countdown = 0 #tracker
    whack=len(board[row])

    for i in range(whack):
        if board[row][i]==chip_type: # check if value is equal to other value
            countdown=countdown+1
            if countdown==4: #winner
                return(1)
        elif board[row][i] != chip_type : #reset countdown but progress through to see if there's another 4
            countdown = 0

    countdown = 0
    #checks each row for possible connect 4
    for i in range(4):
        if board[i][col]==chip_type:
            countdown=countdown+1
        else:
            break

    if countdown==4:
        return(1)
    else:
        return(0)


def main():

    #watching the TV show Wednesday so kinda took the rowan inspiration from there
    rowan = int(input("What would you like the height of the board to be? "))
    collin = int(input("What would you like the length of the board to be? "))
    maxey = rowan*collin

    #initialization
    board = initialize_board(rowan, collin)
    print_board(board)

    pl1='x'
    pl2='o'
    print("Player 1: ",pl1)
    print("Player 2: ",pl2)

    gamez=1
    turns = 0 # keep track of turns and make sure its under max number of moves
    while gamez == 1:
        insert = int(input("Player 1: Which column would you like to choose? "))
        chipper=insert_chip(board, insert, pl1)
        uno = check_if_winner(board, insert, chipper, pl1)
        turns=turns+1
        print_board(board)

        #if player 1 wins, then print statement
        if uno==1:
            print("Player 1 won the game!")
            exit()
        print() #new line print since ZyBooks is a picky software

        insert = int(input("Player 2: Which column would you like to choose? "))
        chipper = insert_chip(board, insert, pl2)
        dos = check_if_winner(board, insert, chipper, pl2)
        turns=turns+1
        print_board(board)

        #if player 2 wins, then print statement
        if dos==1:
            print("Player 2 won the game!")
            exit()
        print()

        #draw if all spots filled and no connected four
        if turns==maxey:
            print("Draw. Nobody wins.")
            exit()


if(__name__ == "__main__"):
    main()