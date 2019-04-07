import random

def drawboard(board):

    print('   |   | ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('-----------')
    print('   |   | ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('-----------')
    print('   |   | ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])

def inputplayerletter():

     letter = ' '
     while not (letter == 'X' or letter == 'O'):
         print('Do you want to be X or O?')
         letter = input().upper()
     if letter == 'X':
         return ['X','O']
     else:
         return ['O','X']
    
    
    

def whogoesfirst():

    if random.randint(0,1) == 0:
        return ('computer')
    else:
        return ('player')

def playagain():

    print('Do u want to play again?(yes or no)')
    return input().lower().startswith('y')

def makemove(board,letter,move):
    board[move]=letter

def iswinner(bo,le):

    return ((bo[1] == le and bo[2] == le and bo[3] == le)or
            (bo[4] == le and bo[5] == le and bo[6] == le)or
            (bo[7] == le and bo[8] == le and bo[9] == le)or
            (bo[1] == le and bo[4] == le and bo[7] == le)or
            (bo[2] == le and bo[5] == le and bo[8] == le)or
            (bo[3] == le and bo[6] == le and bo[9] == le)or
            (bo[1] == le and bo[5] == le and bo[9] == le)or
            (bo[3] == le and bo[5] == le and bo[7] == le))

def getboardcopy(board):
    dupeboard=[]

    for i in board:
                   dupeboard.append(i)
    return dupeboard

def isspacefree(board,move):
     return board[move] == ' '
                  
def getplayermove(board):
    move = ' '

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isspacefree(board,int(move)):
           print('what is ur next move?(1-9)')
           move = input()
    return int(move)

def chooserandommovefromlist(board,moveslist):
    possiblemoves = []

    for i in moveslist:
        if isspacefree(board,i):
            possiblemoves.append(i)

    if len(possiblemoves)!=0:
        return random.choice(possiblemoves)
    else:
        return None
    
def getcomputermove(board,computerletter):

    if computerletter == 'X':
        playerletter = 'O'
    else:
        playerletter = 'X'

    for i in range(1,10):
        copy = getboardcopy(board)
        if isspacefree(copy,i):
            makemove(copy,computerletter,i)
            if iswinner(copy,computerletter):
                return i
            
    for i in range(1,10):
        copy = getboardcopy(board)
        if isspacefree(copy,i):
            makemove(copy,playerletter,i)
            if iswinner(copy,playerletter):
                return i

    move = chooserandommovefromlist(board,[1, 3, 7, 9])
    if move != None:
        return move
    if isspacefree(board,5):
        return 5
    return chooserandommovefromlist(board,[2, 4, 6, 8])


def isboardfull(board):

    for i in range(1,10):
        if isspacefree(board,i):
            return False
    return True

print('Welcome to tic tac toe!')

while True:
    theboard = [' ']*10
    playerletter,computerletter = inputplayerletter()
    turn = whogoesfirst()
    print('The '+turn+' will go first.')
    gameisplaying = True

    while gameisplaying:
        if turn == 'player':
            drawboard(theboard)
            move = getplayermove(theboard)
            makemove(theboard,playerletter,move)

            if iswinner(theboard,playerletter):
                drawboard(theboard)
                print('Hooray! You have won the game!')
                gameisplaying = False
            else:
                if isboardfull(theboard):
                    drawboard(theboard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            move = getcomputermove(theboard,computerletter)
            makemove(theboard, computerletter, move)

            if iswinner(theboard, computerletter):
                drawboard(theboard)
                print('The computer has beaten you! You lose.')
                gameisplaying = False
            else:
                if isboardfull(theboard):
                    drawboard(theboard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not playagain():
            break
       
