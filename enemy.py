import pygame, random



class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("asteroid.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 3

    def update(self):
        self.rect.x -= 1
        self.rect.y -= 0
        if self.rect.x < 0:
            self.kill()





