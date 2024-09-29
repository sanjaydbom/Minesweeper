import pygame
import Mine
from Settings import *

class Minesweeper():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.mine = Mine.Mine(LENGTH,WIDTH)
        self.not_started = True
        self.run = True


    def show_board(self):
        self.screen.fill(CELL_COLOR)
        for i in range(LENGTH):
            for j in range(WIDTH):
                pygame.draw.rect(self.screen, BACKGROUND_COLOR, self.mine.sprite_grid[i][j],BORDER_THICKNESS)
                if(self.mine.grid[i][j].is_clicked):
                    textTitle = FONT.render(str(self.mine.grid[i][j].num_surrounding), True, TEXT_COLOR)
                    rawText = textTitle.get_rect(center= ((self.mine.sprite_grid[i][j].x +50)//2, (self.mine.sprite_grid[i][j].y +50)//2))
                    self.screen.blit(textTitle, textTitle.get_rect(center = (self.mine.sprite_grid[i][j].x +50//2, self.mine.sprite_grid[i][j].y +50//2)))
                if(self.mine.grid[i][j].flagged):
                    self.screen.blit(flag,self.mine.sprite_grid[i][j])

    def event_handler(self, event):
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pressed = pygame.mouse.get_pressed()
                    pos = pygame.mouse.get_pos()
                    for i in range(LENGTH):
                        for j in range(WIDTH):
                            if self.mine.sprite_grid[i][j].collidepoint(pos):
                                k = event.button
                                self.move(i,j,k)

    def getMineField(self):
        return self.mine             

    def move(self,i,j,k):
        if(self.not_started):
            self.mine.set_grid(NUM_BOMBS,i,j)
            self.not_started = False
        if k == 1:
            if(self.mine.click(i,j) == -1):
                self.run = False
        elif k == 3:
            self.mine.flag(i,j)
            
    def start(self):
        pygame.init()
        while self.run:
            if self.mine.is_won():
                self.run = False
                print("You won")

            self.show_board()

            for event in pygame.event.get():
                self.event_handler(event)
            
            pygame.display.update()

        pygame.quit()

m = Minesweeper()

m.start()

    
    
        