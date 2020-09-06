
#import numpy as np # For numerical fast numerical calculations
#import matplotlib.pyplot as plt # For making plots
#import pandas as pd # Deals with data
#import seaborn as sns # Makes beautiful plots
#from sklearn.preprocessing import StandardScaler # Testing sklearn
#import tensorflow # Imports tensorflow
#import keras # Imports keras









#print("hello")
'''
 rowPos = currentPos[0]
        columnPos = currentPos[1]
        val = self.board[rowPos][columnPos]
      #  print(val)
       
     
        horizontalScore = 0
        rightDiagonalScore = 0
        leftDiagonalScore = 0
    #move down a column to count
        if winnerFound == False:

            r = rowPos
            c = columnPos
            while(r < numRows):
              #  print("in first loop")
                #print(r)
                if self.board[r][c] == val:
                   # print("row increase")
                    verticalScore += 1
                    if verticalScore == gameObjective:
                        winnerFound = True
                        winnerVal = val
                        break
                else:
                    #print("in exit")
                    break
                r +=1
                
#move up a column to count
     #   if winnerFound == False:
      #      r = rowPos
       #     c = columnPos
        #    while(r >= 0):
              
         #       if self.board[r][c] == val:
           #         verticalScore += 1
          #      if verticalScore == gameObjective:
            #        winnerFound = True
             #       winnerVal = val
              #      break
               # else:
                #    break
                #r = r-1       
#move right in a row to count
        if winnerFound == False:
            r = rowPos
            c = columnPos
            while(c < numColumns):
              
                if self.board[r][c] == val:
                    horizontalScore += 1
                    if horizontalScore == gameObjective:
                        winnerFound = True
                        winnerVal = val
                        break
                else:
                    break
                c = c + 1
#move left in a row to count
        if winnerFound == False:
            r = rowPos
            c = columnPos
            while(c >= 0):
              
                if self.board[r][c] == val:
                    horizontalScore += 1
                    if horizontalScore == gameObjective:
                        winnerFound = True
                        winnerVal = val
                        break
                else:
                    break
                c = c-1  
#move right then up to count
        if winnerFound == False:
            r = rowPos
            c = columnPos
            while(r >= 0 and c < numColumns):
              
                if self.board[r][c] == val:
                    rightDiagonalScore += 1
                    if rightDiagonalScore == gameObjective:
                        winnerFound = True
                        winnerVal = val
                        break
                else:
                    break
                r = r-1
                c = c+1   
#move left then down to count
        if winnerFound == False:
            r = rowPos
            c = columnPos
            while(r < numRows and c >= 0):
              
                if self.board[r][c] == val:
                    rightDiagonalScore += 1
                    if rightDiagonalScore == gameObjective:
                        winnerFound = True
                        winnerVal = val
                        break
                else:
                    break
                r = r+1
                c = c-1
#move left then up to count
        if winnerFound == False:
            r = rowPos
            c = columnPos
            while(r >= 0 and c >= 0):
              
                if self.board[r][c] == val:
                    leftDiagonalScore += 1
                    if leftDiagonalScore == gameObjective:
                        winnerFound = True
                        winnerVal = val
                        break
                else:
                    break
                r = r-1
                c = c-1 
#move right then down to count  
        if winnerFound == False:
            r = rowPos
            c = columnPos
            while(r < numRows and c < numColumns):
              
                if self.board[r][c] == val:
                    leftDiagonalScore += 1
                    if leftDiagonalScore == gameObjective:
                        winnerFound = True
                        winnerVal = val
                        break
                else:
                    break
                r = r+1
                c = c+1 
                '''
from Board import Board
from Player import  Player
from Controller import GameController
from NeuralNet import Model
from GUI import Gui
import pygame

redVal = -1
yellowVal= 1
tie = 0
gameStateNotEnded = 2

white = (255,255,255)
black = (0,0,0)

r = (255,0,0)
g = (0,255,0)
b = (0,0,255)
y = (255,255,0)


pygame.init()

#train the neuralnet

game1 = Board()
testGui = Gui(game1)
redTrain = Player(redVal, strategy='random')
yellowTrain = Player(yellowVal, strategy='random')
gameController = GameController(game1, redTrain, yellowTrain)
print ("Both players with random strategies")
gameController.gameStimulation(1000, testGui)

model = Model(42, 3, 50, 100) #originally 100 epochs
model.train(gameController.getTrainingHistory())

board = Board()
myGui = Gui(board)
 


redBot = Player(redVal, strategy='model', model=model)
yellow = Player(yellowVal, strategy='picked')
myController = GameController(board, redBot, yellow)
playerToMove = redBot
#gameOver = False
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    myGui.draw()
   
    
    if board.findState() == gameStateNotEnded:

    
        legalMoves = board.getLegalMoves()
        move = playerToMove.getMove(legalMoves, board.getBoard(), myGui)
    # while move== None:
        #    move = playerToMove.getMove(legalMoves, board.getBoard(), myGui)
        print(move)
        board.move(move, playerToMove.getPlayer())
        print("past move")
        myGui.draw()
        #pygame.display.update()
        if playerToMove == redBot:
            playerToMove = yellow
        else:
            playerToMove = redBot
        #pygame.display.update()
        #new added code begins to check for winner or draw
    
    if board.findState() == redVal:
        note = myGui.redWins()
        myGui.screen.blit(note[0], note[1])
        myGui.gameOver()
        
        playerToMove = redBot
        
        #gameOver = True
        print("red wins")
    elif board.findState() == yellowVal:
        note = myGui.yellowWins()
        myGui.screen.blit(note[0], note[1])
        myGui.gameOver()
      
        #gameOver = True
        print("yellow wins")
    elif board.findState() == tie:
        note = myGui.tie()
        myGui.screen.blit(note[0], note[1])
        myGui.gameOver()
        playerToMove = redBot
       
        #gameOver = True
        print("draw")
    
    #if gameOver == True:
     #   print('in end decide')
        
        
    

    pygame.display.update()
        #pygame.display.update()



    
    #pygame.display.update()
    


   
    #myController.play(myGui)



   # myController.play(myGui)
  
       # myGui.mouseAction()
       # pygame.display.update()
    #pixAr = pygame.PixelArray(gameDisplay)
    #pixAr[10][20] = red

    


#script to train neural net
'''
if __name__ == "__main__":
    game1 = Board()
    red = Player(redVal, strategy='random')
    yellow = Player(yellowVal, strategy='random')

    gameController = GameController(game1, red, yellow)
    print ("Both players with random strategies")
    gameController.gameStimulation(1000)

    model = Model(42, 3, 50, 100)
    model.train(gameController.getTrainingHistory())

    redBot = Player(redVal, strategy='model', model=model)
    yellowBot = Player(yellowVal, strategy='model', model=model)

    game2 = Board()
    gameController = GameController(game2, redBot, yellow)
    print("Red Player as Neural Network")
    gameController.gameStimulation(1000)
'''



        

    


    


