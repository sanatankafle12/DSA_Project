import pygame


class Gamestate():
    def __init__(self,DIMENSION):
        
        self.board = []
        for r in range(DIMENSION):
            col = []
            for c in range(DIMENSION):
                col.append('--')
            self.board.append(col)


class Button():
 
    def __init__(self,x,y,image,screen):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.screen = screen


    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
        