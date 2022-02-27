import pygame
import sys
from game import *
from solve import *
from minimum_moves import *
from gamestate import *


def menu(): 
    
    pygame.init()
    screen = pygame.display.set_mode((400,400))   
    pygame.display.set_caption("                                 Choose Your Destiny !!!")
    image = pygame.image.load("images/bg.png")
    play = pygame.image.load('images/PLAY.png').convert_alpha()
    img1 = pygame.image.load('images/image1.png').convert_alpha()
    img2 = pygame.image.load('images/image2.png').convert_alpha()
    img3 = pygame.image.load('images/image3.png').convert_alpha()
    solve = pygame.image.load('images/SOLVE.png').convert_alpha()
    ms = pygame.image.load('images/ms.png').convert_alpha()
    button_play = Button(10, 350, play,screen)
    button_solve = Button(150, 350, solve,screen) 
    button_solve2 = Button(280, 350, ms,screen)
    color1 = Button(10, 260, img1,screen)
    color2 = Button(150, 260, img2,screen)
    color3 = Button(280, 260, img3,screen) 
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


        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()    

            pygame.display.update()

