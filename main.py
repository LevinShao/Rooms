import json
import random
import time
import sys
from game_map import create_grid, place_monsters, place_daphne

# create typing effect
def typing_effect(text):
    for char in text:
        time.sleep(0.02)
        print(char, end='', flush=True)

# Create a random line of text from quotes.md using random.choice and typing effect
def random_line():
    with open("quotes.md", "r", encoding='utf-8') as f:
        lines = f.readlines()
        random_line = random.choice(lines)
        typing_effect(random_line)

# create a loading effect
def loading_effect(text):
    # clear the screen
    print("\033c", end='')
    for char in text:
        time.sleep(0.1)
        print(char, end='', flush=True)

def load_game():
    # load the grid_data from the json file
    try:
        with open("game_data.json", "r") as f:
            grid_data = json.load(f)
        return grid_data
    except FileNotFoundError:
        print("Game data not found. Creating new game...")
        return create_grid()

# create a function to print the grid_data as a table
def print_grid_data(grid_data):
    for row in grid_data:
        print(row, grid_data[row])
    print()
    
# create a function to start the game
def start_game():
    """Start the game when player presses Enter"""
    # use typing effect to prompt the player
    typing_effect("\nPress Enter to begin > ")
    
    # Wait for input
    input()
    
    # clear the screen
    print("\033c", end='')

#------------------LOADER------------------#

# create a loading function
def game_loader():
    grid = load_game()
    time.sleep(1)
    print("\033c", end='') # clear the screen

    typing_effect("Welcome to The Navigation Game - Insert Coins")
    time.sleep(2)
    print("\033c", end='')
    typing_effect("Just kidding, this game is free, the cake is a lie")
    time.sleep(1)
    print("\033c", end='') # clear the screen

    #load the welcome screen text from loader.md file
    try:
        with open("loader.md", "r", encoding='utf-8') as f:
            loader = f.read()
            typing_effect(loader)
    except FileNotFoundError:
        typing_effect("Welcome to The Navigation Game!")

#------------------MAIN------------------#

#create the grid
grid = create_grid()
grid = place_monsters(grid)
grid = place_daphne(grid)

#load the game
game_loader()

#start the game
start_game()

#------------------START------------------#

#clear the screen
print("\033c", end='')

# set player coordinates
player_coordinates = (0, 0)

# set the exit coordinates
exit_coordinates = (5, 5)

# if player coordinates are not the same as exit coordinates, keep playing
while player_coordinates != exit_coordinates:
    current_room = grid[player_coordinates[0]][player_coordinates[1]]
    
    #print the players current location, title and narrative
    typing_effect(current_room["title"])
    print()
    typing_effect(current_room["narrative"])

    #check if the player is in the same room as a monster
    if "M" in current_room:
        #print the monster's name
        print(f"\nYou have encountered a {current_room['M']['name']}!")
        # Add combat logic here if desired
    
    #check if the player is in the same room as daphne
    if "D" in current_room:
        #print the monster's name
        print("\nYou have found Daphne! Congratulations!")
        # break the loop
        break

    # get movement input
    while True:
        movement = input("\nUse W, A, S, D to move > ").lower()
        
        new_coordinates = player_coordinates
        if movement == "w":
            new_coordinates = (player_coordinates[0] - 1, player_coordinates[1])
        elif movement == "a":
            new_coordinates = (player_coordinates[0], player_coordinates[1] - 1)
        elif movement == "s":
            new_coordinates = (player_coordinates[0] + 1, player_coordinates[1])
        elif movement == "d":
            new_coordinates = (player_coordinates[0], player_coordinates[1] + 1)
        else:
            print("Invalid input. Use W, A, S, D to move.")
            continue
            
        # Check boundaries
        if (0 <= new_coordinates[0] < 6) and (0 <= new_coordinates[1] < 6):
            player_coordinates = new_coordinates
            break
        else:
            print("You can't go that way - you'll hit a wall!")
    
    # clear the screen
    print("\033c", end='')
    random_line()
    print()
    
#------------------END------------------#