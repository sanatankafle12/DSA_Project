import gamestate
import sys
import pygame as p
from DsImplementation import *
import random

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15

s = Stack()

def main():
    move = -1
    p.init()
    screen = p.display.set_mode((WIDTH+150,HEIGHT))
    clock = p.time.Clock()
    gs = gamestate.Gamestate(DIMENSION)
    image = p.transform.scale(p.image.load('images\knights.jpg'),(SQ_SIZE,SQ_SIZE))
    img1 = p.image.load('images\game1.png')
    running = True
    location = ()
    drawBoard(screen, gs.board)
    while running:  
        screen.blit(img1,(WIDTH-2,0))
        font = p.font.Font('fsb.ttf', 30)
        score = "MOVE: " + str(move+1)
        text = font.render(score, True,'green') 
        screen.blit(text,(WIDTH+15,HEIGHT-75)) 
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if p.mouse.get_pressed()[0] == 1:
                    location = p.mouse.get_pos()
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    location = (col,row)
                    if check_if_empty(gs.board) == True :
                        Won_screen()
                    else:
                        if(move == -1):
                            if (check_valid(screen, gs.board, location)): 
                                p.mixer.init()
                                button = p.mixer.Sound("sounds/move.wav")
                                button.play()
                                move = move + 1
                                drawBoard(screen, gs.board)
                                drawPieces(screen, gs.board, image,location,move)   
                                green_square(screen, gs.board, location) 
                                s.push(location)

                        else:
                            prev_location = s.items[move]
                            if(square(screen, gs.board,location,prev_location) and check_valid(screen, gs.board, location)):
                                p.mixer.init()
                                button = p.mixer.Sound("sounds/move.wav")
                                button.play()
                                move = move + 1
                                drawBoard(screen, gs.board)
                                drawPieces(screen, gs.board, image,location,move)   
                                green_square(screen, gs.board, location)
                                s.push(location)
                                if(loss(screen, gs.board, location)):
                                    p.quit()
                                    lost_screen(move)
                                    running = False
                            else:
                                button = p.mixer.Sound("sounds/click.wav")
                                button.play()
                                
        clock.tick(MAX_FPS)
        p.display.flip()


def drawBoard(screen,board):
    colors = [p.Color('white'),p.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            if(board[r][c] == '--'):
                color = colors[((r+c)%2)]
                p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
            if(board[r][c]=='++'):
                color = 'red'
                p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))


def drawPieces(screen,board,image,location,move):
    screen.blit(image, p.Rect(location[0]*SQ_SIZE,location[1]*SQ_SIZE,SQ_SIZE,SQ_SIZE))
    board[location[1]][location[0]] = '++'


def check_valid(screen,board,location):
    if(location[0] < 0 or location[0] > (DIMENSION-1) or location[1] < 0 or location[1] > (DIMENSION-1)):
        return
    if(board[location[1]][location[0]] == "--"):
        return True
    return False


def green_square(screen, board, location):
    valid_square = []
    row = location[1]
    col = location[0]
    valid_square.append((col+2,row+1))
    valid_square.append((col+1,row+2))
    valid_square.append((col-2,row+1))
    valid_square.append((col-1,row+2))
    valid_square.append((col+2,row-1))
    valid_square.append((col+1,row-2))
    valid_square.append((col-2,row-1))
    valid_square.append((col-1,row-2))
    for j in range(len(valid_square)):
        for i in valid_square:
            if (i[1]<0 or i[0]<0 or i[0]>(DIMENSION-1) or i[1]>(DIMENSION-1) or board[i[1]][i[0]]=='++'):
                valid_square.remove(i)
            else:
                if(board[i[1]][i[0]]=='--'):
                    p.draw.rect(screen,'LightGreen',p.Rect(i[0]*SQ_SIZE,i[1]*SQ_SIZE,SQ_SIZE,SQ_SIZE))
    return valid_square


def check_if_empty(board):
    count = 0
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            if(board[i][j]=='--'):
                count = count + 1
    if(count == 1 ):
        return True
    return False


def square(screen,board,location,prev_location):
    valid_square = green_square(screen, board, prev_location)
    for i in valid_square:
        if location == i:
            return True
    return False


def loss(screen,board,location):
    valid_square = green_square(screen, board, location)
    if(valid_square == []):
        return True
    return False


def lost_screen(move):
    p.init()
    screen = p.display.set_mode((250,150))
    exit1 = p.image.load('images\exit2.png')
    exit_button = gamestate.Button(30,50,exit1,screen)
    running = True
    while running:
        font = p.font.Font('fsb.ttf',20)
        score_text = "YOU SCORED: " 
        score = str(move+1)
        text = font.render(score, True,'green') 
        text2 = font.render(score_text, True,'green') 
        screen.blit(text,(50,20)) 
        screen.blit(text2,(20,0)) 
        if exit_button.draw():
            p.quit() 
        for j in p.event.get():
            if j.type == p.QUIT:
                sys.exit(1)
                p.quit()
            p.display.update()


def Won_screen():
    p.init()
    screen = p.display.set_mode((250,150))
    exit1 = p.image.load('images\exit2.png')
    exit_button = gamestate.Button(100, 100, exit1, screen)
    screen.fill("black")
    while True:
        font = p.font.Font('fsb.ttf', 20)
        t = "           CONGRATS!!"
        t1 = "      SOLUTION FOUND :)"
        text = font.render(t, True,'Green')
        text1 = font.render(t1, True, 'Green')
        screen.blit(text,(0,50)) 
        screen.blit(text1, (0,75))
        if exit_button.draw():
            p.quit()
        for j in p.event.get():
            if j.type == p.QUIT:
                p.quit()
            p.display.update()