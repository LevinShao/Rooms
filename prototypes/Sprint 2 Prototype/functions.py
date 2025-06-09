import time
import random
from constants import * # Import everything from constants.py

# Game state
current_room = 0 # Start at Room 000
player_health = 100 # Start with full health
inventory = [] # A list that stores the player's items (i.e. their inventory)
coins = 0 # A variable that stores the player's coins, which can be used to buy items.

# Note: I have given up trying to create Levin's Shop in this prototype
# It was way too hard to implement, and I felt like introducing it in this prototype would be too early.
# I definitely will find a way to implement it in later versions, but I'm gonna take a rest now.
# Although this would make the coins useless, I'm keeping them here anyways just for experimentation purposes for the system.

# A dictionary that stores the game data, such as visited rooms, looted rooms, and dark rooms
# set() is used to store unique values, which is useful for visited and looted rooms
game_data = {
    "visited_rooms": set(),
    "looted_rooms": set(),
    "dark_rooms": set()
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
    
# In this case, the expected return type of the get_room_description function is a string, hence the "-> str" at the end of the function definition.
def get_room_description() -> str:
    """Randomly picks a room description for a room out of the five above."""
    # Exceptions for special rooms
    if current_room == 0: # Room 000 is the entrance room with a fixed description.
        return "Reception Area: A creaky wooden door behind you."
    elif current_room == 100: # Room 100 is the final "room" with a fixed description. This "room" will lead to the exit.
        return "You stumble into the outside, seeing a massive gate covered in angelic symbols in front of you."
    elif current_room in game_data["dark_rooms"]:
        return get_dark_room_description()
    else: # For every single other room, select a random description from the ROOM_TYPES list.
        # Seed the random generator with room number for consistent descriptions
        random.seed(current_room)
        # First round the room number to 3 digits as a form of convention from the original Doors game, then return the randomly generaated description
        return f"Room {current_room:03d}: {random.choice(ROOM_TYPES)}"

# These two functions below (handle_entity_encounter and weighted_random_choice) were very difficult to implement,
# and either they could somewhat work well, or they could just not work at all. Even I'm not too sure
# I took these as inspirations from several public CLI games on Replit. These functions are experimental... I guess
def handle_entity_encounter():
    """Handle an entity encounter in the current room."""
    global player_health # Keep track of the player's health by using a global variable

    # If the player is in a dark room, increase the chance of an entity encounter
    if current_room in game_data["dark_rooms"]: 
        entity = weighted_random_choice(ENTITIES, 1.5)  # 1.5 means 50% more chance for entity spawning.
    else:
        entity = weighted_random_choice(ENTITIES) # If not in a dark room, use normal entity spawn chances
    
    # Currently I'm gonna make all the entities behave the same way as each other, just because I'm tired as hell and don't want to overcomplicate more things
    # But in the future, I will make them behave accordingly to their own properties, just like in the original Doors game
    # The hiding function will also come in later updates, right now the player will just lose health when encountering an entity

    # Entity attack process
    fancy_text(f"\nOh no! {entity} appears!")
    player_health -= ENTITIES[entity]["health_penalty"]
    fancy_text(f"You lost {ENTITIES[entity]['health_penalty']} HP! (Current HP: {player_health})")
    return player_health > 0  # Return False if player died

def weighted_random_choice(items, weight_mod=1.0):
    """
    This function is EXTREMELY complicated, so I'm going to explain it to the best of my ability using DocStrings
    What this does is that it randomly selects an item from the Items dictionary in constants.py based on their spawn chances
    weight_mod acts as a multiplier for the spawn chances, which can be used to increase or decrease the chance of an item spawning
    counter is used to keep track of the cumulative spawn chances

    Imagine that we currently have these entities:
    - Tralalero Tralala: spawn_chance = 0.15
    - Bombardino Crocodilo: spawn_chance = 0.15
    - Brr Brr Patapim: spawn_chance = 0.10
    - Boneca Ambalabu: spawn_chance = 0.15
    - Tung Tung Tung Sahur: spawn_chance = 0.10

    With default weight_mod (1.0), total weight = 0.15 + 0.15 + 0.10 + 0.15 + 0.10 = 0.65
    The function then generates a random number (using random.uniform) between 0 and 0.65 (let's say 0.32 as an example)

    It checks:
    - Tralalero Tralala (0-0.15): 0.32 not in this range
    - Bombardino Crocodilo (0.15-0.30): 0.32 not in this range
    - Brr Brr Patapim (0.30-0.40): 0.32 is in this range, so the program will select Brr Brr Patapim as the appearing entity
    - Boneca Ambalabu (0.40-0.55): 0.32 not in this range
    - Tung Tung Tung Sahur (0.55-0.65): 0.32 not in this range

    And that's how the function works! It randomly selects an item based on their spawn chances.
    NOTE: This function works for all the dictionaries in constants.py

    This took me the longest time to figure out, and I had to scroll through several websites and forums just to understand how to implement it.
    """
    # Calculate the total weight by summing all individual weights after applying the modifier
    # For each item's properties (v), multiply its spawn_chance by the weight_mod
    total = sum(v["spawn_chance"] * weight_mod for v in items.values())
    r = random.uniform(0, total) # Generate a random number between 0 and the total weight
    counter = 0 # Initialize a counter to keep track of the cumulative spawn chances, and where we are in the weight range.
    for name, props in items.items():
        # If our weight falls within the range of the current item's spawn chance, select it
        if counter + (props["spawn_chance"] * weight_mod) >= r:
            return name
        counter += props["spawn_chance"] * weight_mod # # Otherwise, add this item's weight to our counter and continue
    return random.choice(list(items.keys())) # Fallback just in case something goes wrong, should theoretically never happen but just in case

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
    fancy_text(f"Room: {current_room:03d} | HP: {player_health}/100 | Coins: {coins}")
    if inventory:
        # Group identical items for display
        item_counts = {}
        # Loop through the inventory and count the number of uses for each item
        # This is the inventory display that will show up on the user interface
        # Not to be confused with the one from the use_time function, which is displayed when the player uses the Use Item function
        for item in inventory:
            name = item["name"]
            item_counts[name] = item_counts.get(name, 0) + item["uses"]
        fancy_text("Inventory: " + ", ".join([f"{name} x{count}" for name, count in item_counts.items()]))

# Refresh the console display to make the game look more dynamic
# The simplest function here
def refresh_display():
    """Completely refreshes all game information"""
    print("\033c", end="")  # Clear screen
    show_status()
    fancy_text(get_room_description())