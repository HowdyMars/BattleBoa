# This is the main body of the program. It will be the only file that is run the game.
# load the modules
import pygame as pg
import constants as c
from resources import InitializeGame # I am initializing all the game resources in this module | keeping main.py clean

game = InitializeGame()

# Accessing the properties
screen = game.screen
clock = game.clock
player = game.player
items = game.items
helper = game.helper
movement_handler = game.movement_handler

running = True

#==================#
#= Main-Game-Loop =#
#==================#

while running:
    
    # Clear the screen with fill
    screen.fill(c.BG_BLACK)

#==================#
#= Event-Handling =#
#==================#
    
    # Check for collision with wall
    if player.check_collision():
        print("Collision!")
        helper.restart_game()

    for item in items:
        if player.segments[0].colliderect(item.rect):
            item.set_random_position()
            player.grow(dx, dy)
            
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

#================#
#= Draw-Screen- =#
#================#

    # Draw a rectangle to represent the player
    player.draw(screen)
    
    # Draw a rectangle to represent the item
    for item in items:
        item.draw(screen)

    # set the game clock
    clock.tick(60) # 60 fps
    
    pg.display.flip()
    
#==================#
#= Quit-Game-Loop =#
#==================#

pg.quit()
    

