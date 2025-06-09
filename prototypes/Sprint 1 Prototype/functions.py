# With lots of background research and extensive testing, this code has somehow took me just around an hour to write.
# Will add lots of code comments since last time a major critique was that I didn't add enough comments to my code.

import time # time module is needed for the fancy text effect
import random # random module is used to generate room descriptions

current_room = 0  # Start at Room 000

# A fancy text function to simulate typing effect
# I learnt this effect from Stack Overflow a few weeks ago, found it quite interesting, and adapted it for my game.
def fancy_text(text):
    """Print text with a typing effect to make it look less boring than usual."""
    for char in text:
        time.sleep(0.02)  # This sets the typing speed, 0.02s (20 miliseconds) is the delay between each character
        print(char, end='', flush=True)
    print()  # Add a new line at the end to properly format the output

# Show the introduction text when someone first boots up the game
def show_intro():
    print("======================================")
    print("      DOORS GAME CLI Prototype v1     ")
    print("======================================")
    print("\nWelcome to the Doors Game CLI Prototype! This is an extremely simple level-1 prototype of my actual project.")
    print("\nNavigate with W (forward) / S (backward).\n")

# ------------------------ ROOM HANDLING FUNCTIONS ------------------------

# Room description templates
# The program will randomly select one of these 5 descriptions for each room using the random module
ROOM_TYPES = [
    "A dimly lit hallway with flickering lights.",
    "A spacious chamber with strange markings on the walls.",
    "A narrow passageway that creaks with every step.",
    "A circular room with an eerie humming sound.",
    "A damp corridor with water dripping from the ceiling."
]

# The arrows pointing to either the "str" or "int" classes are called TYPE HINTS.
# Type hints are used to indicate what type of value a function should return.
# Although unnecessary and doesn't affect the behavior of the actual function, they are useful for readability and maintainability of the code.
# I'm implementing them in this code after learning about them from a YouTube video about Agile Python development practices.
# They are VERY versatile for Agile programs!

# In this case, the expected return type of the get_room_description function is a string, hence the "-> str" at the end of the function definition.
def get_room_description() -> str:
    """Randomly picks a room description for a room out of the five above."""
    # Exceptions for special rooms
    if current_room == 0: # Room 000 is the entrance room with a fixed description.
        return "Entrance: A creaky wooden door behind you."
    elif current_room == 100: # Room 100 is the final "room" with a fixed description. This "room" will lead to the exit.
        return "You stumble into the outside, seeing a massive gate covered in angelic symbols in front of you."
    else: # For every single other room, select a random description from the ROOM_TYPES list.
        # Seed the random generator with room number for consistent descriptions
        random.seed(current_room)
        # First round the room number to 3 digits as a form of convention from the original Doors game, then return the randomly generaated description
        return f"Room {current_room:03d}: {random.choice(ROOM_TYPES)}"

# In this case, the expected return type of the get_room_description function is an integer, hence the "-> int" at the end of the function definition.
def get_current_room() -> int:
    """A mini function that returns the player's current room number."""
    return current_room # That's it, just a single line of code that returns the current room number

# ---------------------- MOVEMENT FUNCTIONS ----------------------

def move_forward() -> str:
    """Move to the next room (up to Room 100)."""
    global current_room # Use a global variable to keep track of the current room number

    # Normal movement logic for Room 000 to Room 099
    if current_room < 100:
        current_room += 1 # Increment the room number by 1 every time the player moves forward
        fancy_text(f"Moved forward to Room {current_room:03d}.") # Round the room number to 3 digits as a form of convention from the original Doors game
        time.sleep(0.5) # Short pause so the player can read the message properly
        print("\033c", end="") # Clear the console screen for a fresh look
        return ""
    # For Room 100 specifically.
    else:
        outro_text = (
            "\nYou've reached the exit beyond Room 100!\n" # Funny thing is that Room 100 isn't even technically a room because it's not an enclosed space, but I still label it as a room because the original Doors game also does that.            "Congratulations! You've beaten the first prototype of my game!\n"
            "However, take notice that there are absolutely no entities or obstacles in this game, because it's just a prototype.\n"
            "Meaning that this is essentially not even a game, more of an unfinished walking simulator.\n"
            "Now go out there and beat the real game featuring many difficult challenges!"
        )
        fancy_text(outro_text)
        time.sleep(1.5)  # Have a 1.5s pause for the victory message
        
        while True:
            # Ask the player if they want to replay or quit
            # strip() removes any leading or trailing whitespace, lower() allows the user to input lowercase letters so that they don't have 
            choice = input("\nWould you like to (R) replay or (Q) quit? ").strip().lower()
            if choice == 'r': # If the player wants to replay the game
                current_room = 0  # Reset to Room 000
                print("\033c", end="") # Clear console screen
                show_intro()  # Show intro again
                return ""
            elif choice == 'q': # Quit the game
                fancy_text("\nThanks for playing! Goodbye.")
                exit()
            else:
                fancy_text("Invalid choice. Please enter R or Q.") # If the player inputs an invalid choice, ask them to input again

def move_backward() -> str:
    """Move to the previous room (down to Room 000)."""
    global current_room # Use a global variable to keep track of the current room number
    # If the player is not in Room 000, which is the entrance room, allow them to move backward
    if current_room > 0:
        current_room -= 1 # Decrement the room number by 1 every time the player moves backward
        message = f"Moved backward to Room {current_room:03d}." # Round the room number to 3 digits as a form of convention from the original Doors game
        fancy_text(message)
        time.sleep(0.5) # Short pause so the player can read the message properly
        print("\033c", end="") # Clear the console screen for a fresh look
        return ""
    # Specifically for Room 000
    else:
        fancy_text("The door behind you is blocked. You can't turn back now.") # Show an error message if the player tries to go back from Room 000
        time.sleep(0.5) # Short pause
        print("\033c", end="") # Clear console screen
        return ""