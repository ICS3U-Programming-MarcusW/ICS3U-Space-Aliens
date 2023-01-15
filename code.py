#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: January 2023
# This program is the "Space Aliens" game for the PyBadge.
# It uses the ugame and stage libraries to manage the graphics
# and input for the game.


import stage
import ugame
import time
import random

import constants


def splash_scene():
    # This function sets up and runs the splash scene.

    # Get sound ready
    # Open the "pew.wav" file for reading as binary data
    coin_sound = open("coin.wav", "rb")
    # Access the audio module from the ugame library
    sound = ugame.audio
    # Stop any currently playing sound
    sound.stop()
    # Un-mute the sound
    sound.mute(False)
    sound.play(coin_sound)

    # Load the background and sprite image banks
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Used this program to split the image into tile:
    # Organize images in order to create the splash screen image
    # https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background and ship to the layers list
    game.layers = [background]

    # Draw the background on the screen
    game.render_block()

    # Game Loop to repeat forever
    while True:
        # Wait 2 seconds before running switching to the menu scene
        time.sleep(2.0)
        menu_scene()


def menu_scene():
    # This function sets up and runs the menu game scene.

    # Load the background and sprite image banks
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Add text objects
    text = []
    # Create a Text object with a width of 29, height of 12, no font, and the red palette
    text1 = stage.Text(
        width=29,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the position (20, 10)
    text1.move(20, 10)
    # Set the text to "MT Game Studio"
    text1.text("Wehbi Game Studio")
    # Add the text object to the text list
    text.append(text1)

    # Create a Text object with a width of 29, height of 12, no font, and the red palette
    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (40, 110)
    text2.move(40, 110)
    # Set the text to "PRESS START"
    text2.text("PRESS START")
    # Add the text object to the text list
    text.append(text2)

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background and ship to the layers list
    game.layers = text + [background]

    # Draw the background on the screen
    game.render_block()

    # Game Loop to repeat forever
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()

        # Check if the "Start" button is pressed
        if keys & ugame.K_START != 0:
            game_scene()
            # Perform action for "Start" button press

        # Pause the loop to achieve 60fps frame rate
        game.tick()


def game_scene():
    # This function sets up and runs the main game scene.

    # Load the background and sprite image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Button that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Get sound ready
    # Open the "pew.wav" file for reading as binary data
    pew_sound = open("pew.wav", "rb")
    # Access the audio module from the ugame library
    sound = ugame.audio
    # Stop any currently playing sound
    sound.stop()
    # Un-mute the sound
    sound.mute(False)

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )
    # Use nested for loops to create a random game scene background each time
    # Iterate through the x and y coordinates of the screen grid
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            # randomly pick a tile from 1 to 3
            tile_picked = random.randint(1, 3)
            # place the randomly picked tile at the current x and y location
            # on the background
            background.tile(x_location, y_location, tile_picked)

    # Create the ship sprite using image at index 5, with initial position
    # (72,57)
    ship = stage.Sprite(image_bank_sprites, 5, 72, 57)

    # Create the alien sprite using image at index 9
    alien = stage.Sprite(
        image_bank_sprites,
        9,
        int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # Add to the layers list
    game.layers = [ship] + [alien] + [background]

    # Draw the background on the screen
    game.render_block()

    # Game Loop to repeat forever
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()

        # Check if the "A" button is pressed
        if keys & ugame.K_X != 0:
            # Check if the button was just pressed and update the button state
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            # Check if the button is still pressed and update the button state
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        # If the button is not pressed
        else:
            # Check if the button was just released and update the button state
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            # Update the button state to "up"
            else:
                a_button = constants.button_state["button_up"]

        # Check if the "B" button is pressed
        if keys & ugame.K_O != 0:
            print("Button B pressed")
            # Perform action for "B" button press

        # Check if the "Start" button is pressed
        if keys & ugame.K_START != 0:
            print("Start button pressed")
            # Perform action for "Start" button press

        # Check if the "Select" button is pressed
        if keys & ugame.K_SELECT != 0:
            print("Select button pressed")
            # Perform action for "Select" button press

        # Check if the "Right" button is pressed
        if keys & ugame.K_RIGHT != 0:
            # Move the ship to the right
            if ship.x <= 160:
                ship.move(ship.x + 1, ship.y)
            else:
                # If the sprite exceeds the right side of the screen
                # wrap it around to the left side
                ship.move(0, ship.y)

        # Check if the "Left" button is pressed
        if keys & ugame.K_LEFT != 0:
            # Move the ship to the left
            if ship.x >= -5:
                ship.move(ship.x - 1, ship.y)
            else:
                # If the sprite exceeds the left side of the screen
                # wrap it around to the right side
                ship.move(160, ship.y)

        # Check if the "Up" button is pressed
        if keys & ugame.K_UP != 0:
            # Move the ship up
            if ship.y >= -8:
                ship.move(ship.x, ship.y - 1)
            else:
                # If the sprite exceeds the top of the screen
                # wrap it around to the bottom
                ship.move(ship.x, 120)

        # Check if the "Down" button is pressed
        if keys & ugame.K_DOWN != 0:
            # Move the ship down
            if ship.y <= 120:
                ship.move(ship.x, ship.y + 1)
            else:
                # If the sprite exceeds the bottom of the screen
                # wrap it around to the top
                ship.move(ship.x, 0)

        # Update the game logic
        # Play sound if A button was just pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # Redraw the sprites on the screen
        game.render_sprites([ship] + [alien])

        # Pause the loop to achieve 60fps frame rate
        game.tick()


if __name__ == "__main__":
    splash_scene()
