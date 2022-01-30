import pygame


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
BG_COLOR = pygame.Color('gray12')

done = False
while not done:
    # This event loop empties the event queue each frame.
    for event in pygame.event.get():
        # Quit by pressing the X button of the window.
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # MOUSEBUTTONDOWN events have a pos and a button attribute
            # which you can use as well. This will be printed once per
            # event / mouse click.
            print('In the event loop:', event.pos, event.button)

    # Instead of the event loop above you could also call pygame.event.pump
    # each frame to prevent the window from freezing. Comment it out to check it.
    # pygame.event.pump()

    click = pygame.mouse.get_pressed()
    mousex, mousey = pygame.mouse.get_pos()
    print(click, mousex, mousey)

    screen.fill(BG_COLOR)
    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS.
