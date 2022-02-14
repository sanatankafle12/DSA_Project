import pygame
import sys
from game import *
from solve import *
from minimum_moves import *
from gamestate import *
from settings import *

pygame.init()
screen = pygame.display.set_mode((400,400))

def Menu():    
    pygame.display.set_caption("                                 Choose Your Destiny !!!")
    image = pygame.image.load("images/bg.png")
    play = pygame.image.load('images/PLAY.png').convert_alpha()
    solve = pygame.image.load('images/SOLVE.png').convert_alpha()
    ms = pygame.image.load('images/ms.png').convert_alpha()
    setting = pygame.image.load('images/ms.png').convert_alpha()
    button_play = Button(10, 350, play,screen)
    button_solve = Button(150, 350, solve,screen) 
    button_solve2 = Button(280, 350, ms,screen) 
    button_setting = Button(150,300,setting,screen)
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
            pygame.quit()
            Solve()
        
        if button_solve2.draw():
            pygame.quit()
            main2()

        if button_setting.draw():
            pygame.quit()
            help_setting()

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()    

            pygame.display.update()
