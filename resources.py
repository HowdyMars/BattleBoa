# This file will handle the resouce handling for the game, like images, sounds, etc.
import pygame as pg
import constants as c
from char import Character
from item import Item

class InitializeGame:
    def __init__(self):
        pg.init()
        
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("BattleBoa")
        self.clock = pg.time.Clock()
        self.screen.fill(c.BG_BLACK)
        
        self.player = Character()
        self.item = Item()
        self.items = [self.item]
        self.helper = Helper(self.player, self.item)
        self.movement_handler = Movement()
        
    def initialize_game():
        pg.init()
        screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("BattleBoa")
        clock = pg.time.Clock()
        screen.fill(c.BG_BLACK)
        
        player = Character()
        item = Item()
        items = [item]  # Using a list comprehension
        helper = Helper(player, item)
        movement_handler = Movement()

        return screen, clock, player, item, items, helper, movement_handler
class Movement():
    def __init__(self, speed=c.DEFAULT_SPEED):   # setting a default speed of 5
        self.x, self.y = 0, 0
        self.speed = speed
        self.direction = "RIGHT"
        
    def update_direction(self, keys):
        if keys[pg.K_UP] or keys[pg.K_w]:
            if self.direction != "DOWN":
                self.direction = "UP"
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            if self.direction != "UP":
                self.direction = "DOWN"
        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            if self.direction != "RIGHT":
                self.direction = "LEFT"
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            if self.direction != "LEFT":
                self.direction = "RIGHT"
                
        opposite_directions = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        new_direction = self.direction
        if new_direction and new_direction != opposite_directions[self.direction]:
            self.direction = new_direction
        
    def move(self):
        dx, dy = 0, 0
        if self.direction == "UP":
            dy = -self.speed
        elif self.direction == "DOWN":
            dy = self.speed
        elif self.direction == "LEFT":
            dx = -self.speed
        elif self.direction == "RIGHT":
            dx = self.speed

        return dx, dy
    
class Helper():
    def __init__(self, player, item):
        self.player = player
        self.item = item
    
    def restart_game(self):
        # reinitalize the player and item
        self.player.__init__()
        self.item.__init__()

        