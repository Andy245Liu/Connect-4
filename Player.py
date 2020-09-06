import random
import copy
import pygame
redVal = -1
yellowVal = 1
class Player:
    def __init__(self, value, strategy= 'random', model=None):
        self.value = value
        self.strategy = strategy
        self.model = model
    #move with random model or with keras learning model
    def getMove(self, legalMoves, board, gui):#addition of GUI input to let user pick a move
        if self.strategy == "random":
            return legalMoves[random.randrange(0, len(legalMoves))]
        #new option to let player play
        elif self.strategy== "picked":
            
            return gui.mouseAction()
        else:
            maxValue = 0
            bestMove = legalMoves[0]
            for legalMove in legalMoves:
                boardCopy = copy.deepcopy(board)
                boardCopy[legalMove[0]][legalMove[1]] = self.value
                if self.value == redVal:
                    value = self.model.predict(boardCopy, 2)
                else:
                    value = self.model.predict(boardCopy, 0)
                if value > maxValue:
                    maxValue = value
                    bestMove = legalMove
            gui.visited[bestMove[1]][bestMove[0]] = -1
            return bestMove

    def getPlayer(self):
        return self.value

