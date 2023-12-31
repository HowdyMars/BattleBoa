# This file will handle the resouce handling for the game, like images, sounds, etc.
import pygame as pg
import constants as c
from char import Character
from item import Item

class InitializeGame:
    def __init__(self,):
        self.init = pg.init()
        self.mixer_init = pg.mixer.init()
        self.screen = pg.display.set_mode((1000, 1000), pg.HWSURFACE | pg.DOUBLEBUF | pg.SCALED, vsync=1)
        self.clock = pg.time.Clock()
        self.player = Character(player=True)
        self.player2 = Character(400, 300)
        self.items = Item.create_item()
        for item in self.items:
            item.set_random_position()
        self.display_caption = pg.display.set_caption("BattleBoa")
        self.screen_fill = self.screen.fill(c.BLACK)
        self.movement_handler = Movement()


    def restart_game(self):
        # reinitalize the player and item
        self.player.__init__(player=True)
        self.player2.__init__(400, 300)
        self.items
        for item in self.items:
            item.set_random_position()
            
    def draw_text(self, text, font, x, y, color=c.WHITE, size=60):
        font_path = c.FONTS.get(font, c.FONTS["default"])
        font_style = pg.font.Font(font_path, size)
        txt = font_style.render(text, True, color)
        textRect = txt.get_rect()
        textRect.center = (x, y)
        
        self.screen.blit(txt, textRect)
        
    def sound_effects(self, sound, volume=0.5):
        sound_path = c.SOUNDS.get(sound, c.SOUNDS["item_collected"])
        sound = pg.mixer.Sound(sound_path)
        sound.set_volume(volume)
        sound.play()
        
            
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
    
        

        