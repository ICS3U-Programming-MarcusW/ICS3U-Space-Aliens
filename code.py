#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: January 2023
# This program is the Aqua-Kingdom game for the PyBadge.
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

    # Get the splash scene sound ready
    # Open the "bubble.wav" file for reading as binary data
    splash_sound = open("bubble.wav", "rb")
    # Access the audio module from the ugame library
    sound = ugame.audio
    # Stop any currently playing sound
    sound.stop()
    # Un-mute the sound
    sound.mute(False)
    sound.play(splash_sound)

    # Load the background and sprite image banks
    # This will be used in the splash scene for a white background
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
    # Splash scene only has background for splash scene
    game.layers = [background]

    # Draw the background on the screen
    game.render_block()

    # Game Loop to repeat forever
    while True:
        # Wait 2 seconds before switching to the menu scene
        time.sleep(2.0)
        # Load menu scene
        menu_scene()


def menu_scene():
    # This function sets up and runs the menu  scene.

    # Load the background and sprite image banks
    # This will be used for a white background in the menu scene
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Add text objects for the menu scene
    text = []
    # Create a Text object with a width of 29, height of 12, no font, and the red palette
    text1 = stage.Text(
        width=29,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the proper position (20, 10)
    text1.move(20, 10)
    # Set the text to "Wehbi Game Studio"
    text1.text("Wehbi Game Studio")
    # Add the text object to the text list
    text.append(text1)

    # Create a second Text object with a width of 11, height of 10, no font, and the red palette
    text2 = stage.Text(
        width=11, height=10, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the proper position (40, 110)
    text2.move(40, 110)
    # Set the text to "PRESS START"
    text2.text("PRESS START TO PLAY")
    # Add the text object to the text list
    text.append(text2)

    # Create a third Text object with a width of 29, height of 10, no font, and the red palette
    text3 = stage.Text(
        width=29, height=10, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (40, 60)
    text3.move(40, 60)
    # Set the text
    text3.text("PRESS B FOR")
    # Add the text object to the text list
    text.append(text3)

    # Create a fourth Text object with a width of 29, height of 10, no font, and the red palette
    text4 = stage.Text(
        width=29, height=10, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text to the position (40, 68)
    text4.move(40, 68)
    # Set the text
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

    # Add the background and text to the layers list
    # For the menu scene, we only have the background and the text
    game.layers = text + [background]

    # Draw the background on the screen
    game.render_block()

    # Game Loop to repeat forever
    while True:
        # Get the user input (buttons pressed)
        keys = ugame.buttons.get_pressed()

        # Check if the "Start" button is pressed
        if keys & ugame.K_START != 0:
            game_scene()
            # Perform action for "Start" button press
            # which is to start the game scene

        # Check if the "B" button is pressed
        if keys & ugame.K_O != 0:
            instructions_scene()
            # Perform action for "B" button press
            # which is to start the instructions scene

        # Pause the loop to achieve 60fps frame rate
        game.tick()


def instructions_scene():
    # This function displays the instructions scene

    # Load the image "mt_game_studio.bmp" for the background
    # The background will be white
    image_bank_3 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Create a background object using the image and dimensions from constants
    background = stage.Grid(
        image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Add text objects for the menu scene
    text = []
    # Create a Text object with a width of 15, height of 12, no font, and the red palette
    text1 = stage.Text(
        width=15,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the proper position (20, 10)
    text1.move(20, 10)
    # Set the text to "AQUA-KINGDOM : INSTRUCTIONS"
    text1.text("AQUA-KINGDOM : INSTRUCTIONS")
    # Add the text object to the text list
    text.append(text1)

    # Create a Text object with a width of 17, height of 12, no font, and the red palette
    text2 = stage.Text(
        width=17,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the proper position (20, 50)
    text2.move(20, 45)
    # Set the text
    text2.text("Win-highest score")
    # Add the text object to the text list
    text.append(text2)

    # Create a Text object with a width of 20, height of 12, no font, and the red palette
    text3 = stage.Text(
        width=20,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )

    # Move the text to the position (20, 90)
    text3.move(20, 75)
    # Set the text
    text3.text("Point-shoot fire")
    # Add the text object to the text list
    text.append(text3)

    # Create a Text object with a width of 17, height of 12, no font, and the red palette
    text4 = stage.Text(
        width=17,
        height=12,
        font=None,
        palette=constants.RED_PALETTE,
        buffer=None,
    )
    # Move the text to the proper position (20, 70)
    text4.move(20, 115)
    # Set the text
    text4.text("1 life")
    # Add the text object to the text list
    text.append(text4)

    # Create a "Stage" object to manage the game graphics and input
    game = stage.Stage(ugame.display, constants.FPS)

    # Add the background and text objects to the layers list
    # For the instructions scene, we only need the background and text
    game.layers = text + [background]

    # Draw the background and text on the screen
    game.render_block()

    while True:
        # Get user input (buttons pressed)
        keys = ugame.buttons.get_pressed()

        # Check if the 'A' button is pressed
        if keys & ugame.K_X != 0:
            # If the 'A' button is pressed, run the menu scene
            menu_scene()

        game.tick()


def game_scene():
    # This function sets up and runs the main game scene.

    # Add a score for our video game
    # Set it to 0
    score = 0

    # Add lives for our video game
    # Set it to 1
    lives = 1

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

    # Create a text object to display the lives
    lives_text = stage.Text(width=29, height=14)
    # Clear the text object
    lives_text.clear()
    # Set the cursor position to (0,0)
    lives_text.cursor(0, 0)
    # Move the text to position (1,1)
    lives_text.move(80, 1)
    # Update the text with the current lives
    lives_text.text("Lives: {0}".format(lives))

    def show_alien():
        # This function takes an alien from off screen and moves it on screen.
        # It iterates through all the fire_aliens in the "fire_aliens" list,
        # checks if the x-coordinate of the alien is less than 0, meaning it is off the screen
        # if so, move the alien on the screen at a random x position between
        # 0 + constants.SPRITE_SIZE and constants.SCREEN_X - constants.SPRITE_SIZE,
        # and a fixed y position at constants.OFF_TOP_SCREEN */
        for alien_number in range(len(fire_aliens)):
            if fire_aliens[alien_number].x < 0:
                fire_aliens[alien_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                # The break statement is used to exit the loop once an alien is placed on screen
                break

    # Load the background and sprite image banks so that we can use them in the game
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Button that we want to keep the state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # Get sound ready
    # Open the "water_gun.wav" file for reading as binary data
    water_gun_sound = open("water_gun.wav", "rb")
    # Access the audio module from the ugame library
    sound = ugame.audio
    # Stop any currently playing sound
    sound.stop()
    # Un-mute the sound
    sound.mute(False)

    # Get waterfall sound ready
    # Open the "waterfall.wav" file for reading as binary data
    waterfall_sound = open("waterfall.wav", "rb")
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

    # Use nested for loops in order to create a random game scene background each time
    # Iterate through the x and y coordinates of the screen grid
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            # randomly pick a tile from 1 to 3
            tile_picked = random.randint(1, 3)
            # Place the randomly picked tile at the current x and y location
            # on the background
            background.tile(x_location, y_location, tile_picked)

    # Create the ship sprite using image at index 5, with initial position
    # (72,57)
    ship = stage.Sprite(image_bank_sprites, 5, 72, 85)

    # Create a list of fire_aliens
    fire_aliens = []
    # Create new alien objects and append them to the list
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(
            image_bank_sprites, 15, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        fire_aliens.append(a_single_alien)
    # Place one alien on the screen using a function
    show_alien()

    # Create a list of water_lasers for when we shoot
    water_lasers = []
    # Iterate over the total number of water_lasers specified in the constants module
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        # Create a new laser object using the image bank and initial position
        #  off screen
        a_single_laser = stage.Sprite(
            image_bank_sprites, 12, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        # Append the laser object to the list of water_lasers
        water_lasers.append(a_single_laser)

    # Create a "Stage" object to manage the game graphics and input
    # Set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)

    # Add to the water layers to the list including everything else
    game.layers = (
        [score_text] + [lives_text] + water_lasers + [ship] + fire_aliens + [background]
    )

    # Draw the background on the screen
    game.render_block()

    # Game Loop to repeat forever
    while True:
        # Getting the users input (buttons pressed)
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
        # Firing water_lasers and making sound when 'A' button is pressed
        if a_button == constants.button_state["button_just_pressed"]:
            # Fire a water laser if we have enough power
            # (have not used up all the water_lasers)
            # Go through the number of water_lasers we have
            for laser_number in range(len(water_lasers)):
                # Move the laser from off the screen to the location of the
                # sprite shooting it
                if water_lasers[laser_number].x < 0:
                    water_lasers[laser_number].move(ship.x, ship.y)
                    # Play sound if A was just pressed
                    sound.play(water_gun_sound)
                    break

        # Each frame move the water_lasers, that have been fired up
        # Check every laser
        for laser_number in range(len(water_lasers)):
            # Check if one of the lasers is on the screen
            if water_lasers[laser_number].x > 0:
                # If it is, move it up by 2 (the laser speed)
                water_lasers[laser_number].move(
                    water_lasers[laser_number].x,
                    water_lasers[laser_number].y - constants.LASER_SPEED,
                )
                # Check if the laser has gone off the top of the screen
                if water_lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    # If it has, move it back to the holding location
                    # off the screen
                    water_lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

        # Iterate through all the fire_aliens in the "fire_aliens" list
        for alien_number in range(len(fire_aliens)):
            # Check if the x-coordinate of the alien is greater than 0, meaning
            # it is on the screen
            if fire_aliens[alien_number].x > 0:
                # Move the alien down by adding the ALIEN_SPEED to its
                # y-coordinate
                fire_aliens[alien_number].move(
                    fire_aliens[alien_number].x,
                    fire_aliens[alien_number].y + constants.ALIEN_SPEED,
                )
                # Check if the y-coordinate of the alien is greater than the
                # SCREEN_Y value, meaning it has gone off the screen
                if fire_aliens[alien_number].y > constants.SCREEN_Y:
                    # Move the alien to the OFF_SCREEN_X and OFF_SCREEN_Y coordinates
                    # to remove it from the game screen
                    fire_aliens[alien_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
                    # Call the show_alien function to place an alien back on the screen
                    # This is to replace the fire alien that went off the screen by the bottom
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

        # Iterate through the water_lasers
        for laser_number in range(len(water_lasers)):
            # Check if the laser is on screen
            if water_lasers[laser_number].x > 0:
                # Iterate through the fire_aliens
                for alien_number in range(len(fire_aliens)):
                    # Check if the alien is on screen
                    if fire_aliens[alien_number].x > 0:
                        # Check if the laser and alien have collided
                        # Change the hit-box logic in order to suit my sprite
                        if stage.collide(
                            water_lasers[laser_number].x + 4,
                            water_lasers[laser_number].y + 2,
                            water_lasers[laser_number].x + 11,
                            water_lasers[laser_number].y + 12,
                            fire_aliens[alien_number].x,
                            fire_aliens[alien_number].y + 6,
                            fire_aliens[alien_number].x + 15,
                            fire_aliens[alien_number].y + 15,
                        ):
                            # You hit an alien
                            # Move the alien off screen
                            fire_aliens[alien_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            # Move the laser off screen
                            water_lasers[laser_number].move(
                                constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                            )
                            # Stop any currently playing sound
                            sound.stop()
                            # Play the sound of the alien being hit
                            sound.play(waterfall_sound)
                            # Show two new fire_aliens on the screen using the function
                            show_alien()
                            show_alien()
                            # Increase the score by 1 for killing a fire alien
                            score = score + 1
                            # Clear the score and then reprint it in the same spot
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))

        # Check if any of the fire_aliens on screen have collided with the ship
        for alien_number in range(len(fire_aliens)):
            # Check if the x-coordinate of the alien is greater than 0, meaning it is on the screen
            if fire_aliens[alien_number].x > 0:
                # Check for collision between the current alien and the ship using the `stage.collide` function
                # This function takes the x and y coordinates of the bounding box of each object
                # In this case, the bounding box/hit-box has been handled and manipulated for my personal
                # game so that the user has a better results
                if stage.collide(
                    fire_aliens[alien_number].x + 2,
                    fire_aliens[alien_number].y + 2,
                    fire_aliens[alien_number].x + 15,
                    fire_aliens[alien_number].y + 15,
                    ship.x + 7,
                    ship.y + 7,
                    ship.x + 8,
                    ship.y + 15,
                ):
                    # Decrease the lives
                    lives -= 1
                    # Clear the score and then reprint it in the same spot
                    lives_text.clear()
                    lives_text.cursor(0, 0)
                    lives_text.move(80, 1)
                    lives_text.text("Lives: {0}".format(lives))
                    # When the user runs out of lives, end the game
                    if lives == 0:
                        # Clear the score and then reprint it
                        score_text.clear()
                        score_text.cursor(0, 0)
                        score_text.move(1, 1)
                        score_text.text("Score: {0}".format(score))
                        # If collision is detected, stop any currently playing sound
                        sound.stop()
                        # Play the crash sound
                        sound.play(crash_sound)
                        # Wait for 3 seconds before moving on to the game over scene
                        time.sleep(3.0)
                        # Call the game over scene and pass in the current score
                        game_over_scene(score)

        # Redraw the sprites on the screen
        game.render_sprites(fire_aliens + water_lasers + [ship])
        # Pause the loop to achieve 60fps frame rate
        game.tick()


def game_over_scene(final_score):
    # This function displays the game over scene with the final score and
    # allows the user to restart the game by pressing the SELECT button.

    # Load the image "mt_game_studio.bmp"
    # This will be used in the splash scene for a white background
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Create a background object using the image and dimensions from constants
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Create a list to store text objects for the game over scene
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
    # For the game over scene, we will only need the background and the text
    game.layers = text + [background]

    # Draw the background and text on the screen
    game.render_block()

    while True:
        # Check if the SELECT button is pressed
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_SELECT != 0:
            # Reload the game if SELECT is pressed by using the reload function
            # taken from the supervisor module
            supervisor.reload()

        game.tick()


if __name__ == "__main__":
    # Start the game by running the splash scene
    splash_scene()
