# This file will serve as the character class for the game
import pygame as pg
import constants as c
from collections import deque
from icecream import ic
import random

class Character(pg.sprite.Sprite):
    def __init__(self, start_x=500, start_y=500, player=False):
        super().__init__()  # This is another way to call the parent class's __init__ method
        self.player = player
        self.original_dimensions = (30, 30) # width, height to test
        start_x = start_x - self.original_dimensions[0] // 2
        start_y = start_y - self.original_dimensions[1] // 2
        self.rect = pg.Rect(start_x, start_y, 30, 30)
        self.segments = [self.rect] # This will be a list of all the segments of the snake
        self.buffer_length = 6 # This is the buffer between segments
        self.positions = deque(maxlen=1000)
        self.last_dx = 0
        self.last_dy = c.DEFAULT_SPEED
        self.target_item = None
        self.frames_since_last_item = 0
        
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
    def draw(self, screen, color=c.GREEN):
        # head = self.segments[0]
        # pg.draw.rect(screen, c.PLAYER_RECT_RED, head)
        for segment in self.segments:
            pg.draw.rect(screen, color, segment)
            
    def follow_mouse(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        # Calculate the difference between the mouse and the player position
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery
        # Normalize the movement if it's greater than the character's speed
        magnitude = (dx ** 2 + dy ** 2) ** 0.5
        if magnitude > 0:
            dx, dy = (dx / magnitude) * c.DEFAULT_SPEED, (dy / magnitude) * c.DEFAULT_SPEED
            self.last_dx, self.last_dy = dx, dy
        else:
            dx, dy = self.last_dx, self.last_dy
        return dx, dy
        
    def move(self, dx, dy):
        # Move head
        self.flip_rect(dx, dy)
        self.rect.move_ip(dx, dy)
        # Always store the new head position in the positions deque
        self.positions.appendleft(self.segments[0].topleft)
        # Move each segment to its new position based on the positions in the deque and the buffer length
        for i, segment in enumerate(self.segments[1:], start=1):
            if i * self.buffer_length < len(self.positions):
                segment.topleft = self.positions[i * self.buffer_length]
        # Ensure the deque doesn't store unnecessary positions
        max_positions_needed = (len(self.segments) - 1) * self.buffer_length
        while len(self.positions) > max_positions_needed:
            self.positions.pop()
        return dx, dy

            
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
        
    def check_collision(self):
        # Check left and right boundaries
        if self.segments[0].left < 0 or self.segments[0].right > 1000:
            return True
        # Check top and bottom boundaries
        if self.segments[0].top < 0 or self.segments[0].bottom > 1000:
            return True
        # # Check for collision with self
        # head_rect_centered = pg.Rect(
        #     self.segments[0].x + 5, 
        #     self.segments[0].y + 5, 
        #     self.segments[0].width - 5, 
        #     self.segments[0].height - 5
        # )
        # if self.player:
        #     for segment in self.segments[2:]:
        #         if head_rect_centered.colliderect(segment):
        #             return True
        #     return False

    def ai(self, items):
        '''TODO: study up on vector math to understand this better
            This will be useful for pathfinding later on
        '''
        
        if not self.target_item or self.frames_since_last_item > 100:
            self.target_item = random.choice(items)
            self.frames_since_last_item = 0

        # Calculate the direction vector towards the target item
        dx = self.target_item.rect.centerx - self.rect.centerx
        dy = self.target_item.rect.centery - self.rect.centery

        # Normalize the direction vector
        magnitude = (dx ** 2 + dy ** 2) ** 0.5
        if magnitude > 0:
            dx, dy = (dx / magnitude) * c.DEFAULT_SPEED, (dy / magnitude) * c.DEFAULT_SPEED
        else:
            dx, dy = 0, 0

        self.frames_since_last_item += 1
        
        return dx, dy