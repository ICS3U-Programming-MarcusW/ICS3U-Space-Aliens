#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: January 2023
# This program is the "Space Aliens" game for the PyBadge.
# It uses the ugame and stage libraries to manage the graphics
# and input for the game.


import stage
import ugame

import constants


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
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

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

    # Add the background and ship to the layers list
    game.layers = [ship] + [alien] + [background]

    # Draw the background on the screen
    game.render_block()

    # Game Loop to repeat forever
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()

        # Check if the "A" button is pressed
        # Perform action for "A" button press - fire missile and make sound
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
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

        # update game logic
        # Play sound if A button was just pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # Redraw the sprites on the screen
        game.render_sprites([ship] + [alien])

        # Pause the loop to achieve 60fps frame rate
        game.tick()


if __name__ == "__main__":
    game_scene()
