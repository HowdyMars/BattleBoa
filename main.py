# This is the main body of the program. It will be the only file that is run the game.
# load the modules
import pygame as pg
import constants as c
from char import Character
from resources import Movement
from item import Item

# initialize pg
pg.init()
# initialize the display
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("BattleBoa")
# set the game clock
clock = pg.time.Clock()
# set the game loop
running = True
# Fill background
screen.fill(c.BG_BLACK)
# initialize the character
player = Character()
# initialize the item
item = Item()
# initialize the movement
movement_handler = Movement()

#==================#
#= Main-Game-Loop =#
#==================#

while running:
    
    # Clear the screen with fill
    screen.fill(c.BG_BLACK)

#==================#
#= Event-Handling =#
#==================#

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    movement_handler.update_direction(pg.key.get_pressed())
    dx, dy = movement_handler.move()
    player.move(dx, dy)
            
#================#
#= Key-Handling =#
#================#

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False

#=================#
#= Screen-Update =#
#=================#


    
#================#
#= Draw-Screen- =#
#================#

    # Draw a rectangle to represent the player
    player.draw(screen)
    
    # Draw a rectangle to represent the item
    item.draw(screen)

    # set the game clock
    clock.tick(60) # 60 fps
    
    pg.display.flip()
    
#==================#
#= Quit-Game-Loop =#
#==================#

pg.quit()
    

