#!/usr/bin/env python3

# Created by: Marcus Wehbi
# This program is the "Space Aliens" game for the PyBadge.
# It uses the ugame and stage libraries to manage the graphics
# and input for the game.


import stage
import ugame


def game_scene():
    # This function sets up and runs the main game scene.

    # Load the background and sprite image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Create the background grid using the image and set the size to 10x8 tiles
    background = stage.Grid(image_bank_background, 10, 8)

    # Create the ship sprite using image at index 5, with initial position
    # (72,57)
    ship = stage.Sprite(image_bank_sprites, 5, 72, 57)

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # Add the background and ship to the layers list
    game.layers = [ship] + [background]

    # Draw the background on the screen
    game.render_block()

    # Game Loop to repeat forever
    while True:
        # Get user input
        keys = ugame.buttons.get_pressed()

        # Check if the "A" button is pressed
        if keys & ugame.K_X:
            print("Button A pressed")
            # Perform action for "A" button press

        # Check if the "B" button is pressed
        if keys & ugame.K_O:
            print("Button B pressed")
            # Perform action for "B" button press

        # Check if the "Start" button is pressed
        if keys & ugame.K_START:
            print("Start button pressed")
            # Perform action for "Start" button press

        # Check if the "Select" button is pressed
        if keys & ugame.K_SELECT:
            print("Select button pressed")
            # Perform action for "Select" button press

        # Check if the "Right" button is pressed
        if keys & ugame.K_RIGHT:
            # Move the ship to the right
            ship.move(ship.x + 1, ship.y)

        # Check if the "Left" button is pressed
        if keys & ugame.K_LEFT:
            # Move the ship to the left
            ship.move(ship.x - 1, ship.y)

        # Check if the "Up" button is pressed
        if keys & ugame.K_UP:
            # Move the ship up
            ship.move(ship.x, ship.y - 1)

        # Check if the "Down" button is pressed
        if keys & ugame.K_DOWN:
            # Move the ship down
            ship.move(ship.x, ship.y + 1)

        # update game logic

        # Redraw the sprites on the screen
        game.render_sprites([ship])

        # Pause the loop to achieve 60fps frame rate
        game.tick()


if __name__ == "__main__":
    game_scene()
