#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: January 2023
# This program is the "Space Aliens" game for the PyBadge.
# It uses the ugame and stage libraries to manage the graphics
# and input for the game.


import random
import time

import constants
import stage
import supervisor
import ugame


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

    menu_sound = open(".wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    music_loop = 0

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
        width=11, height=10, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (40, 110)
    text2.move(40, 110)
    # Set the text to "PRESS START"
    text2.text("PRESS START TO PLAY")
    # Add the text object to the text list
    text.append(text2)

    # Add text to tell the user where to find the instructions page
    text3 = stage.Text(
        width=29, height=10, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (40, 110)
    text3.move(40, 60)
    # Set the text to "PRESS START"
    text3.text("PRESS B FOR")
    # Add the text object to the text list
    text.append(text3)

    # Add second part of instructions page
    text4 = stage.Text(
        width=29, height=10, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (40, 110)
    text4.move(40, 68)
    # Set the text to "PRESS START"
    text4.text("INSTRUCTIONS")
    # Add the text object to the text list
    text.append(text4)

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

        # Check if the "B" button is pressed
        if keys & ugame.K_O != 0:
            instructions_scene()
            # Perform action for "B" button press

        # Pause the loop to achieve 60fps frame rate
        game.tick()

        # play sound
        if music_loop >= 1875.96000075:
            sound.play(menu_sound)
            music_loop = 0
        else:
            music_loop += 1


def instructions_scene():
    # This function displays the game over scene with the final score and
    # allows the user to restart the game by pressing the SELECT button.

    # Load the image "mt_game_studio.bmp"
    image_bank_3 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Create a background object using the image and dimensions from constants
    background = stage.Grid(
        image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    text = []
    # Create a Text object with a width of 29, height of 12, no font, and the red palette
    text1 = stage.Text(
        width=15,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the position (20, 10)
    text1.move(20, 10)
    # Set the text to "MT Game Studio"
    text1.text("AQUA-KINGDOM : INSTRUCTIONS")
    # Add the text object to the text list
    text.append(text1)

    # Create a Text object with a width of 29, height of 12, no font, and the red palette
    text2 = stage.Text(
        width=15,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the position (20, 10)
    text2.move(20, 30)
    # Set the text to "MT Game Studio"
    text2.text(" - Win by getting the highest score.")
    # Add the text object to the text list
    text.append(text2)

    # Create a Text object with a width of 29, height of 12, no font, and the red palette
    text3 = stage.Text(
        width=15,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the position (20, 10)
    text3.move(20, 40)
    # Set the text to "MT Game Studio"
    text3.text(
        " - Use your water blaster to shoot the fire. Hit it, you get a point. It hits you, you lose a life."
    )
    # Add the text object to the text list
    text.append(text3)

    # Create a "Stage" object to manage the game graphics and input
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background and text objects to the layers list
    game.layers = text + [background]

    # Draw the background and text on the screen
    game.render_block()

    while True:
        # Check if the SELECT button is pressed
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X != 0:
            # Reload the game if SELECT is pressed
            menu_scene()

        game.tick()


def game_scene():
    # This function sets up and runs the main game scene.

    # Add a score for our video game
    score = 0

    # Create a text object to display the score
    score_text = stage.Text(width=29, height=14)
    # Clear the text object
    score_text.clear()
    # Set the cursor position to (0,0)
    score_text.cursor(0, 0)
    # Move the text to position (1,1)
    score_text.move(1, 1)
    # Update the text with the current score
    score_text.text("Score: {0}".format(score))

    def show_alien():
        # This function takes an alien from off screen and moves it on screen.
        # It iterates through all the aliens in the "aliens" list,
        # checks if the x-coordinate of the alien is less than 0, meaning it is off the screen
        # if so, move the alien on the screen at a random x position between
        # 0 + constants.SPRITE_SIZE and constants.SCREEN_X - constants.SPRITE_SIZE,
        # and a fixed y position at constants.OFF_TOP_SCREEN */
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                # The break statement is used to exit the loop once an alien is placed on screen
                break

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

    # Get boom sound ready
    # Open the "boom.wav" file for reading as binary data
    boom_sound = open("boom.wav", "rb")
    # Access the audio module from the ugame library
    sound = ugame.audio
    # Stop any currently playing sound
    sound.stop()
    # Un-mute the sound
    sound.mute(False)

    # Get crash sound ready
    # Open the "crash.wav" file for reading as binary data
    crash_sound = open("crash.wav", "rb")
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
    ship = stage.Sprite(image_bank_sprites, 5, 72, 85)

    # Create a list of aliens
    aliens = []
    # Create new alien objects and append them to the list
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(
            image_bank_sprites, 15, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        aliens.append(a_single_alien)
    # Place one alien on the screen, maybe using a function
    show_alien()

    # Create a list of lasers for when we shoot
    lasers = []
    # Iterate over the total number of lasers specified in the constants module
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        # Create a new laser object using the image bank and initial position
        #  off screen
        a_single_laser = stage.Sprite(
            image_bank_sprites, 12, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        # Append the laser object to the list of lasers
        lasers.append(a_single_laser)

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # Add to the layers list
    game.layers = [score_text] + lasers + [ship] + aliens + [background]

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
        # Firing lasers and making sound when 'A' button is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            # Fire a laser if we have enough power
            # (have not used up all the lasers)
            # Go through the number of lasers we have
            for laser_number in range(len(lasers)):
                # Move the laser from off the screen to the location of the
                # sprite shooting it
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    # Play sound if A was just pressed
                    sound.play(pew_sound)
                    break

        # Each frame move the lasers, that have been fired up
        # Check every laser
        for laser_number in range(len(lasers)):
            # Check if one of the lasers is on the screen
            if lasers[laser_number].x > 0:
                # If it is, move it up by 2
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED,
                )
                # Check if the laser has gone off the top of the screen
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    # If it has, move it back to the holding location
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

        # Iterate through all the aliens in the "aliens" list
        for alien_number in range(len(aliens)):
            # Check if the x-coordinate of the alien is greater than 0, meaning
            # it is on the screen
            if aliens[alien_number].x > 0:
                # Move the alien down by adding the ALIEN_SPEED to its
                # y-coordinate
                aliens[alien_number].move(
                    aliens[alien_number].x,
                    aliens[alien_number].y + constants.ALIEN_SPEED,
                )
                # Check if the y-coordinate of the alien is greater than the
                # SCREEN_Y value, meaning it has gone off the screen
                if aliens[alien_number].y > constants.SCREEN_Y:
                    # Move the alien to the OFF_SCREEN_X and OFF_SCREEN_Y coordinates
                    # to remove it from the game screen
                    aliens[alien_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
                    # Call the show_alien function to place an alien back on the screen
                    show_alien()
                    # Decrease the score for missing an alien
                    score -= 1
                    # Make sure the score never goes below 0
                    if score < 0:
                        score = 0
                    # Clear the score and then reprint it
                    score_text.clear()
                    score_text.cursor(0, 0)
                    score_text.move(1, 1)
                    score_text.text("Score: {0}".format(score))

        # Iterate through the lasers
        for laser_number in range(len(lasers)):
            # Check if the laser is on screen
            if lasers[laser_number].x > 0:
                # Iterate through the aliens
                for alien_number in range(len(aliens)):
                    # Check if the alien is on screen
                    if aliens[alien_number].x > 0:
                        # Check if the laser and alien have collided
                        if stage.collide(
                            lasers[laser_number].x + 4,
                            lasers[laser_number].y + 2,
                            lasers[laser_number].x + 11,
                            lasers[laser_number].y + 12,
                            aliens[alien_number].x,
                            aliens[alien_number].y + 6,
                            aliens[alien_number].x + 15,
                            aliens[alien_number].y + 15,
                        ):
                            # You hit an alien
                            # Move the alien off screen
                            aliens[alien_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            # Move the laser off screen
                            lasers[laser_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            # Stop any currently playing sound
                            sound.stop()
                            # Play the sound of the alien being hit
                            sound.play(boom_sound)
                            # Show two new aliens on the screen
                            show_alien()
                            show_alien()
                            # Increase the score by 1
                            score = score + 1
                            # Clear the score and then reprint it
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))

        # Check if any of the aliens on screen have collided with the ship
        for alien_number in range(len(aliens)):
            # Check if the x-coordinate of the alien is greater than 0, meaning it is on the screen
            if aliens[alien_number].x > 0:
                # Check for collision between the current alien and the ship using the `stage.collide` function
                # This function takes the x and y coordinates of the bounding box of each object
                # In this case, the bounding box of the alien is defined as x+1, y, x+15, y+15
                # and the bounding box of the ship is defined as ship.x, ship.y, ship.x + 15, ship.y + 15
                if stage.collide(
                    aliens[alien_number].x + 2,
                    aliens[alien_number].y + 2,
                    aliens[alien_number].x + 15,
                    aliens[alien_number].y + 15,
                    ship.x + 7,
                    ship.y + 7,
                    ship.x + 8,
                    ship.y + 15,
                ):
                    # If collision is detected, stop any currently playing sound
                    sound.stop()
                    # Play the crash sound
                    sound.play(crash_sound)
                    # Wait for 3 seconds before moving on to the game over scene
                    time.sleep(3.0)
                    # Call the game over scene and pass in the current score
                    game_over_scene(score)

        # Redraw the sprites on the screen
        game.render_sprites(aliens + lasers + [ship])
        # Pause the loop to achieve 60fps frame rate
        game.tick()


def game_over_scene(final_score):
    # This function displays the game over scene with the final score and
    # allows the user to restart the game by pressing the SELECT button.

    # Load the image "mt_game_studio.bmp"
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Create a background object using the image and dimensions from constants
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Create a list to store text objects
    text = []

    # Create a Text object with a width of 29, height of 14, no font, and the blue palette
    text1 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (20, 20)
    text1.move(20, 20)
    # Set the text to the final score
    text1.text("Final Score: {:0>2d}".format(final_score))
    # Add the text object to the text list
    text.append(text1)

    # Create a Text object with a width of 29, height of 14, no font, and the blue palette
    text2 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (43, 60)
    text2.move(43, 60)
    # Set the text to "GAME OVER"
    text2.text("GAME OVER")
    # Add the text object to the text list
    text.append(text2)

    # Create a Text object with a width of 29, height of 14, no font, and the blue palette
    text3 = stage.Text(
        width=29, height=14, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (32, 110)
    text3.move(32, 110)
    # Set the text to "PRESS SELECT"
    text3.text("PRESS SELECT")
    # Add the text object to the text list
    text.append(text3)

    # Create a "Stage" object to manage the game graphics and input
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background and text objects to the layers list
    game.layers = text + [background]

    # Draw the background and text on the screen
    game.render_block()

    while True:
        # Check if the SELECT button is pressed
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_SELECT != 0:
            # Reload the game if SELECT is pressed
            supervisor.reload()

        game.tick()


if __name__ == "__main__":
    splash_scene()
