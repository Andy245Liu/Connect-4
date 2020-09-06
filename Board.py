import copy
redPlayer = 'r'
yellowPlayer = 'y'
redVal = -1
yellowVal = 1
empty = ' '
EMPTY_VAL = 0

gameStateX = -1
gameStateO = 1
gameStateDraw = 0
gameStateNotEnded = 2

numRows = 6
numColumns = 7
gameObjective = 4

class Board:
    '''
    class for the game board of connect 4

    '''
    def __init__(self):
        self.resetBoard()
    def resetBoard(self):
        
        self.board = [[EMPTY_VAL for i in range(numColumns)] for j in range(numRows)]  
 
        self.boardHistory = []
    def printBoard(self):
        #prints out the connect four game board
        for i in range(0, numRows):
            for j in range(0, numColumns):
                print(self.board[i][j], end=' ')
            print('')
    def getLegalMoves(self):
        legalMoves = []
        for i in range(numColumns):
            if self.board[numRows - 1] [i] == EMPTY_VAL:
                legalMoves.append([numRows-1, i])
            else:
                for j in range(numRows - 1):
                    if self.board[j][i] == EMPTY_VAL and self.board[1+j] [i] != EMPTY_VAL:
                        legalMoves.append([j,i])
        return legalMoves
    def findState(self):
       
    
        winnerFound = False
        winnerVal = 0

    #check for vertical winners
        if winnerFound == False:
            for j in range(numColumns):
                for i in range(numRows):
                    if self.board[i][j] != EMPTY_VAL:
                        verticalScore = 1
                        currentVal = self.board[i][j]
                        x = i
                        while(x + 1 < numRows):
                            if self.board[x+1][j] == currentVal:
                                verticalScore = verticalScore + 1
                                if verticalScore == gameObjective:
                                    #print("ver")
                                    winnerVal = currentVal
                                    winnerFound = True
                                    break
                            else:
                                break
                            x = x+1
                        if(winnerFound == True):
                            break
                if(winnerFound == True):
                    break
        
    #check for horizontal winners
        if winnerFound == False:
            for i in range(numRows):
                for j in range(numColumns):
                    if self.board[i][j] != EMPTY_VAL:
                        horizontalScore = 1
                        currentVal = self.board[i][j]
                        x = j
                        #print(x)
                        while(x + 1 < numColumns):
                            if self.board[i][x+1] == currentVal:
                                #print(x+1)
                                horizontalScore = horizontalScore + 1
                                if horizontalScore == gameObjective:
                                    #print("hor")
                                    winnerVal = currentVal
                                    winnerFound = True
                                    break
                            else:
                                break
                            x = x+1
                        if(winnerFound == True):
                            break
                #if(winnerFound == True):
                #    break
    
    #check for left diagonal winners
        if winnerFound == False:
            for i in range(numRows):
                for j in range(numColumns):
                    if self.board[i][j] != EMPTY_VAL:
                        leftDiagonalScore = 1
                        currentVal = self.board[i][j]
                        x = i
                        y = j
                        while(x + 1 < numRows and y+1 < numColumns):
                            if self.board[x+1][y+1] == currentVal:
                                leftDiagonalScore = leftDiagonalScore + 1
                                if leftDiagonalScore == gameObjective:
                                   # print("left d")
                                    winnerVal = currentVal
                                    winnerFound = True
                                    break
                            else: 
                                break
                            x = x+1
                            y = y+1
                        if(winnerFound == True):
                            break
                if(winnerFound == True):
                    break
    #check for right diagonal winners
        if winnerFound == False:
            for i in range(numRows):
                for j in range(numColumns):
                    if self.board[i][j] != EMPTY_VAL:
                        rightDiagonalScore = 1
                        currentVal = self.board[i][j]
                        x = i
                        y = j
                        while(x-1 >= 0 and y+1 < numColumns):
                            if self.board[x-1][y+1] == currentVal:
                                rightDiagonalScore = rightDiagonalScore + 1
                                if rightDiagonalScore == gameObjective:
                                    #print("right d")
                                    winnerVal = currentVal
                                    winnerFound = True
                                    break
                            else:
                                break
                            x = x-1
                            y = y+1
                    if(winnerFound == True):
                        break
                if(winnerFound == True):
                    break
                    


       
            
#if winner, declare winner - else continue game
        if winnerFound == True:
           # print('winner')
            return winnerVal
        else:
           # print("in else")
            isDone = True
            for i in range(numRows):
                for j in range(numColumns):
                    if self.board[i][j] == EMPTY_VAL:
                        isDone = False

            if isDone == True:
                #print("in draw")
                return gameStateDraw
            else:
                #print("in not ended")
                return gameStateNotEnded
       
                   

        
        
        
    #establishes a player's move (row, column number)
    def move(self, move, player):
        self.board[move[0]][move[1]] = player
        self.boardHistory.append(copy.deepcopy(self.board))
    def getBoardHistory(self):
        return self.boardHistory

    def getBoard(self):
        return self.board


