#!/usr/bin/env python3

# This program is the "Pyramid Escape" game for the PyBadge.
# It is written in Python and uses the ugame and stage libraries
# to manage the graphics and input for the game.

import ugame
import stage


def game_scene():
    # This function is in charge of setting up and running the main game scene.

    # Load the background image and create a "Grid" object using the image
    # and a size of 10x8 tiles.
    image_bank_background = stage.Bank.from_bmp16("pacBackgroundImg.bmp")
    background = stage.Grid(image_bank_background, 10, 8)

    # Create a "Stage" object to manage the game graphics and input,
    # and set the frame rate to 60fps.
    game = stage.Stage(ugame.display, 60)

    # Set the "layers" property of the "Stage" object to a list containing
    # the "Grid" object, which serves as the background for the game.
    game.layers = [background]

    # Render the background image on the screen.
    game.render_block()

    # Enter an infinite loop to update the game and handle user input.
    while True:
        pass  # Placeholder for future code


# Run the "game_scene()" function when the program is executed.
if __name__ == "__main__":
    game_scene()
