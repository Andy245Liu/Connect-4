

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

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    myGui.draw()
   
    
    if board.findState() == gameStateNotEnded:

    
        legalMoves = board.getLegalMoves()
        move = playerToMove.getMove(legalMoves, board.getBoard(), myGui)
  
        print(move)
        board.move(move, playerToMove.getPlayer())
        print("past move")
        myGui.draw()

        if playerToMove == redBot:
            playerToMove = yellow
        else:
            playerToMove = redBot
    
        #new added code begins to check for winner or draw
    
    if board.findState() == redVal:
        note = myGui.redWins()
        myGui.screen.blit(note[0], note[1])
        myGui.gameOver()
        
        playerToMove = redBot
        
      
        print("red wins")
    elif board.findState() == yellowVal:
        note = myGui.yellowWins()
        myGui.screen.blit(note[0], note[1])
        myGui.gameOver()
      
        
        print("yellow wins")
    elif board.findState() == tie:
        note = myGui.tie()
        myGui.screen.blit(note[0], note[1])
        myGui.gameOver()
        playerToMove = redBot
       
       
        print("draw")
    
 
        
        
    

    pygame.display.update()
       


    
  

    


#script to test neural net
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



        

    


    


