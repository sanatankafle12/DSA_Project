import DsImplementation
from game import *
import gamestate
import time

n = 6

s1 = DsImplementation.Stack()
q1 = DsImplementation.Queue()

def Solve():
    p.init()
    screen = p.display.set_mode((WIDTH+150,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    gs = gamestate.Gamestate(n)
    image = p.transform.scale(p.image.load('images\knights.jpg'),(SQ_SIZE,SQ_SIZE))
    mark = p.transform.scale(p.image.load('images\mark.png'),(SQ_SIZE,SQ_SIZE))
    running = True
    location = ()
    drawBoard(screen, gs.board)
    while running:        
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if p.mouse.get_pressed()[0] == 1:
                    location = p.mouse.get_pos()
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    location = (col,row)
                    screen.blit(mark, p.Rect(location[0]*(SQ_SIZE),location[1]*(SQ_SIZE),(SQ_SIZE),(SQ_SIZE)))
                    solveKT(location,screen,gs.board,image)
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
        print("Solution does not exist") 
    else:
        for i in range(len(q1.items)):
            j = q1.dequeue()
            font = p.font.Font('fsb.ttf', 50)
            text = font.render(str(i+1), True,'green')
            Solution(screen, board, j,text)
            time.sleep(0.05)
            p.display.update()
            
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

