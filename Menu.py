import pygame
import sys
from game import *
from solve import *

pygame.init()
screen = pygame.display.set_mode((400,400))
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

def Menu():    
    pygame.display.set_caption("                                 Choose Your Destiny !!!")
    image = pygame.image.load("images/bg.png")
    play = pygame.image.load('images/PLAY.png').convert_alpha()
    solve = pygame.image.load('images/SOLVE.png').convert_alpha()
    button_play = Button(150, 300, play)
    button_solve = Button(150, 350, solve) 
    pygame.mixer.init()
    crash_sound = pygame.mixer.Sound("sounds/background.wav")
    crash_sound.set_volume(0.2)
    crash_sound.play()
    while True:
        screen.blit(image, (0,0))
        if button_play.draw():
            pygame.quit()
            pygame.mixer.init()
            button = pygame.mixer.Sound("sounds/click.wav")
            button.play()
            main()

        if button_solve.draw():
            Solve()
            pygame.quit()


        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()    

            pygame.display.update()
