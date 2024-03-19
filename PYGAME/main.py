import pygame

#inicial config
pygame.init()

#create a player screen

screen =pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("My game")
BG_COLOR = (246, 234, 180)
WIDTH = 400
HEIGHT = 400
#main loop
status = True
while status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
    screen.fill(BG_COLOR)
    pygame.display.flip()
pygame.quit()
