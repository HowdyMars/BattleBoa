# This file will serve as the character class for the game
import pygame as pg
import constants as c

class Character(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()  # This is another way to call the parent class's __init__ method
        self.rect = pg.Rect(200, 200, 100, 60)        
        self.original_dimensions = (100, 60) # width, height to test
        
    def flip_rect(self, dx, dy): # for testing
        if dx != 0:  # Moving horizontally
            self.rect.width, self.rect.height = self.original_dimensions
        elif dy != 0:  # Moving vertically
            self.rect.height, self.rect.width = self.original_dimensions
        
    def update_direction(self, new_direction):
        # Ensure the snake can't reverse onto itself
        opposite_directions = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if new_direction != opposite_directions[self.direction]:
            self.direction = new_direction
    
    # define draw method
    def draw(self, screen):
        pg.draw.rect(screen, c.PLAYER_RECT_RED, self.rect)
        
    def move(self, dx, dy):
        self.flip_rect(dx, dy)
        self.rect.move_ip(dx, dy)
