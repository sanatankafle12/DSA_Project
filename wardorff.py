import DsImplementation
from game import *
import gamestate
import time

n = 8

s1 = DsImplementation.Stack()
q1 = DsImplementation.Queue()
WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
board = []
for i in range(n):
    board.append([0]*n)

def Solve():
    p.init()
    num =1  
    start = 0
    end = 0
    screen = p.display.set_mode((WIDTH+150,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    gs = gamestate.Gamestate(n)
    image = p.transform.scale(p.image.load('images\knights.jpg'),(SQ_SIZE,SQ_SIZE))
    mark = p.transform.scale(p.image.load('images\mark.png'),(SQ_SIZE,SQ_SIZE))
    img1 = p.image.load('images\game2.png')
    running = True
    location = ()
    drawBoard(screen, gs.board)
    while running: 
        screen.blit(img1,(WIDTH-2,0))     
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if p.mouse.get_pressed()[0] == 1:
                    location = p.mouse.get_pos()
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    if(row>=0 and col>=0 and row<n and col<n):
                        location = (col,row)
                        screen.blit(mark, p.Rect(location[0]*(SQ_SIZE),location[1]*(SQ_SIZE),(SQ_SIZE),(SQ_SIZE)))
                        start = time.time()
                        tour(num, [], location, screen,start)
        clock.tick(MAX_FPS)
        p.display.flip()


def generate_legal_moves(cur_pos):
    possible_pos = []
    move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                    (2, 1), (2, -1), (-2, 1), (-2, -1)]

    for move in move_offsets:
        new_x = cur_pos[0] + move[0]
        new_y = cur_pos[1] + move[1]

        if (new_x >= n or new_x < 0 or new_y < 0 or new_y >= n):
            continue
        else:
            possible_pos.append((new_x, new_y))
    return possible_pos


def sort_lonely_neighbors(board,to_visit):
    neighbor_list = generate_legal_moves(to_visit)
    empty_neighbours = []
    for neighbor in neighbor_list:
        np_value = board[neighbor[0]][neighbor[1]]
        if np_value == 0:
            empty_neighbours.append(neighbor)

    scores = []
    for empty in empty_neighbours:
        score = [empty, 0]
        moves = generate_legal_moves(empty)
        for m in moves:
            if board[m[0]][m[1]] == 0:
                score[1] += 1
        scores.append(score)

    scores_sort = sorted(scores, key = lambda s: s[1])
    sorted_neighbours = [s[0] for s in scores_sort]
    return sorted_neighbours

def tour(n, path, to_visit,screen,start):
        exit1 = p.image.load('images\exit.png')
        exit_button = gamestate.Button(WIDTH+10,HEIGHT-50,exit1,screen)
        print(n)
        board[to_visit[0]][to_visit[1]] = n
        path.append(to_visit)
        q1.enqueue(to_visit) 
        if n == 8 * 8:
            end = time.time()
            draw_board(screen,end,start)
            while True:
                if exit_button.draw():
                    sys.exit(1)
                    p.quit()
                for e in p.event.get():
                    if e.type == p.QUIT:
                        sys.exit(1)
                        p.quit()
                p.display.update()
        else:
            sorted_neighbours = sort_lonely_neighbors(board,to_visit)
            for neighbor in sorted_neighbours:
                tour(n+1, path, neighbor,screen,start)
            board[to_visit[0]][to_visit[1]] = 0
            try:
                x = path.pop()
                q1.items.remove(x)
            except IndexError or ValueError:
                sys.exit(1)

def draw_board(screen,end,start):
    exit1 = p.image.load('images\exit.png')
    exit_button = gamestate.Button(WIDTH+20, HEIGHT-50, exit1, screen)
    for i in range(len(q1.items)):
        if(i==0):
            j = q1.dequeue()
            continue
        j = q1.dequeue()
        font = p.font.Font('fsb.ttf', 30)
        text = font.render(str(i), True,'green')
        Solution(screen, j,text)
        p.mixer.init()
        button = p.mixer.Sound("sounds/move.wav")
        button.set_volume(0.2)
        button.play()
        time.sleep(0.05)
        p.display.update()
    font = p.font.Font('fsb.ttf', 20)
    score = "TIME: " + str(round(end-start,2))
    text = font.render(score, True,'green') 
    screen.blit(text,(WIDTH+10,HEIGHT-75))  


def Solution(screen,j,text):
    screen.blit(text, p.Rect(j[0]*(SQ_SIZE),j[1]*(SQ_SIZE),(SQ_SIZE),(SQ_SIZE)))

