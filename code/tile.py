import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)

        self.sprite_type = sprite_type
        self.image = surface
        self.inflation_factor = 0
        if sprite_type == "object":
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1]-TILESIZE))
            self.inflation_factor = -10
        else:
            self.rect = self.image.get_rect(topleft=pos)
            self.inflation_factor = -10

        self.hitbox = self.rect.inflate(0, self.inflation_factor)