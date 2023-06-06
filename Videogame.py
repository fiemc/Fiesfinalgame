import pygame, sys
from settings import *
from level import Level
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

font = pygame.font.Font("freesansbold.ttf", 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    level.run()
    if(len(level.player) > 0):
        text = font.render(str(level.player.sprite.score), True, (0,250,100))
    screen.blit(text,(0,0))
    pygame.display.update()
    clock.tick(fps)





