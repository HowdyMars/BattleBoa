# This file will serve as the item class for the game
import pygame as pg
import constants as c
import random

class Item(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pg.Rect(200, 200, 30, 30)
        self.item_collected = False
        self.text_float = False
        self.text_float_frames = 0

    def draw(self, screen):
        pg.draw.rect(screen, c.RED, self.rect)
        
    def check_collision(self, player_rect):
        if self.rect.colliderect(player_rect):
            self.item_collected = True
            return True
        return False
    
    def handle_collected(self, player_rect):
        if self.item_collected:
            self.text_float = True
            self.item_collected = False
            self.text_start_y = player_rect.centery - player_rect.height // 2
            
        if self.text_float:
            self.text_start_y -= 5
            self.text_float_frames += 1
            
        if self.text_float_frames >= 20:
            self.text_float = False
            self.text_float_frames = 0
    
    def set_random_position(self):
        random_x = random.randint(0, 1000 - self.rect.width)
        random_y = random.randint(0, 1000 - self.rect.height)
        self.rect.topleft = (random_x, random_y)
        
    @classmethod
    def create_item(cls, count=3):
        return [cls() for _ in range(count)]
    