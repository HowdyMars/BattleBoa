# This file will serve as the character class for the game
import pygame as pg
import constants as c
from collections import deque

class Character(pg.sprite.Sprite):
    def __init__(self, start_x=400, start_y=300, player=False):
        super().__init__()  # This is another way to call the parent class's __init__ method
        self.player = player
        self.original_dimensions = (40, 40) # width, height to test
        start_x = start_x - self.original_dimensions[0] // 2
        start_y = start_y - self.original_dimensions[1] // 2
        self.rect = pg.Rect(start_x, start_y, 40, 40)
        self.segments = [self.rect] # This will be a list of all the segments of the snake
        self.buffer_length = 7 # This is the buffer between segments
        self.positions = deque(maxlen=1000)
        self.last_dx = 0
        self.last_dy = c.DEFAULT_SPEED
        
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
        # head = self.segments[0]
        # pg.draw.rect(screen, c.PLAYER_RECT_RED, head)
        for segment in self.segments:
            pg.draw.rect(screen, c.PLAYER_RECT_GREEN, segment)
            
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
        dx, dy = 0,0
        if self.player:
            dx, dy = self.follow_mouse()
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
        
    def check_collision(self):
        # Check left and right boundaries
        if self.segments[0].left < 0 or self.segments[0].right > 800:
            return True
        # Check top and bottom boundaries
        if self.segments[0].top < 0 or self.segments[0].bottom > 600:
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
        

    def ai(self, screen, item):
        dx, dy = 0, 0
        # Distance from boundaries
        dist_left = self.rect.left
        dist_right = 800 - self.rect.right
        dist_top = self.rect.top
        dist_bottom = 600 - self.rect.bottom
        
        # Decide if the snake needs to change direction due to proximity to a boundary
        if dist_left < c.DEFAULT_SPEED and dx == -c.DEFAULT_SPEED:
            dy = c.DEFAULT_SPEED if self.rect.centery <= 300 else -c.DEFAULT_SPEED
            dx = 0
        elif dist_right < c.DEFAULT_SPEED and dx == c.DEFAULT_SPEED:
            dy = c.DEFAULT_SPEED if self.rect.centery <= 300 else -c.DEFAULT_SPEED
            dx = 0
        elif dist_top < c.DEFAULT_SPEED and dy == -c.DEFAULT_SPEED:
            dx = c.DEFAULT_SPEED if self.rect.centerx <= 400 else -c.DEFAULT_SPEED
            dy = 0
        elif dist_bottom < c.DEFAULT_SPEED and dy == c.DEFAULT_SPEED:
            dx = c.DEFAULT_SPEED if self.rect.centerx <= 400 else -c.DEFAULT_SPEED
            dy = 0
        else:
            # Original AI logic
            if self.rect.centery < item.rect.centery:
                dy = c.DEFAULT_SPEED
            elif self.rect.centery > item.rect.centery:
                dy = -c.DEFAULT_SPEED
            if self.rect.centerx < item.rect.centerx:
                dx = c.DEFAULT_SPEED
            elif self.rect.centerx > item.rect.centerx:
                dx = -c.DEFAULT_SPEED
                
        return dx, dy
