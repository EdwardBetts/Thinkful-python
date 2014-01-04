player1 = "X"
player2 = "O"
#le = ["X","O"]


board = [' ', ' ', ' ', ' ', ' ',
 ' ', ' ', ' ', ' ', ' ']
def board_game(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' ---------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' ---------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def winner(board,le):
	return ((board[7] == le and board[8] == le and board[9] == le) or # top
    (board[4] == le and board[5] == le and board[6] == le) or #  middle
    (board[1] == le and board[2] == le and board[3] == le) or #  bottom
    (board[7] == le and board[4] == le and board[1] == le) or # left side
    (board[8] == le and board[5] == le and board[2] == le) or #  middle
    (board[9] == le and board[6] == le and board[3] == le) or # right side
    (board[7] == le and board[5] == le and board[3] == le) or # diagonal
    (board[9] == le and board[5] == le and board[1] == le)) # diagonal

def getPosition(msg):
    position = input(msg)
    while position <= 0 or position > 9:
        print "ERROR! must be integer 1-9"
        position = input(msg)
    return position

positionList= []
def openSpace (positionList, position):
    for item in positionList:
        if item == position:
            print " position taken, try again"
            return True 
        item = item + 1

def errorCheck (i):
    if i > 9:
        print "incorrect position"
        return True    

def game(board,player1, player2):
    ticTac = True
    positionList= []
    while ticTac:
        positionList =[]
        gamePlaying = True
        while gamePlaying:
            i = int(raw_input("player 1: pick a position from 1-9"))
            if errorCheck==True:
                continue 
            if openSpace(positionList,i):
                continue
            board [i] = player1
            positionList.append(i)    
            print positionList
            print board_game(board)
            if winner(board, player1):
                print 'Hooray! Player 1 won the game!'
                gamePlaying = False
                ticTac = False
            else:   
                print "keep playing"
                contPlaying = True
                while contPlaying:
                    j = int(raw_input("player 2: pick a position from 1-9"))
                    if errorCheck==True:
                        continue
                    if openSpace(positionList,j):
                        continue      
                    board [j] = player2
                    positionList.append(j)
                    print board_game(board)
                    if winner(board, player2):
                        print 'Hooray! Player 2 won the game!'
                        contPlaying = False
                        gamePlaying = False
                        ticTac = False
                    else:   
                        print "keep playing"
                        contPlaying= False


game(board,player1, player2) 




# continue matching loops, not for loops. booleans for checking, 