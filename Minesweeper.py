import random as random
from tkinter import *
WIDTH = 10
HEIGHT = 10
numMines = 37
msBoard = [[0 for j in range(WIDTH)] for i in range(HEIGHT)]
shownBoard = [[" " for j in range(WIDTH)] for i in range(HEIGHT)]
listOfLabels = [["" for j in range(WIDTH)] for i in range(HEIGHT)]
listOfMines = []


def createBoard():

    nM = numMines
    while nM != 0:
        col = random.randint(0,WIDTH-1)
        row = random.randint(0,HEIGHT-1)
        if msBoard[row][col] != "X" :
            listOfMines.append((row,col))
            for i in range(row-1,row+2):
                for j in range(col-1,col+2):
                    if i >= 0 and i < HEIGHT:
                        if j >=0 and j <WIDTH:
                            if msBoard[i][j] != "X":
                                msBoard[i][j] += 1
            msBoard[row][col] = "X"
            nM -= 1
def show():
    for i in range(HEIGHT):
        print("|",end = "")
        for j in range(WIDTH):
            print(shownBoard[i][j], end = "|")
        print("")


def floodfill(row,col):
    if(row >= 0 and row < HEIGHT and col >= 0 and col < WIDTH and shownBoard == " "):
        shownBoard[row][col] = msBoard[row][col]
        label = Label(window,bg='White',text = shownBoard[row][col],fg='Black',command=open(row,col)).grid(row=row,column=col)
        if(msBoard[row][col] == 0):
            floodfill(row+1,col)
            floodfill(row,col+1)
            floodfill(row-1,col)
            floodfill(row,col-1)

def open(row,col):
    print(str(row) + " " + str(col))
    if msBoard[row][col] == "X":
        print("Game over")
        exit()
    else:
        if msBoard[row][col] == 0:
            floodfill(row,col)
        else:
            shownBoard[row][col] = msBoard[row][col]
            label = Label(window, bg='White', text=shownBoard[row][col], fg='Black', command=open(row, col)).grid(row=row,
                                                                                                          column=col)
def isWon():
    for i in listOfMines:
        if(shownBoard[i[0]][i[1]] != "X"):
            return False
    return True

#createBoard()
#while not isWon():
#    show()
#    if input("Place bomb? [y/n]") == "n":
#        open(int(input("Enter the row: ")),int(input("Enter the col: ")))
#    else:
#        shownBoard[int(input("Enter row: "))][int(input("Enter col: "))] = "X"
#if isWon():
#    print("Congrats")

window = Tk()
window.config(background="Grey")
window.geometry("500x500")
grid = Grid()
label = Label(window,text="Hi")
label.pack()
label.bind("<Button-1>", open(0,0))
'''for i in range(HEIGHT):
    for j in range(WIDTH):
        listOfLabels[i][j] = Label(window,bg='White',text = "0",fg='Black',relief=RAISED).grid(row=i,column=j)
        listOfLabels[i][j].bind("<Button-1>", open(i,j))
        '''
window.mainloop()
















