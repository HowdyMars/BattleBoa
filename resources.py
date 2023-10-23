# This file will handle the resouce handling for the game, like images, sounds, etc.
import pygame as pg
import constants as c

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