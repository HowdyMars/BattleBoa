# This file will serve as the character class for the game
import pygame as pg
import constants as c
from collections import deque

class Character(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()  # This is another way to call the parent class's __init__ method
        self.rect = pg.Rect(60, 60, 40, 40)
        self.segments = [self.rect] # This will be a list of all the segments of the snake
        self.original_dimensions = (40, 40) # width, height to test
        self.buffer_length = 10 # This is the buffer between segments
        self.positions = deque(maxlen=1000)
        
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
        for segment in self.segments:
            pg.draw.rect(screen, c.PLAYER_RECT_RED, segment, 1)
        
    def move(self, dx, dy):
        previous_position = self.segments[0].topleft
        # move head
        self.flip_rect(dx, dy)
        self.rect.move_ip(dx, dy)
        # Store the new head position in the positions deque
        self.positions.appendleft(self.segments[0].topleft)
        # Move each segment to its new position based on the positions in the deque
        for i, segment in enumerate(self.segments[1:], start=1):
            segment.topleft = self.positions[i * self.buffer_length]
            
        
    def grow(self, dx, dy):
        tail = self.segments[-1].copy() # get the last segment
        # Adjust tail's position based on movement direction
        if dx > 0:  # Moving right
            tail.move_ip(-tail.width, 0)
        elif dx < 0:  # Moving left
            tail.move_ip(tail.width, 0)
        elif dy > 0:  # Moving down
            tail.move_ip(0, -tail.height)
        elif dy < 0:  # Moving up
            tail.move_ip(0, tail.height)
            
        self.segments.append(tail)
