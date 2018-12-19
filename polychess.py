"""
@author: Team Alpha0
"""

##python-chess import
#https://github.com/niklasf/python-chess
import chess
from minMax import MinMax
import time

## Is the game ready to end ?
# Search if an ending condition has been triggered.

def finDuGame (board):
    #do we have a winner?
    if (board.is_game_over() or board.is_stalemate() or board.is_insufficient_material()):
        print("The game is over")
        #print(board.result())
        #return False
    elif (board.is_fivefold_repetition() or board.is_seventyfive_moves()):
        print("The game is over because 5 repetitions or 75 moves without capture")
        #print(board.result())
        return False
    else:
        return True

## What is the move wanted by the player ?
# Until the move written by the player is impossible,
# we ask another time what move he want to do.

def mouvementDemande (board):

    while ("The move isn't possible or isn't legal"):
        possibleMoves = board.legal_moves
        temp = input("What move do you want to do (do) : ")
        if (temp == 'q'):
            return ["q", 0]
        mouv = chess.Move.from_uci(temp)
        if (mouv in possibleMoves):
            return (temp, mouv)
        else:
            print("The move isn't possible or isn't legal")

## Main function for the program.
# The backbone of the program, with the gestion of the game.
# Features loading/saving gestion, play modes and the game.

def main ():

    # Check how the player want to play :
    # Player vs Computer or Computer vs Computer
    PLAYER = False;
    jeu = input ("Do you want to play against AI (1) or see an AI play against another AI (2) ?\n")
    if (int(jeu) < 2):
        PLAYER = True

    #set the board to its initial position
    #corresponding to: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
    board = chess.Board()
    movement = [0, 0]
    while (finDuGame(board) and movement[0] != 'q'):
        print("SAVING GAME HERE")

        # Player versus AI

        if (PLAYER == True):
            movement = mouvementDemande(board)
            if (movement[0] != "q"):
                board.push(movement[1])
                print("")
                print(board)
                print("Play AI here")

        # AI versus AI

        else:
            print("Play AI vs AI here")

"""
    Start Programm
"""

main()
print ("You have quitted the game by force. See you next time !")


#print the board on the console
"""print(board)

#SVG render for the board is possible in Jupyter Notebook
#board

#get all the legal moves for the current position
moves = board.legal_moves

#how many moves are available?
print(moves.count())

#iterate over all the moves
for move in moves:

    #display the move
    print(move)

    #save the current position
    current_board = board

    #do the move
    board.push(move)

    #display the board
    print(board)

    #number of black moves
    print("Black moves:" + str(board.legal_moves.count()))

    #undo the move
    board.pop()

    finDuGame(board)"""

"""
THE TESTS
"""
"""
#set the board to its initial position
#corresponding to: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
board = chess.Board()


a = mouvementDemande ()
print ("a : ", a)
print(a[0])
#save the current position
current_board = board
#do the move
board.push(a[1])
#display the board
print(board)

print("\nPlayer 2 :")

a = mouvementDemande ()
print ("a : ", a)
print(a[0])
#save the current position
current_board = board
#do the move
board.push(a[1])
#display the board
print(board)
"""
