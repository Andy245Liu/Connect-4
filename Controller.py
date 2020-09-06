import copy
redVal = -1
yellowVal = 1
gameStateNotEnded = 2

class GameController:
    def __init__(self, game, redPlayer, yellowPlayer):
        self.game = game
        self.redPlayer = redPlayer
        self.yellowPlayer = yellowPlayer
        self.trainingHistory = []
    #stores each move, the board, and the outcome to be used for training set on keras
    def play(self, gui):
        
        playerToMove = self.redPlayer
        while self.game.findState() == gameStateNotEnded:
            legalMoves = self.game.getLegalMoves()
            move = playerToMove.getMove(legalMoves, self.game.getBoard(), gui)
          
            print(move)
            self.game.move(move, playerToMove.getPlayer())
            print("past move")
            if playerToMove == self.redPlayer:
                playerToMove = self.yellowPlayer
            else:
                playerToMove = self.redPlayer
        #new added code begins to check for winner or draw
        if self.game.findState() == redVal:
            note = gui.redWins()
            gui.screen.blit(note[0], note[1])
            print("red wins")
        elif self.game.findState() == yellowVal:
            note = gui.yellowWins()
            gui.screen.blit(note[0], note[1])
            print("yellow wins")
        else:
            note = gui.tie()
            gui.screen.blit(note[0], note[1])
            print("draw")
        #new added code ends
        #for event in self.game.getBoardHistory():
         #   self.trainingHistory.append((self.game.findState(), copy.deepcopy(event)))
    def playNoGUI(self, gui):
        playerToMove = self.redPlayer
        while self.game.findState() == gameStateNotEnded:
            legalMoves = self.game.getLegalMoves()
            move = playerToMove.getMove(legalMoves, self.game.getBoard(), gui)
            self.game.move(move, playerToMove.getPlayer())
            if playerToMove == self.redPlayer:
                playerToMove = self.yellowPlayer
            else:
                playerToMove = self.redPlayer
        for event in self.game.getBoardHistory():
            self.trainingHistory.append((self.game.findState(), copy.deepcopy(event)))

    #stimulates many games, used for training AI
    
    def gameStimulation(self, numberOfGames, gui):
        redPlayerWins = 0
        yellowPlayerWins = 0
        draws = 0
        for i in range(numberOfGames):
            self.game.resetBoard()
            self.playNoGUI(gui)
            if self.game.findState() == redVal:
                redPlayerWins = redPlayerWins + 1
            elif self.game.findState() == yellowVal:
                yellowPlayerWins = yellowPlayerWins + 1
            else:
               
                draws = draws + 1
            totWins = redPlayerWins + yellowPlayerWins + draws
        print('Red Wins: ' + str(int(redPlayerWins * 100 / totWins)) + '%')
        print('Yellow Wins: ' + str(int(yellowPlayerWins * 100 / totWins)) + '%')
        print('Draws: ' + str(int(draws * 100 / totWins)) + '%') 
       
    
    def getTrainingHistory(self):
        return self.trainingHistory
    




        
