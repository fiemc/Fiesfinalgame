import pygame, random
from settings import tile_size, screen_width, screen_height
from tile import Tile
from player import Player
from enemy import Enemy


class Level:
    def __init__(self, level_data, surface):

        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.setup_level(level_data)


    def setup_level(self, layout):

        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size
                if cell == "x":
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                elif cell == "p":
                    player_sprite = Player ((x,y))
                    self.player.add(player_sprite)

        for i in range(20):
            enemy = Enemy((random.randint(400, screen_width), random.randint(0, screen_height)))
            self.enemies.add(enemy)

    def run(self):

        self.tiles.draw(self.display_surface)

        self.enemies.update()
        self.enemies.draw(self.display_surface)




        # Dettect collisions between player and enemy
        collided_with = pygame.sprite.groupcollide(self.player, self.enemies, True, False)
        if len(collided_with)> 0:
            print(collided_with)
            print("GAMEOVER")
        if len(self.player) > 0:
            self.player.update(self.enemies)
            self.player.draw(self.display_surface)
            print(self.player.sprite.bullets)
            self.player.sprite.bullets.draw(self.display_surface)

        while(len(self.enemies) < 20):
            enemy = Enemy((screen_width + 60, random.randint(0, screen_height)))
            self.enemies.add(enemy)
