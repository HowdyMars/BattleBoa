# This file will serve as the item class for the game
import pygame as pg
import constants as c
import random

class Item(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pg.Rect(200, 200, 30, 30)

    def draw(self, screen):
        pg.draw.rect(screen, c.PLAYER_RECT_RED, self.rect)
        
    def check_collision(self, player_rect):
        if self.rect.colliderect(player_rect):
            return True
        return False
    
    def set_random_position(self):
        random_x = random.randint(0, 1000 - self.rect.width)
        random_y = random.randint(0, 1000 - self.rect.height)
        self.rect.topleft = (random_x, random_y) 
        
    @classmethod
    def create_item(cls, count=3):
        return [cls() for _ in range(count)]