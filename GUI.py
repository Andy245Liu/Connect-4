import pygame
import math
from Board import Board

redVal = -1
yellowVal = 1
gameStateNotEnded = 2
numRows = 6
numColumns = 7

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)



class Gui:
    def __init__(self, board):
        self.board = board
        self.X = 800
        self.Y = 600
        self.screen = pygame.display.set_mode((800,600))
        self.screen.fill((173,216,230))
        self.resetScreen()
        self.rectWidth = 100
        self.rectHeight = 600
        self.circSep = 45
        self.rectList = [pygame.Rect(0,0,self.rectWidth,self.rectHeight), 
                        pygame.Rect(10+self.rectWidth,0,self.rectWidth,self.rectHeight),
                        pygame.Rect(2*(10+self.rectWidth),0,self.rectWidth,self.rectHeight),
                        pygame.Rect(3*(10+self.rectWidth),0,self.rectWidth,self.rectHeight),
                        pygame.Rect(4*(10+self.rectWidth),0,self.rectWidth,self.rectHeight),
                        pygame.Rect(5*(10+self.rectWidth),0,self.rectWidth,self.rectHeight),
                        pygame.Rect(6*(10+self.rectWidth),0,self.rectWidth,self.rectHeight)]
        #here i, j refers to collumn, row, NOT row, column, so it will be the inverse of the format of the players' move (row, column)
        self.circList = [[[(50, 50), 30], [(50, 50+ 50+self.circSep), 30], [(50, 50+ 2*(50+self.circSep)), 30], [(50, 50+ 3*(50+self.circSep)), 30], [(50, 50+ 4*(50+self.circSep)), 30], [(50, 50+ 5*(50+self.circSep)), 30] ],
                         [[(160, 50), 30], [(160, 50+ 50+self.circSep), 30], [(160, 50+ 2*(50+self.circSep)), 30], [(160, 50+ 3*(50+self.circSep)), 30], [(160, 50+ 4*(50+self.circSep)), 30], [(160, 50+ 5*(50+self.circSep)), 30] ],
                         [[(270, 50), 30], [(270, 50+ 50+self.circSep), 30], [(270, 50+ 2*(50+self.circSep)), 30], [(270, 50+ 3*(50+self.circSep)), 30], [(270, 50+ 4*(50+self.circSep)), 30], [(270, 50+ 5*(50+self.circSep)), 30] ],
                         [[(380, 50), 30], [(380, 50+ 50+self.circSep), 30], [(380, 50+ 2*(50+self.circSep)), 30], [(380, 50+ 3*(50+self.circSep)), 30], [(380, 50+ 4*(50+self.circSep)), 30], [(380, 50+ 5*(50+self.circSep)), 30] ],
                         [[(490, 50), 30], [(490, 50+ 50+self.circSep), 30], [(490, 50+ 2*(50+self.circSep)), 30], [(490, 50+ 3*(50+self.circSep)), 30], [(490, 50+ 4*(50+self.circSep)), 30], [(490, 50+ 5*(50+self.circSep)), 30] ],
                         [[(600, 50), 30], [(600, 50+ 50+self.circSep), 30], [(600, 50+ 2*(50+self.circSep)), 30], [(600, 50+ 3*(50+self.circSep)), 30], [(600, 50+ 4*(50+self.circSep)), 30], [(600, 50+ 5*(50+self.circSep)), 30] ],
                         [[(710, 50), 30], [(710, 50+ 50+self.circSep), 30], [(710, 50+ 2*(50+self.circSep)), 30], [(710, 50+ 3*(50+self.circSep)), 30], [(710, 50+ 4*(50+self.circSep)), 30], [(710, 50+ 5*(50+self.circSep)), 30] ]
                         ]
        self.visited = [[0 for i in range(numRows)] for j in range(numColumns)]  
       # self.circleList
    def resetScreen(self):
        self.visited =  [[0 for i in range(numRows)] for j in range(numColumns)]  
    def draw(self):
        for rectangle in self.rectList:
            pygame.draw.rect(self.screen, blue, rectangle)
        for j in range(numColumns):
            for i in range(numRows):
                #if pygame.mouse.get_pressed()[0]:
                   # if pygame.mouse.get_pos()[0] <= self.rectWidth:
                  #      pygame.draw.circle(self.screen, yellow, self.circList[0][-1][0], self.circList[0][-1][1])
                 #   elif pygame.mouse.get_pos()[0] >= 10+self.rectWidth and pygame.mouse.get_pos()[0] <= 10+self.rectWidth +self.rectWidth:
                #        pygame.draw.circle(self.screen, yellow, self.circList[1][-1][0], self.circList[1][-1][1])
               # else:
                if self.visited[j][i] == 0:
                    pygame.draw.circle(self.screen, white, self.circList[j][i][0], self.circList[j][i][1])
                elif self.visited[j][i] == 1:
                    pygame.draw.circle(self.screen, yellow, self.circList[j][i][0], self.circList[j][i][1]) #the -1 index will need to be updated for the game.this is just a test
                else:
                    pygame.draw.circle(self.screen, red, self.circList[j][i][0], self.circList[j][i][1])

    def mouseAction(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True  
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #if pygame.mouse.get_pressed()[0]:
                        legalMoves = self.board.getLegalMoves()
                        if pygame.mouse.get_pos()[0] <= self.rectWidth:
                            #pygame.draw.circle(self.screen, yellow, self.circList[0][-1][0], self.circList[0][-1][1])
                            #check is this column is a legal move
                            for legalMove in legalMoves:
                                if legalMove[1] == 0:
                                    self.visited[0][legalMove[0]] = 1
                                    return [legalMove[0], 0]
                                    #break
                                
                        
                            
                        elif pygame.mouse.get_pos()[0] >= 10+self.rectWidth and pygame.mouse.get_pos()[0] <= 10+self.rectWidth +self.rectWidth:
                        # pygame.draw.circle(self.screen, yellow, self.circList[1][-1][0], self.circList[1][-1][1])
                            for legalMove in legalMoves:
                                if legalMove[1] == 1:
                                    self.visited[1][legalMove[0]] = 1
                                    return [legalMove[0], 1]
                                    #break
                            #self.visited[1][-1] = 1
                        elif pygame.mouse.get_pos()[0] >= 2*(10+self.rectWidth) and pygame.mouse.get_pos()[0] <= 2*(10+self.rectWidth) +self.rectWidth:
                            for legalMove in legalMoves:
                                if legalMove[1] == 2:
                                    self.visited[2][legalMove[0]] = 1
                                    return [legalMove[0], 2]
                                    #break
                            #self.visited[2][-1] = 1
                        elif pygame.mouse.get_pos()[0] >= 3*(10+self.rectWidth) and pygame.mouse.get_pos()[0] <= 3*(10+self.rectWidth) +self.rectWidth:
                            for legalMove in legalMoves:
                                if legalMove[1] == 3:
                                    self.visited[3][legalMove[0]] = 1
                                    return [legalMove[0], 3]
                                    #break
                            #self.visited[3][-1] = 1
                        elif pygame.mouse.get_pos()[0] >= 4*(10+self.rectWidth) and pygame.mouse.get_pos()[0] <= 4*(10+self.rectWidth) +self.rectWidth:
                            for legalMove in legalMoves:
                                if legalMove[1] == 4:
                                    self.visited[4][legalMove[0]] = 1
                                    return [legalMove[0], 4]
                                    #break
                            #self.visited[4][-1] = 1
                        elif pygame.mouse.get_pos()[0] >= 5*(10+self.rectWidth) and pygame.mouse.get_pos()[0] <= 5*(10+self.rectWidth) +self.rectWidth:
                            for legalMove in legalMoves:
                                if legalMove[1] == 5:
                                    self.visited[5][legalMove[0]] = 1
                                    return [legalMove[0], 5]
                                    #break
                        # self.visited[5][-1] = 1
                        elif pygame.mouse.get_pos()[0] >= 6*(10+self.rectWidth) and pygame.mouse.get_pos()[0] <= 6*(10+self.rectWidth) +self.rectWidth:
                            for legalMove in legalMoves:
                                if legalMove[1] == 6:
                                    self.visited[6][legalMove[0]] = 1
                                    return [legalMove[0], 6]
        #else:
         #   self.mouseAction()
                        #break
                #self.visited[6][-1] = 1
   # def computerMove(playerNeural): #needs the neural net play as input -> probably will need to add this on to the main looping function later on
    #    return playerNeural.getMove(self.board.getLegalMoves(), self.board, self)
    def redWins(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Red Wins!', True, red, blue)
        textRect = text.get_rect()
        textRect.center = (self.X // 2, self.Y // 2)
        return (text, textRect)  
    def yellowWins(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Yellow Wins!', True, yellow, blue)
        textRect = text.get_rect()
        textRect.center = (self.X // 2, self.Y // 2)  
        return (text, textRect)  
    def tie(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Game Over: Draw', True, green, blue)
        textRect = text.get_rect()
        textRect.center = (self.X // 2, self.Y // 2)  
        return (text, textRect)  
    def gameOver(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Game Over. Press Space to Start New Game.', True, white, green)
        textRect = text.get_rect()
        textRect.center = (800 // 2, 300 // 2)
        self.screen.blit(text, textRect)  
        #self.draw()
        
       # done = False
        #while not done:
           # print("in loop")
        for event in pygame.event.get():
           # print("in forrrrrrrrrrrrrrrr")
            if event.type == pygame.QUIT:
                #print("in quit")

                pygame.quit()
                quit()  
            elif event.type == pygame.KEYDOWN:
                #print("in keyyyyyyyyyyyyyyyyyyyyyyyy")
                if event.key == pygame.K_SPACE:
                    #print("in spaceeeeeeeeeeeeeeeeeeeeeeeee")
                    #done = True
                    self.board.resetBoard()
                    self.resetScreen()
                    return 0
                        
                        #gameOver = False
        

#code to test GUI
'''
pygame.init()


#gui = Gui()
#gameDisplay = pygame.display.set_mode((800,600))
#gameDisplay.fill((173,216,230))
board = Board()
myGui = Gui(board)
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    myGui.draw()
  
       # myGui.mouseAction()
       # pygame.display.update()
    #pixAr = pygame.PixelArray(gameDisplay)
    #pixAr[10][20] = red

    pygame.display.update()
'''


