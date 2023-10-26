# This is the main body of the program. It will be the only file that is run the game.
# load the modules
import pygame as pg
import constants as c
from resources import InitializeGame # I am initializing all the game resources in this module | keeping main.py clean
from item import Item
from icecream import ic

game = InitializeGame()

# Accessing the properties
init = game.init
display_caption = game.display_caption
screen = game.screen
clock = game.clock
screen_fill = game.screen_fill
player = game.player
player2 = game.player2
items = game.items
movement_handler = game.movement_handler
running = True

#==================#
#= Main-Game-Loop =#
#==================#

while running:
    # set the game clock
    clock.tick(60) # 60 fps
    
    # Clear the screen with fill
    screen.fill(c.BLACK)
    
    # Player movement and AI movement
    player_dx, player_dy = player.follow_mouse()
    player.move(player_dx, player_dy)
    
    ai_dx, ai_dy = player2.ai(items)
    player2.move(ai_dx, ai_dy)
    
#================#
#= Draw-Screen- =#
#================#

    # Title
    game.draw_text("BattleBoa", "infill" , 500, 20, c.YELLOW, 100)

    # # Draw a rectangle to represent the player
    player.draw(screen)
    # Draw a rectangle to represent the player2
    player2.draw(screen, c.BLUE)
    
    # Draw a rectangle to represent the item
    for item in items:
        item.draw(screen)


#==================#
#= Event-Handling =#
#==================#
    
    # Check for collision with wall
    if player.check_collision():
        game.restart_game()
        
    #Check for collision with [player2]
    for segment in player2.segments:
        if player.segments[0].colliderect(segment):
            ic("You Lose!")
            game.sound_effects("oops", 0.2)
            game.restart_game()
    # Check for collision with [player]
    for segment in player.segments:
        if player2.segments[0].colliderect(segment):
            ic("You Win!")
            game.sound_effects("hit_player", 0.2)
            game.restart_game()
            
    # # Check for collision with item
    for item in items:
        if item.check_collision(player.rect):
            item.set_random_position()
            game.sound_effects("item_collected", 0.3)
            player.grow(player_dx, player_dy)
            item.handle_collected(player.rect)
        if item.text_float:
            x = player.rect.centerx
            y = item.text_start_y
            game.draw_text("1", "infill", x, y, c.YELLOW, 60)
            if item.handle_collected(player.rect):
                item.text_float = False
                
        if player2.segments[0].colliderect(item.rect):
            item.set_random_position()
            player2.grow(ai_dx, ai_dy)
        
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            

#================#
#= Key-Handling =#
#================#

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False


    pg.display.flip()
    
#==================#
#= Quit-Game-Loop =#
#==================#

pg.quit()
    

