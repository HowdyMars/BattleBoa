# This file will handle the resouce handling for the game, like images, sounds, etc.
import pygame as pg
import constants as c
from char import Character
from item import Item

class InitializeGame:
    def __init__(self):
        self.init = pg.init()
        self.screen = pg.display.set_mode((800, 600))
        self.display_caption = pg.display.set_caption("BattleBoa")
        self.screen_fill = self.screen.fill(c.BG_BLACK)
        self.movement_handler = Movement()
        
        self.set_up_game()
        
    def set_up_game(self):
        self.clock = pg.time.Clock()
        self.player = Character(player=True)
        self.player2 = Character(400, 300)
        self.item = Item()
        self.items = [self.item]

    def restart_game(self):
        # reinitalize the player and item
        self.player.__init__(player=True)
        self.player2.__init__(400, 300)
        self.item.__init__()
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
    

        