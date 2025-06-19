# Total time to write: Around 3 days
# I had to consult some people online just to debug and get help with some parts of the code
# Since I had serious problems with the entity spawning system and the replay function

# Note: I have given up trying to create Levin's Shop in this prototype
# It was way too hard to implement, and I felt like introducing it in this prototype would be too early.
# I definitely will find a way to implement it in later versions, but I'm gonna take a rest now.
# Although this would make the coins useless, I'm keeping them here anyways just for experimentation purposes for the system.

# Also, due to the serious time struggles I had with this prototype, I have not had enough time to fully playtest the game
# Therefore bugs are definitely present in the game and don't be surprised if you find some
# But I'd much rather work on the next few prototypes than fix bugs in this one, since this is just a prototype and not the final product

# --------------------------------------------------------------------------------------------------------------------------------

import time # Time is needed for the fancy text effect and pauses
import random # Random is very useful in this game, almost every function relies on it
from constants import * # Import everything from constants.py

# Game state
current_room = 0 # Start at Room 000
player_health = 100 # Start with full health
inventory = [] # A list that stores the player's items (i.e. their inventory)
coins = 0 # A variable that stores the player's coins, which can be used to buy items.

# A dictionary that stores the game data, such as visited rooms, looted rooms, and dark rooms
# set() is used to store unique values, which is useful for visited and looted rooms
game_data = {
    "visited_rooms": set(), # Visited rooms will be stored here
    "looted_rooms": set(), # Looted rooms will be stored here
    # Dark rooms will be stored here, generated at the start of the game
    # There will be at least 10 dark rooms, with some of them having a 50% chance to make the next room dark as well
    "dark_rooms": set(),
    "entity_spawned_rooms": set() # Track rooms that have had entities spawn in them, and make sure that they don't spawn in that room again
}

# Show the introduction text when someone first boots up the game
def show_intro():
    print("===================================")
    print("      DOORS GAME CLI Prototype     ")
    print("===================================")
    print("\nWelcome to the Doors Game CLI Prototype! This is an extremely simple level-2 prototype of my actual project.")
    print("\nNavigate with W (forward) / S (backward).\n")

# A fancy text function to simulate typing effect
# I learnt this effect from Stack Overflow a few weeks ago, found it quite interesting, and adapted it for my game.
def fancy_text(text):
    """Print text with a typing effect to make it look less boring than usual."""
    for char in text:
        time.sleep(0.02)  # This sets the typing speed, 0.02s (20 miliseconds) is the delay between each character
        print(char, end='', flush=True)
    print()  # Add a new line at the end to properly format the output

def move_forward() -> str:
    """Move to the next room (up to Room 100)."""
    global current_room # Use global variable to keep track of the current room number

    # Normal movement logic for Room 000 to Room 099
    if current_room < 100:
        current_room += 1 # Increment the room number by 1 every time the player moves forward
        # Mark room as visited when moving forward
        game_data["visited_rooms"].add(current_room)
        # Round the room number to 4 digits as a form of convention from the original Doors game
        fancy_text(f"Moved forward to Room {current_room:04d}.")
        time.sleep(0.5) # Short pause so the player can read the message properly
        print("\033c", end="") # Clear the console screen for a fresh look
        return ""
    # For Room 100 specifically
    else:
        outro_text = (
            "\nYou've reached the exit beyond Room 100!\n" # Funny thing is that Room 100 isn't even technically a room because it's not an enclosed space, but I still label it as a room because the original Doors game also does that.
            "Congratulations! You've beaten the second prototype of my game!\n"
            "However, take notice that there are absolutely no entities or obstacles in this game, because it's just a prototype.\n"
            "Meaning that this is essentially not even a game, more of an unfinished walking simulator.\n"
            "Now go out there and beat the real game featuring many difficult challenges!"
        )
        fancy_text(outro_text)
        time.sleep(1) # Have a 1s pause for the victory message
        replay_prompt() # Ask the player if they want to replay or quit after the victory message
        return ""

def move_backward() -> str:
    """Move to the previous room (down to Room 000)."""
    global current_room # Use a global variable to keep track of the current room number
    # If the player is not in Room 000, which is the entrance room, allow them to move backward
    if current_room > 0:
        current_room -= 1 # Decrement the room number by 1 every time the player moves backward
        # No need to mark as visited here since forward movement already did it
        # Round the room number to 4 digits as a form of convention from the original Doors game
        fancy_text(f"Moved backward to Room {current_room:04d}.")
        time.sleep(0.5) # Short pause so the player can read the message properly
        print("\033c", end="") # Clear the console screen for a fresh look
        return ""
    else: # Specifically for Room 000
        # Show an error message if the player tries to go back from Room 000
        fancy_text("The door behind you is blocked. You can't turn back now.")
        time.sleep(0.5) # Short pause
        print("\033c", end="") # Clear the screen
        return ""
    
# In this case, the expected return type of the get_room_description function is a string, hence the "-> str" at the end of the function definition.
def get_room_description() -> str:
    """Randomly picks a room description for a room out of the five above."""
    # Exceptions for special rooms
    if current_room == 0: # Room 000 is the entrance room with a fixed description.
        return "Reception Area: A creaky wooden door behind you."
    elif current_room == 100: # Room 100 is the final "room" with a fixed description. This "room" will lead to the exit.
        return "You stumble into the outside, seeing a massive gate covered in angelic symbols in front of you."
    elif current_room in game_data["dark_rooms"]:
        return f"⚠️  DARK ROOM: {get_dark_room_description()}"
    else: # For every single other room, select a random description from the ROOM_TYPES list.
        random.seed(current_room)
        return f"Room {current_room:04d}: {random.choice(ROOM_TYPES)}"
    
def generate_dark_rooms():
    """Randomly assigns dark rooms for the run."""
    # Assign 10 dark rooms randomly between 1 and 99 (excluding 0 and 100)
    num_dark_rooms = max(10, int(100 * 0.1))
    dark_rooms = set(random.sample(range(1, 100), num_dark_rooms))
    # Make some dark rooms consecutive
    for room in list(dark_rooms):
        if random.random() < 0.5 and room < 99: # 50% chance to make the next room dark as well
            dark_rooms.add(room + 1) # Apply the dark room effect to the next room
    return dark_rooms # Return the set of dark rooms

def spawn_entities():
    """
    Spawn entities in the current room.
    
    This function's main purpose is to handle entity spawning in rooms
    but it's also used to ensure that once a room has had an entity spawned, 
    then it doesn't spawn another entity ever again for the duration of the game.
    """
    global current_room, player_health # Access current room and player health variables

    # Don't spawn in first/last room or rooms that have already had entities
    if (current_room == 0 or current_room == 100 or 
        current_room in game_data.get("entity_spawned_rooms", set())):
        return True

    # SYSTEM CHECKS THE CURRENT ROOM. IS IT A DARK ROOM?
    # IF YES, SET SPAWN RATE TO 40%, IF NO, CHECK IF IT'S A ROOM 090 OR HIGHER
    # IF YES, SET SPAWN RATE TO 30%, IF NO, SET SPAWN RATE TO 15%, SINCE THAT ROOM SHOULD BE A ROOM FROM 001-089 AND NOT DARK

    if current_room in game_data["dark_rooms"]:
        spawn_chance = 0.4 # Set 40% spawn chance in dark rooms
    elif current_room >= 90:
        spawn_chance = 0.3 # 30% chance since difficulty is ramped up when the player reaches the final few rooms
    else:
        spawn_chance = 0.15 # Default spawn chance

    if random.random() < spawn_chance: # If entity spawns
        entity = random.choice(list(ENTITIES.keys())) # Choose a random entity to spawn
        entity_data = ENTITIES[entity] # Get the entity data from the ENTITIES dictionary in constants.py

        fancy_text(f"\nOh no! {entity} appears!")
        player_health -= entity_data["damage"] # Deduct the entity's damage from the player's health
        fancy_text(f"You lost {entity_data['damage']} HP! (Current HP: {player_health})")
        
        # Mark this room as having had an entity spawn so that it doesn't spawn another entity in this room again

        # I would've just made it so that all visited rooms are prevented from spawning an entity, but for some reason it just doesn't work when I try it
        # After a few hours of attempted debugging, I just gave up on it and made a separate set for entity spawned rooms
        # Not too code-efficient but hey, when you need the program to work, you need the program to work
        if "entity_spawned_rooms" not in game_data:
            game_data["entity_spawned_rooms"] = set()
        game_data["entity_spawned_rooms"].add(current_room)
        
        if player_health <= 0: # Death messages
            fancy_text("\nYOU DIED! NOOOOOOOOO 😭")
            fancy_text("Better luck next time... that's all I can say 😢")
            return False
        
        return True # If the entity spawned and the player is still alive, return True
    return True # If no entity spawned, return True

def replay_prompt():
    """The legendary replay option is right here! Handles replay or quit after death or victory"""
    while True: # Ask the player if they want to replay or quit
        choice = input("\nWould you like to (R) replay or (Q) quit? ").strip().lower() # strip removes whitespaces, lower allows lowercase input
        if choice == 'r': # If the player wants to replay the game
            # Reset game state
            global current_room, player_health, inventory, coins, game_data
            current_room = 0
            player_health = 100
            inventory = []
            coins = 0
            game_data = {
                "visited_rooms": set(),
                "looted_rooms": set(),
                "dark_rooms": generate_dark_rooms(),
                "entity_spawned_rooms": set()
            }
            print("\033c", end="") # Clear the console screen
            show_intro() # Show the intro text again
            return # Return to the main game loop
        elif choice == 'q': # If the player wants to quit the game
            fancy_text("\nThanks for playing! Goodbye.")
            exit()
        else: # Invalid choice error handler
            fancy_text("Invalid choice. Please enter R or Q.")

def loot_room():
    """Loot the current room for coins and items."""
    # Keep track of the player's coins, inventory, and health by using global variable
    global coins, inventory, player_health
    
    # Make it so that if you already looted a room, you can't loot it again
    if current_room in game_data["looted_rooms"]:
        fancy_text("You've already looted this room, you can't seem to find anything else.")
        time.sleep(1)
        return ""
    
    # Guaranteed coins
    coins_found = random.randint(2, 5) # Can find between 2 to 5 coins
    coins += coins_found # Add the found coins to the player's total coins
    fancy_text(f"\nFound {coins_found} coins!")
    
    # 35% item chance
    if random.random() <= 0.35:
        # Randomly select an item from the ITEMS dictionary from constants.py
        item = random.choice(list(ITEMS.keys()))
        found = next((i for i in inventory if i["name"] == item), None) # Check if the item is already in the inventory
        if found:
            found["uses"] += 1 # If the item is in the inventory, increment its uses by 1
        else:
            inventory.append({"name": item, "uses": 1}) # Otherwise add the item to the inventory with 1 use
        # Generate description for the item
        fancy_text(f"Among the coins, you discover a {item}! ({ITEMS[item]['description']})")
    
    # 15% Peter the Spider attack chance
    if random.random() <= 0.15:
        damage = random.randint(3, 5) # Random damage between 3 to 5
        player_health -= damage # Deduct the damage from the player's health
        fancy_text(f"\nPeter the Spider jumps out and scratches you! (-{damage} HP)")
        fancy_text(f"He quickly scurries away into the darkness, nowhere to be seen...")
        fancy_text(f"Current HP: {player_health}/100")
    
    # Add the current room to the looted rooms list, so that it can't be looted again
    game_data["looted_rooms"].add(current_room)
    time.sleep(1)
    return ""

def use_item() -> str:
    """Use an item from the player inventory."""
    global player_health, inventory # Keep track of the player's health and inventory by using global variables
    
    # If nothing is in the inventory, show a message and return
    # Because how would you be able to use an item if you don't have any items in your inventory :/
    if not inventory:
        fancy_text("Your inventory is empty!")
        time.sleep(1)
        return ""
    
    # Create a consolidated list of unique items for display
    consolidated_items = {}
    for item in inventory:
        if item["name"] in consolidated_items:
            consolidated_items[item["name"]]["uses"] += item["uses"]
        else:
            consolidated_items[item["name"]] = {"uses": item["uses"], "description": ITEMS[item["name"]]["description"]}
    
    fancy_text("\nAvailable items:") # Display the available items in the inventory
    # Loop through all the items in inventory and print them with their uses and descriptions
    for i, (name, props) in enumerate(consolidated_items.items(), 1):
        fancy_text(f"{i}. {name} x{props['uses']} - {props['description']}")
    
    try:
        choice = int(input("Select item (number) or 0 to cancel: "))
        # If the user inputs 0, cancel the item usage
        if choice == 0:
            return ""
        
        # Get the selected item name from the consolidated list
        selected_name = list(consolidated_items.keys())[choice-1]
        
        # Find the first inventory entry with this name
        selected = next(item for item in inventory if item["name"] == selected_name)
        item_name = selected["name"]
        
        # Handle effects
        if item_name == "Bandage":
            if player_health == 100: # If the player is already at full health, show a message and return
                fancy_text("You are already at full health!")
                return ""
            else:
                player_health = min(100, player_health + 10) # Plus 10 HP for each bandage used
                fancy_text(f"Used Bandage! HP restored to {player_health}/100")
        elif item_name == "Flashlight":
            # If the player is in a dark room, light it up
            if current_room in game_data["dark_rooms"]:
                fancy_text("You light up the room temporarily!")
                game_data["dark_rooms"].remove(current_room) # Un-dark the room
            else:
                # If the player is not in a dark room, show error message
                fancy_text("No need to use this in a lit room!")
                return ""
            
        # The lockpick is currently useless because I wasn't able to implement a locked door event at this stage
        # In later versions they will be very useful, but for now they are just a placeholder
        # The code for the lockpick is only an experiment. I'll see if it works. If it does, it might also go in Sprints 3 and 4

        elif item_name == "Lockpick":
            if random.random() <= 0.5:
                fancy_text("The lock clicks open!")
            else:
                fancy_text("The lockpick broke!")
        
        # Decrement uses after the player uses the item
        selected["uses"] -= 1
        # Remove item title from inventory completely if they have all been used up
        if selected["uses"] <= 0:
            inventory.remove(selected)
            fancy_text(f"{item_name} has been used up!")
            
    except (ValueError, IndexError):
        fancy_text("Invalid selection!") # If the user inputs an invalid number, show an error message
    
    time.sleep(1)
    return ""

# This function will be used every single time the player moves forward or backward.
# Because it displays critical information about the player's current status.
def show_status(): # Show the player's current status, including room number, health, coins, and inventory
    """Display the player's current progress in the game."""
    # The option bar right here
    fancy_text(f"Room: {current_room:04d} | HP: {player_health}/100 | Coins: {coins}")
    # Show the player inventory
    if inventory: # If there are anything in the inventory
        # Group identical items for display
        item_counts = {}
        # Loop through the inventory and count the number of uses for each item
        # This is the inventory display that will show up on the user interface
        # Not to be confused with the one from the use_time function, which is displayed when the player uses the Use Item function
        for item in inventory:
            name = item["name"]
            item_counts[name] = item_counts.get(name, 0) + item["uses"]
        fancy_text("Inventory: " + ", ".join([f"{name} x{count}" for name, count in item_counts.items()]))