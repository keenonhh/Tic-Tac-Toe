# Practice environment for python
#! python3
import random
import copy

# function that will print the current board state
def printBoard(theBoard):
    print('   |   |')
    print(' ' + theBoard['Top-L'] + ' | ' + theBoard['Top-M'] + ' | ' + theBoard['Top-R'])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + theBoard['Center-L'] + ' | ' + theBoard['Center'] + ' | ' + theBoard['Center-R'])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + theBoard['Bottom-L'] + ' | ' + theBoard['Bottom-M'] + ' | ' + theBoard['Bottom-R'])
    print('   |   |')

# get the character the player will use
def getPlayerLetter():
    playerChar = ''

    # loop until the player inputs a valid choice
    while not (playerChar == 'X' or playerChar == 'O'):
        print('Do you want to be \'X\' or \'O\'?')
        # uppercase player input in case of lower case x or o
        playerChar = input().upper()

    # return list with playerChar first and computer char second
    if playerChar == 'X':
        return ['X', 'O']

    else:
        return ['O', 'X']

# use random int to decide who goes first   
def goFirst():
    if random.randint(1, 2) == 1:
        return 'Computer'
    else:
        return 'Player'

# ask the player if they want to keep playing until they input Y or N
def playAgain():
    choice = ''
    while choice != 'Y' and choice != 'N':
        print('Do you want to play again? (Y/N)')
        choice = input().upper()
    return choice == 'Y'

# prompt the player to select a valid move and return that move
def playerMove(theBoard):
    move = ' '
    while move not in ['Top-L', 'Top-M', 'Top-R', 'Center-L', 'Center', 'Center-R', 'Bottom-L', 'Bottom-M', 'Bottom-R'] or not freeSpace(theBoard, move):
        print('Select your move. (Top-L, Top-M, Top-R, Center-L, Center, Center-R, Bottom-L, Bottom-M, Bottom-R)')
        move = input()
    return move
    
# copies the board for the AI to check for it's next move
def copyBoard(theBoard):
    boardCopy = copy.deepcopy(theBoard)
    return boardCopy

# function that returns true if the player has met a win condition, to be called after every move
def winner(theBoard, letter):
    # if the player has three across top
    return ((theBoard['Top-L'] == letter and theBoard['Top-M'] == letter and theBoard['Top-R'] == letter) or
    # three across center
    (theBoard['Center-L'] == letter and theBoard['Center'] == letter and theBoard['Center-R'] == letter) or
    # three across bottom
    (theBoard['Bottom-L'] == letter and theBoard['Bottom-M'] == letter and theBoard['Bottom-R'] == letter) or
    # three vertical left side
    (theBoard['Top-L'] == letter and theBoard['Center-L'] == letter and theBoard['Bottom-L'] == letter) or
    # three vertical center
    (theBoard['Top-M'] == letter and theBoard['Center'] == letter and theBoard['Bottom-M'] == letter) or
    # three vertical right
    (theBoard['Top-R'] == letter and theBoard['Center-R'] == letter and theBoard['Bottom-R'] == letter) or
    # diagonal left to right
    (theBoard['Top-L'] == letter and theBoard['Center'] == letter and theBoard['Bottom-R'] == letter) or
    # diagonal right to left
    (theBoard['Top-R'] == letter and theBoard['Center'] == letter and theBoard['Bottom-L'] == letter))

# checks to see if the space is free
def freeSpace(theBoard, move):
    return theBoard[move] == ' '
      
# a list of random moves that are available to the AI
def possibleMoves(theBoard, moveList):
    possibleMoves = []
    for i in moveList:
        if freeSpace(theBoard, i):
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
# update the board with the specified move
def makeMove(theBoard, letter, move):
    theBoard[move] = letter

# computer move algorithm
def computerMove(theBoard, compChar):
    if compChar == 'X':
        playerChar = 'O'
    else:
        playerChar = 'X'
    
    # check if computer can win with next move
    for i in ['Top-L', 'Top-M', 'Top-R', 'Center-L', 'Center', 'Center-R', 'Bottom-L', 'Bottom-M', 'Bottom-R']:
        copy = copyBoard(theBoard)
        if freeSpace(copy, i):
            makeMove(copy, compChar, i)
            if winner(copy, compChar):
                return i

    # check if player can win with nect move
    for i in ['Top-L', 'Top-M', 'Top-R', 'Center-L', 'Center', 'Center-R', 'Bottom-L', 'Bottom-M', 'Bottom-R']:
        copy = copyBoard(theBoard)
        if freeSpace(copy, i):
            makeMove(copy, playerChar, i)
            if winner(copy, playerChar):
                return i

    # if no winner with next move try to move to a corner
    move = possibleMoves(theBoard, ['Top-L', 'Top-R', 'Bottom-L', 'Bottom-R']) 
    if move != None:
        return move
    
    # try to take the center if corners are taken
    if freeSpace(theBoard, 'Center'):
        return 'Center'

    # if center and corners are taken choose a side square
    return possibleMoves(theBoard, ['Top-M', 'Center-L', 'Center-R', 'Bottom-M']) 
 
# check to make sur ethe board is not full (Tie game)
def boardFull(theBoard):
    for i in ['Top-L', 'Top-M', 'Top-R', 'Center-L', 'Center', 'Center-R', 'Bottom-L', 'Bottom-M', 'Bottom-R']:
        if freeSpace(theBoard, i):
            return False
    return True


##### GAME STARTS HERE #####
print('Welcome to Tic-Tac-Toe!')

while True:
    # define a dictionary to hold the empty board state
    theBoard = {'Top-L': ' ', 'Top-M': ' ', 'Top-R': ' ', 'Center-L': ' ', 'Center': ' ', 'Center-R': ' ', 'Bottom-L': ' ', 'Bottom-M': ' ', 'Bottom-R': ' '}
    playerChar, compChar = getPlayerLetter()
    turn = goFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        # if player's turn
        if turn =='Player':
            printBoard(theBoard)
            move = playerMove(theBoard)
            makeMove(theBoard, playerChar, move)

            if winner(theBoard, playerChar):
                printBoard(theBoard)
                print('You Won!!!')
                gameIsPlaying = False
            else:
                if boardFull(theBoard):
                    printBoard(theBoard)
                    print('It\'s a tie!!!')
                    break
                else:
                    turn = 'Computer'

        else:
            # if computers turn
            move = computerMove(theBoard, compChar)
            makeMove(theBoard, compChar, move)

            if winner(theBoard, compChar):
                printBoard(theBoard)
                print('The computer beat you!!!')
                gameIsPlaying = False
            else:
                if boardFull(theBoard):
                    printBoard(theBoard)
                    print('It\'s a tie!!!')
                    break
                else:
                    turn = 'Player'

    if not playAgain():
        break
    