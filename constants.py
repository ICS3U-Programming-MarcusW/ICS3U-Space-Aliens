#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: January 2023
# This constants file is for the Aqua-Kingdom game

# PyBadge screen size is 160x128 and sprites are 16x16
# Set the length of the screen vertically and horizontally
SCREEN_X = 160
SCREEN_Y = 128

# Define grid size for the screen
# The screen is a 10x8 grid of 16x16 pixel sprites
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8

# Define the size of the sprites
# A sprite is 16 pixels by 16 pixels
SPRITE_SIZE = 16

# Define the total number of aliens in the game
TOTAL_NUMBER_OF_ALIENS = 5

# Define the total number of lasers in the game
TOTAL_NUMBER_OF_LASERS = 5

# Define the ship speed in the game
SHIP_SPEED = 1

# Define the alien speed in the game
ALIEN_SPEED = 1

# Define the laser speed in the game
LASER_SPEED = 2

# Define how far the lasers/aliens will be off the screen for x coordinate
OFF_SCREEN_X = -100

# Define how far the lasers/aliens will be off the screen for y coordinate
OFF_SCREEN_Y = -100

# Make sure the bottom of sprite is off the screen from the top
OFF_TOP_SCREEN = -1 * SPRITE_SIZE

# Make sure the sprite is off the screen from the bottom
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE

# Define the frames per second (FPS)
FPS = 60

# Define the movement speed of the sprites
SPRITE_MOVEMENT_SPEED = 1

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}

# New palette for red filled text
RED_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)
