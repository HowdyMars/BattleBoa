# This file will serve as the item class for the game
import pygame as pg
import constants as c

class Item(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pg.Rect(200, 200, 100, 60)
        
    def draw(self, screen):
        pg.draw.rect(screen, c.PLAYER_RECT_GREEN, self.rect)