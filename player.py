import pygame
from bullet import Bullet
from enemy import random

class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("x rotate.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8

        # Shooting
        self.bullets = pygame.sprite.Group()  # Changed from "bullet" to "bullets"
        self.firing = False

        self.score = 0

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.y = -1
        elif keys[pygame.K_LEFT]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_SPACE] and not self.firing:
            self.fire()
            self.firing = True
        elif not keys[pygame.K_SPACE] and self.firing:
            self.firing = False

    def fire(self):
        # Fixed incomplete line
        bullet = Bullet(((self.rect.centerx, self.rect.centery)), self.direction.x)
        self.bullets.add(bullet)

    def update(self, enemies):
        self.get_input()
        # this is the code for when a bullet hits a enemy and the score goes up
        self.rect.y += self.direction.y * self.speed
        killed = pygame.sprite.groupcollide(self.bullets, enemies, True, True)
        if(len(killed) > 0):
            self.score += 1
        self.bullets.update()


