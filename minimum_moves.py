import gamestate
import sys
import pygame as p
from DsImplementation import *
import random
from minimum_moves_solution import *
from Menu import *


WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15


s = Stack()


def main2():
    move = -1
    p.init()
    screen = p.display.set_mode((WIDTH+150,HEIGHT))
    solve = p.image.load('images/SOLVE.png').convert_alpha()
    redo = gamestate.Button(WIDTH,HEIGHT//2,solve,screen)
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    gs = gamestate.Gamestate(DIMENSION)
    image = p.transform.scale(p.image.load('images\knights.jpg'),(SQ_SIZE,SQ_SIZE))
    running = True
    drawBoard(screen, gs.board)
    locations = get_positions()
    start = locations[0]
    end = locations[1]
    gs.board[start[1]][start[0]] = 'ee'
    gs.board[end[1]][end[0]] = 'ee'
    p.draw.rect(screen,'pink',p.Rect(start[0]*SQ_SIZE,start[1]*SQ_SIZE,SQ_SIZE,SQ_SIZE))
    p.draw.rect(screen,'orange',p.Rect(end[0]*SQ_SIZE,end[1]*SQ_SIZE,SQ_SIZE,SQ_SIZE))
    img3 = p.image.load('images\game3.png')
    src = Node(start[0],start[1])
    dest = Node(end[0], end[1])
    x = findShortestDistance(src, dest, DIMENSION)
    if(x<=2):
        level = "Easy"
    elif(x<=4):
        level = "Medium"
    else:
        level = "Difficult"
    while running:  

        screen.blit(img3,(WIDTH-2,0))
        font = p.font.Font('fsb.ttf', 20)
        score = "Level: "+level
        text = font.render(score, True,'green') 
        screen.blit(text,(WIDTH+10,HEIGHT-75)) 
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
                        return False

                    else:
                        if(move == -1):

                            if(location == start):
                                if (check_valid(screen, gs.board, location,move)): 
                                    move = move + 1
                                    drawBoard(screen, gs.board)
                                    drawPieces(screen, gs.board, image,location,move)   
                                    green_square(screen, gs.board, location) 
                                    s.push(location)
                        else:
                            prev_location = s.items[move]
                            if(square(screen, gs.board,location,prev_location) and check_valid(screen, gs.board, location,move)):
                                move = move + 1
                                drawBoard(screen, gs.board)
                                drawPieces(screen, gs.board, image,location,move) 
                                if(location == end):
                                    if(check_optimal(start,end,move)):
                                        p.quit()
                                        Won_screen() 
                                    else:
                                        p.quit()
                                        lost_screen(start,end,move)               
                                green_square(screen, gs.board, location)
                                s.push(location)

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
    if(move == 0):
        return
    board[location[1]][location[0]] = '++'


def check_valid(screen,board,location,move):
    if(location[0] < 0 or location[0] > (DIMENSION-1) or location[1] < 0 or location[1] > (DIMENSION-1)):
        return
    if(board[location[1]][location[0]] == "--" or move == -1 or board[location[1]][location[0]] == "ee"):
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


def get_positions():
    array = [x for x in range(DIMENSION)]
    start_col = random.choice(array)
    start_row = random.choice(array)
    destination_col = random.choice(array)
    destination_row = random.choice(array)
    if(destination_col == start_col and destination_row == start_row):
        destination_col = random.choice(array)
        destination_row = random.choice(array)
    start = (start_col,start_row)
    destination = (destination_col,destination_row)
    return start,destination


def check_optimal(start,end,move):
    src = Node(start[0],start[1])
    dest = Node(end[0], end[1])
    return findShortestDistance(src, dest, DIMENSION) == move


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


def lost_screen(start,end,move):
    src = Node(start[0],start[1])
    dest = Node(end[0], end[1])
    x = findShortestDistance(src, dest, DIMENSION)
    p.init()
    screen = p.display.set_mode((250,150))
    exit1 = p.image.load('images\exit2.png')
    exit_button = gamestate.Button(100, 100, exit1, screen)
    screen.fill("black")
    while True:
        font = p.font.Font('fsb.ttf', 20)
        t = "       OOPS!!"
        t1 = "      optimal Move:" + str(x)
        t2 = "      You took:" +str(move)
        text = font.render(t, True,'Green')
        text1 = font.render(t1, True, 'Green')
        text2 = font.render(t2, True, 'Green')
        screen.blit(text,(0,25)) 
        screen.blit(text1, (0,50))
        screen.blit(text2, (0,75))
        if exit_button.draw():
            p.quit()
        for j in p.event.get():
            if j.type == p.QUIT:
                p.quit()
            p.display.update()
    