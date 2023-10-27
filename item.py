# This file will serve as the item class for the game
import pygame as pg
import constants as c
import random

class Item(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.food_images_path = c.SPRITES["food"]
        self.food_images = pg.image.load(self.food_images_path).convert_alpha()
        self.sprite = self.random_sprite()
        self.rect = pg.Rect(200, 200, 60, 60)
        self.item_collected = False
        self.text_float = False
        self.text_float_frames = 0

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)
        
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
            
            self.sprite = self.random_sprite()
            
            self.set_random_position()
            
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
        
    def get_item_sprite(self, frame, width, height, scale, color):
        image = pg.Surface(([width, height]), pg.SRCALPHA).convert_alpha()
        image.blit(self.food_images, (0, 0), ((frame * width), 0, width, height))
        image = pg.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        
        return image
    
    def random_sprite(self):
        item_sprite_list = []
        for frame in range(7):
            item_sprite_list.append(self.get_item_sprite(frame, 16, 16, 4, c.BLACK))
            
        return random.choice(item_sprite_list)
        
    @classmethod
    def create_item(cls, count=3):
        return [cls() for _ in range(count)]
    