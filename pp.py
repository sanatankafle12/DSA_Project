import DsImplementation
from game import *
import gamestate
import time

n = 6

s1 = DsImplementation.Stack()
q1 = DsImplementation.Queue()
WIDTH = HEIGHT = 512
DIMENSION = 6
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15

def Solve():
    p.init()    
    start = 0
    end = 0
    screen = p.display.set_mode((WIDTH+150,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    gs = gamestate.Gamestate(n)
    image = p.transform.scale(p.image.load('images\knights.jpg'),(SQ_SIZE,SQ_SIZE))
    mark = p.transform.scale(p.image.load('images\mark.png'),(SQ_SIZE,SQ_SIZE))
    img1 = p.image.load('images\game2.png')
    exit1 = p.image.load('images\exit.png')
    exit_button = gamestate.Button(WIDTH+10,HEIGHT-50,exit1,screen)
    running = True
    location = ()
    drawBoard(screen, gs.board)
    while running: 
        screen.blit(img1,(WIDTH-2,0))     
        font = p.font.Font('fsb.ttf', 20)
        score = "TIME: " + str(round(end-start,2))
        text = font.render(score, True,'green') 
        screen.blit(text,(WIDTH+10,HEIGHT-75))  
        if exit_button.draw():
            p.quit() 
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
                p.quit()
            elif e.type == p.MOUSEBUTTONDOWN:
                if p.mouse.get_pressed()[0] == 1:
                    location = p.mouse.get_pos()
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    if(row>=0 and col>=0 and row<n and col<n):
                        location = (col,row)
                        screen.blit(mark, p.Rect(location[0]*(SQ_SIZE),location[1]*(SQ_SIZE),(SQ_SIZE),(SQ_SIZE)))
                        start = time.time()
                        end = solveKT(location,screen,gs.board,image) 
                    
        clock.tick(MAX_FPS)
        p.display.flip()


def isSafe(x,y,board):   
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1): 
        return True
    return False

def solveKT(location,screen,board,image): 
    board = [[-1 for i in range(n)]for i in range(n)] 
    move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
    move_y = [1, 2, 2, 1, -1, -2, -2, -1] 
    
    board[location[1]][location[0]] = 0
  
    pos = 1
   
    if(not solveKTUtil(board, location[1], location[0], move_x, move_y, pos)):
        return False
    else:
        end = time.time()
        for i in range(len(q1.items)):
            j = q1.dequeue()
            font = p.font.Font('fsb.ttf', 50)
            text = font.render(str(i+1), True,'green')
            Solution(screen, board, j,text)
            p.mixer.init()
            button = p.mixer.Sound("sounds/move.wav")
            button.set_volume(0.2)
            button.play()
            time.sleep(0.05)
            p.display.update()
        return(end)
            
def Solution(screen,board,j,text):
    screen.blit(text, p.Rect(j[1]*(SQ_SIZE),j[0]*(SQ_SIZE),(SQ_SIZE),(SQ_SIZE)))

def solveKTUtil(board,curr_x,curr_y,move_x,move_y,pos):   
    if(pos == n**2): 
        return True    
    for i in range(8): 
        new_x = curr_x + move_x[i] 
        new_y = curr_y + move_y[i] 
        if(isSafe(new_x,new_y,board)): 
            board[new_x][new_y] = pos 
            if(solveKTUtil(board,new_x,new_y,move_x,move_y,pos+1)): 
                q1.enqueue((new_x,new_y))
                return True
            board[new_x][new_y] = -1
    return False

