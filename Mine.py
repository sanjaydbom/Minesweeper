import Cell
from random import *
import pygame
from Settings import *

class Mine():
    def __init__(self,length,width):
        self.grid = [[Cell.Cell() for i in range(width)] for j in range(length)]
        self.sprite_grid = [[pygame.Rect(CELL_SIZE*i,CELL_SIZE*j,CELL_SIZE,CELL_SIZE) for i in range(width)] for j in range(length)]
        self.width = width
        self.length = length
        self.num_opened = 0
        self.bombs = 0

    def set_grid(self,num,i,j):
        self.bombs = num
        while(num > 0):
            w = randint(0 , self.width-1)
            l = randint(0 , self.length-1)
            if(abs(l-i) > 1 or abs(w-j) > 1) and self.grid[l][w].make_bomb():
                num = num - 1
                
        for i in range(self.length):
            for j in range(self.width):
                if(self.grid[i][j].is_bomb()):
                    continue
                num = 0
                for k in range(-1,2):
                    for l in range(-1,2):
                        if(i + k >= 0 and i + k  < self.length and j + l >= 0 and j + l < self.width):
                            if(self.grid[i+k][j + l].is_bomb()):
                                num += 1
                self.grid[i][j].set_num_surrounding(num)
        for i in range(self.length):
            for j in range (self.width):
                print(self.grid[i][j].num_surrounding, end = " ")
            print()

    def click(self,x,y):
        if(x < 0 or x >= self.length or y < 0 or y >= self.width or self.grid[x][y].is_clicked or self.grid[x][y].flagged):
            return
        elif(self.grid[x][y].num_surrounding == -1):
            return -1
        elif(self.grid[x][y].num_surrounding > 0):
            self.grid[x][y].open()
            self.num_opened += 1
        else:
            self.grid[x][y].open()
            self.num_opened += 1
            self.click(x + 1, y)
            self.click(x, y + 1)
            self.click(x - 1, y)
            self.click(x, y - 1)
            self.click(x + 1, y + 1)
            self.click(x - 1, y + 1)
            self.click(x + 1, y - 1)
            self.click(x - 1, y - 1)
            return 0
    
    def is_won(self):
        if self.num_opened >= self.length * self.width - self.bombs:
            return True
        return False
    
    def flag(self,i,j):
        self.grid[i][j].flag()
    
    def getCell(self,i,j):
        return self.grid[i][j]
