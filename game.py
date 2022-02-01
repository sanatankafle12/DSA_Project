import gamestate
import pygame as p

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15


def main():
    move = 1
    p.init()
    screen = p.display.set_mode((WIDTH+150,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    gs = gamestate.Gamestate()
    image = p.transform.scale(p.image.load('images\knights.jpg'),(SQ_SIZE,SQ_SIZE))
    running = True
    sqSelected = ()
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
                    if(check_valid(screen, gs.board, location)):
                        drawBoard(screen, gs.board)
                        drawPieces(screen, gs.board, image,location,move)   
                        green_square(screen, gs.board, location)      
        clock.tick(MAX_FPS)
        p.display.flip()
'''
def drawGameState(screen,gs,image):
    drawBoard(screen,gs.board)
    drawPieces(screen,gs.board,image)
'''

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
    '''if(move==1):
        screen.blit(image, p.Rect(location[0]*SQ_SIZE,location[1]*SQ_SIZE,SQ_SIZE,SQ_SIZE))
        board[location[1]][location[0]] == 'hh'
        return'''
    
    screen.blit(image, p.Rect(location[0]*SQ_SIZE,location[1]*SQ_SIZE,SQ_SIZE,SQ_SIZE))
    board[location[1]][location[0]] = '++'

def check_valid(screen,board,location):
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
            if (i[1]<0 or i[0]<0 or i[0]>7 or i[1]>7):
                valid_square.remove(i)
            else:
                if(board[i[1]][i[0]]=='--'):
                    p.draw.rect(screen,'LightGreen',p.Rect(i[0]*SQ_SIZE,i[1]*SQ_SIZE,SQ_SIZE,SQ_SIZE))

    if location in valid_square:
        return True
    False



