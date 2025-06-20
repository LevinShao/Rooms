# Some of the code here is SO complicated that I literally have to take inspiration by looking at the source code for the original Doors game in Roblox Studio.
# Gotta say, I hope the 3 all-nighters I pulled for this task will be worth it.
# My brain is literally burning right now, I am not joking.
# Also, special thanks to QuackGod on Discord and a few other people for helping me with some sections of this code!

# All of these modules right here are part of the standard Python library
# They do NOT need to be pip installed!
# This means that I don't need to write a requirements.txt file, since there is literally nothing needed for the player to install
# They can literally just download the program, then run it as soon as they import it to VS Code

import time # For time.sleep functions
import random # RNG for entities and obstacles
import msvcrt # Msvcrt is useful for non-blocking input in Windows

# Msvcrt is very useful for my entity functions, since when the player comes across an entity,
# they wouldn't need to press Enter after using the key
# For example, if the player comes across Boneca Ambalabu, they'll just need to press the C key in order to avoid him
# They wouldn't need to press C then enter, thanks to the msvcrt module
# If I didn't use msvcrt, then the player would have to type C then enter, which could be really inefficient
# Since the player is only allowed 3 seconds in order to avoid the entity, otherwise they take damage
# With msvcrt, the p0layer can just press the C key, and it would register as the player input without having to hit enter

# These two modules will be used as an alternative to msvcrt since msvcrt is Windows-only
# These two are used for any other OS other than Windows
import sys
import select

from constants import * # Import everything from constants.py

# The main player class that manages health, inventory, and special room visits
class Player:
    def __init__(self): # Initalize player with default values
        self.health = 100 # Starting health
        # Maximum possible health. This is added so that using the bandage can't exceed the maximum health
        # For example, if the player has 98 HP and uses a bandage which heals 10 HP, the player can only heal 2 HP back to 100, not exceeding it.
        self.max_health = 100
        self.inventory = [] # List of items in player inventory
        self.coins = 0 # Starting coin amount
        self.special_room_visited = False # Special room tracker that tracks if players has visited any special rooms (such as Room 051)
        # Mark false because the player hasn't visited any special rooms on start        

    # --------------------- ITEM MANAGEMENT -----------------------------

    def add_item(self, item_name, uses=1): # Add item to inventory
        # Check if item already exists in inventory
        existing_item = next((item for item in self.inventory if item["name"] == item_name), None) # Loop through inventory to find item by their name
        if existing_item:
            # If items exists, increase its uses. For example, if the player collected a bandage and they already have two, then make it three uses.
            existing_item["uses"] += uses
        else:
            self.inventory.append({"name": item_name, "uses": uses}) # Otherwise just add it to their inventory with name and uses displayed
    
    def use_item(self, item_name): # Use the item
        item = next((item for item in self.inventory if item["name"] == item_name), None) # Once again, loop through the inventory to find the item by their name
        if item:
            item["uses"] -= 1 # Minus a use from the item
            if item["uses"] <= 0: # If the item has no uses left, remove it from the inventory
                self.inventory.remove(item)
            return True
        return False # If the item doesn't even exist, return False
    
    def has_item(self, item_name):
        return any(item["name"] == item_name for item in self.inventory)
    
    def get_consolidated_inventory(self): # Consolidate the inventory to show items with their total uses
        consolidated = {} # Create an empty dictionary to store consolidated items
        for item in self.inventory:
            if item["name"] in consolidated: # If the item already exists in the consolidated dictionary, add its uses to the existing entry
                consolidated[item["name"]]["uses"] += item["uses"]
            else:
                # Otherwise, add the item to the consolidated dictionary with its uses and description
                consolidated[item["name"]] = {
                    "uses": item["uses"], 
                    "description": ITEMS[item["name"]]["description"]
                }
        return consolidated # Return the consolidated inventory dictionary to the player
    
    def take_damage(self, amount):  # Take damage from an entity, obstacle or event
        self.health -= amount
        return self.health > 0
    
    def heal(self, amount): # Heal the player by a certain amount
        self.health = min(self.max_health, self.health + amount) # Make sure the health doesn't exceed the maximum health
    
    def full_heal(self): # Full heal mechanic for the Starlight Jug item which heals all player's health
        self.health = self.max_health

class Room:
    def __init__(self, number, persistent_room_types, game_data):  # Add game_data parameter
        self.number = number # Room number
        self.visited = False # Mark visited rooms as false
        self.looted = False # Mark looted rooms as false
        self.is_dark = False # Mark dark rooms as false
        self.has_entity = False # Mark rooms with entity false
        self.has_obstacle = False # Mark rooms with obstacle false
        self.entity = None # Mark entity as None since they don't spawn at start
        self.obstacle = None # Mark obstacle as None for the same reason
        self.is_special = number in SPECIAL_ROOMS # Check if the room is a special room
        self.is_puzzle = number in PUZZLES # Check if the room is a puzzle room
        self.persistent_description = persistent_room_types[number] # This function right here will generate persistent descriptions

        # The generate_room_description function used to be able to generate persistent room descriptions in Sprint 1 and 2
        # But since I added classes in Sprint 3, there was an issue with the persistent descriptions not being generated correctly
        # I think this was due to the fact that the persistent descriptions in the generate_room_description function were generated before the game_data was passed to the Room class
        # And the easiest solution for this, as far as I can tell from all the research, is to pass the game_data to the Room class by adding a game_data parameter to the __init__ function, like how I did it here.

        self.game_data = game_data  # Store game_data reference
        self.has_duplicated_rooms = False # The duplicated rooms event tracker. 
        # Duplicated rooms wasn't added as an obstacle because it behaves differently than other obstacles
    
    def spawn_entity(self):
        """
        Spawns an entity in the current room

        If the room is dark, there is a 60% chance to spawn a dark-favored entity.
        Otherwise, a random entity is chosen from the available entities.
        Marks the room as having an entity and records the spawn in game data.

        Will not spawn obstacles in special rooms, puzzle rooms or rooms 000 and 100.
        This function will be called in the enter_room function. When it lands on the random chance,
        this function will be used to mark has_obstacles to True
        then, after it's marked as True, move_forward will call the handle_duplicated_rooms function
        which will then do all the event-related stuff, such as sending the display to the player
        """
        self.has_entity = True # Mark has_entity as true
        if self.is_dark: # If the room is a dark room
            dark_favored = ["Boneca Ambalabu", "Tung Tung Tung Sahur"] # Boneca Ambalabu and Tung Sahur will be set as dark favored entities
            # 60% chance for dark favored entity, otherwise choose an entity from the entity list that is not dark favored
            self.entity = random.choice(dark_favored if random.random() < 0.6 else [e for e in ENTITIES if e not in dark_favored])
        else:
            self.entity = random.choice(list(ENTITIES.keys())) # For normal, lit rooms, choose whatever entity
        self.game_data["entity_spawned_rooms"].add(self.number) # Add room number as having had an entity

    def spawn_obstacle(self):
        """
        Main function for obstacle spawning
        
        Will not spawn obstacles in special rooms, puzzle rooms or rooms 000 and 100.
        This function will be called in the enter_room function. When it lands on the random chance,
        this function will be used to mark has_obstacles to True
        then, after it's marked as True, move_forward will call the handle_duplicated_rooms function
        which will then do all the event-related stuff, such as sending the display to the player
        """
        if (self.number in (0, 100) or self.is_special or self.is_puzzle):
            return False # Return false for these rooms
        # Otherwise mark as true, and generate a random obstacle
        self.has_obstacle = True
        self.obstacle = random.choice(list(OBSTACLES.keys()))
        # Add current room to obstacle-spawned rooms in game data
        self.game_data["obstacle_spawned_rooms"].add(self.number)

    def spawn_duplicated_rooms_event(self):
        """
        Main function controlling the duplicated rooms event
        
        This function will be called in the enter_room function. When it lands on the random chance,
        this function will be used to mark has_duplicated_rooms to True
        then, after it's marked as True, move_forward will call the handle_duplicated_rooms function
        which will then do all the event-related stuff, such as sending the display to the player
        """
        if (self.is_special or self.is_puzzle or self.number in (0, 100)):
            return False # Once again we wanna return false for any of the rooms listed above
        self.has_duplicated_rooms = True
        self.game_data["event_spawned_rooms"].add(self.number) # Add current room to event spawned list

    @staticmethod
    # A static method is a method that belongs to a class but does not operate on instances of that class. 
    # It does not require a reference to the instance (self) or the class (cls) as its first parameter. 
    def get_room_description(self, game):
        """Generate room types that will persist for the entire game"""
        room_types = {}
        for room_number in range(101):
            if room_number == 0: # Room 0000
                room_types[0] = "Reception Area: A creaky wooden door behind you."
            elif room_number == 100: # Room 0100
                room_types[100] = "You stumble into the outside, seeing a massive gate covered in angelic symbols in front of you."
            elif room_number in SPECIAL_ROOMS: # Special room
                room_types[room_number] = SPECIAL_ROOMS[room_number]["description"]
            elif room_number in PUZZLES: # Puzzle room
                room_types[room_number] = f"Room {room_number:04d}: {PUZZLES[room_number]['description']}"
            elif room_number in self.game_data["dark_rooms"]: # Dark room
                room_types[room_number] = f"⚠️  DARK ROOM: {random.choice(DARK_ROOM_DESCRIPTIONS)}"
            elif room_number == game.starlight_room: # Starlight room
                room_types[room_number] = f"💫  STARLIGHT ROOM: This room glows with golden light. Maybe a good idea to loot?"
            else: # Any other normal room
                room_types[room_number] = f"Room {room_number:04d}: {random.choice(ROOM_TYPES)}"
        return room_types
        # Also, round every room number to 4 d.p. as a convention to the original Doors game
    
    def handle_duplicated_rooms(self, game):
        """
        The main function for the duplicated room event.
        
        This code was pulled and slightly modified from the original source code for a 
        collaborative sandbox game me and some other friends made around 2 years ago
        """
        # The real next room is supposed to be the one after the current room
        # So that means it should be the current room + 1
        # If the player comes across this event at Room 045, the next room should be 046, shouldn't it?
        real_next_room = self.number + 1
        
        # Generate potential fake room numbers that could be shown to player

        # Criteria for fake rooms:
        # - Must be within 1-100 range
        # - Can't be special/puzzle rooms
        # - Can't be the actual next room
        # - Initially looks 3 rooms ahead (n+1 to n+3)
        possible_fakes = [
            n for n in range(self.number + 1, self.number + 4) 
            if n <= 100 and 
            n not in SPECIAL_ROOMS and 
            n not in PUZZLES and 
            n != real_next_room
        ]
        
        # If we don't have enough forward rooms, allow some backward options
        if len(possible_fakes) < 2:
            possible_fakes += [
                n for n in range(self.number - 2, self.number) 
                if n > 0 and 
                n not in SPECIAL_ROOMS and 
                n not in PUZZLES and 
                n != real_next_room
            ]
        
        # Make sure we have exactly 2 fake rooms
        fake_rooms = random.sample(possible_fakes, min(2, len(possible_fakes)))
        
        # Create door options (1 real, 2 fake)
        doors = [real_next_room] + fake_rooms
        random.shuffle(doors) # Random module's shuffle function is EXTREMELY useful here!
        # Without shuffle I don't know how else I'm supposed to have created this function
        
        game.fancy_text("\nThe room number is obscured... something feels wrong here.")
        game.fancy_text("You see three doors ahead:")
        
        # Display ALL the door options
        for i, door in enumerate(doors, 1):
            game.fancy_text(f"{i}. Room {door:04d}") # 4 decimal places as usual
        
        # Main choice loop - repeats until valid choice or player dies
        while True:
            try:
                # The code right here is a bit complex but since I kind of just copied them from an old game I'll do whatever
                choice = int(input("Choose a door (1-3): "))
                if 1 <= choice <= 3:
                    selected_room = doors[choice-1] # Convert to a 0-based index.
                    
                    if selected_room == real_next_room: # Success scenario
                        game.fancy_text("You chose the correct door!")
                        self.has_duplicated_rooms = False
                        return selected_room  # Return the real room number
                    else: # Handle wrong choice
                        # Apply damage while checking for death
                        game.fancy_text(DUPLICATED_ROOMS_EVENT["consequence"]["message"] + " You lost 10 HP!")
                        if not game.player.take_damage(DUPLICATED_ROOMS_EVENT["consequence"]["damage"]):
                            return None  # Player died
                        game.fancy_text(f"Current HP: {game.player.health}/{game.player.max_health}")
                        
                        # Show doors again after wrong choice
                        game.fancy_text("\nThe three doors remain:")
                        for i, door in enumerate(doors, 1):
                            game.fancy_text(f"{i}. Room {door:04d}")
                else: # Error handlers
                    game.fancy_text("Please enter a number between 1 and 3")
            except ValueError:
                game.fancy_text("Invalid input! Please enter a number")

class Game:
    """
    The main game class. 
    
    This is the most important class since it's in control of everything in the game's nature.
    """
    def __init__(self): # Initialize everything
        self.player = Player()
        self.current_room = 0
        self.game_data = { # ALL THE MOST IMPORTANT GAME DATA IS STORED HERE
            "visited_rooms": set(),
            "looted_rooms": set(),
            "dark_rooms": set(),
            "completed_puzzles": set(),
            "entity_spawned_rooms": set(),
            "obstacle_spawned_rooms": set(),
            "event_spawned_rooms": set()
        }
        
        # Generate starlight room FIRST
        self.starlight_room = self.generate_starlight_room()
        
        # Then generate dark rooms
        self.generate_dark_rooms()
        
        # Then create rooms with this information
        self.persistent_room_types = Room.get_room_description(self, self)
        self.rooms = {i: Room(i, self.persistent_room_types, self.game_data) for i in range(101)}
        self.setup_special_rooms()
    
    def setup_special_rooms(self): # Configuration function for special rooms
        # For every room number in the special rooms list, make sure they aren't dark, doesn't have an entity, obstacle or room event
        for room_num in SPECIAL_ROOMS:
            room = self.rooms[room_num]
            room.is_dark = False
            room.has_entity = False
            room.has_obstacle = False
            room.has_duplicated_rooms = False

    def generate_dark_rooms(self):
        possible_rooms = list(range(1, 100)) # Possible rooms range from 001 to 100
        
        # Remove special rooms and puzzle rooms from possible dark rooms
        excluded_rooms = set(SPECIAL_ROOMS.keys()).union(set(PUZZLES.keys()))
        possible_rooms = [r for r in possible_rooms if r not in excluded_rooms]
        
        # Select dark rooms
        dark_rooms = set(random.sample(possible_rooms, 10))
        
        # Make some dark rooms consecutive
        for room in list(dark_rooms):
            if random.random() < 0.3 and room < 99:  # 30% chance to have consecutive dark rooms
                new_room = room + 1 # Consecutive function
                if new_room not in excluded_rooms:
                    dark_rooms.add(new_room)
        
        self.game_data["dark_rooms"] = dark_rooms  # Store the dark rooms in game_data
    
    def generate_starlight_room(self):
        """Generate a random room for the Starlight Jug"""
        # Rooms where Starlight Jug cannot appear (special rooms and puzzle rooms)
        excluded_rooms = {0, 25, 49, 50, 51, 52, 75, 99, 100}
        # All possible rooms between 1-99 that aren't excluded
        possible_rooms = [r for r in range(1, 100) if r not in excluded_rooms]
        # Randomly select one room from possible candidates
        return random.choice(possible_rooms)
    
    def move_forward(self):
        """Basic function for moving forward"""
        room = self.rooms[self.current_room]
        
        if room.has_duplicated_rooms: # If the room has the duplicated rooms event
            result = room.handle_duplicated_rooms(self) # Call the handle dupe rooms function to handle dupe rooms
            if result is None:  # Player died
                return False
            self.current_room = result # Dupe rooms process
            self.game_data["visited_rooms"].add(self.current_room) # Add room into visited rooms list
            self.fancy_text(f"Moved forward to Room {self.current_room:04d}.") # 4 d.p.
            time.sleep(0.5) # Short pause
            self.enter_room() # Enter new room by using enter room function
            return True
        
        if self.current_room < 100: # If the room is just a normal room
            next_room = self.current_room + 1 # Progression by adding 1. For example, Room 0045 --> Room 0046
            self.current_room = next_room
            self.game_data["visited_rooms"].add(self.current_room) # Mark visited
            self.fancy_text(f"Moved forward to Room {self.current_room:04d}.")
            time.sleep(0.5)
            self.enter_room()
            return True
        else: # IF THE PLAYER BEATS THE GAME
            outro_text = (
                "\nYou've reached the exit beyond Room 100!\n"
                "Congratulations! You've beaten the game!\n\n"
                "Thanks for playing!"
            )
            self.fancy_text(outro_text)
            self.replay_prompt()
            return False
    
    def move_backward(self):
        """Basic function for moving backward"""
        if self.current_room > 0: 
            # If in a room that's not 0 then decrease room number by 1 every time player goes back
            self.current_room -= 1
            self.fancy_text(f"Moved backward to Room {self.current_room:04d}.")
            time.sleep(0.5)
            self.enter_room()
            return True
        else: # For Room 0000
            self.fancy_text("The door behind you is blocked. You can't turn back now.")
            time.sleep(0.5)
            return False # Mark as false because player won't be allowed to move back
    
    def enter_room(self):
        """A very important function to handle stuff when player enters new room"""
        # Mark room as visited as soon as player enters
        room = self.rooms[self.current_room]
        room.visited = True
        self.game_data["visited_rooms"].add(self.current_room)
        
        # Set room darkness based on game_data
        room.is_dark = self.current_room in self.game_data["dark_rooms"]
        
        # Handle special room effects
        if self.current_room in SPECIAL_ROOMS:
            self.handle_special_room()
            return
        
        # Only spawn events/entities/obstacles if first visit
        if (self.current_room not in self.game_data["entity_spawned_rooms"] and 
            self.current_room not in self.game_data["obstacle_spawned_rooms"] and
            self.current_room not in self.game_data["event_spawned_rooms"] and
            not room.is_special and not room.is_puzzle):
            
            spawn_roll = random.random() # Will decide if an entity/obstacle/room event will spawn

            if room.is_dark: # Dark rooms
                if spawn_roll < 0.60:
                    # Try different spawns with adjusted probabilities
                    spawn_roll2 = random.random()
                    if spawn_roll2 < 0.10:  # 10% duplicated rooms
                        room.spawn_duplicated_rooms_event()
                    elif spawn_roll2 < 0.80:  # 70% entities (10-80)
                        room.spawn_entity()
                    else:  # 20% obstacles (80-100)
                        room.spawn_obstacle()
            elif self.current_room >= 90: # Rooms after 0089
                if spawn_roll < 0.50:
                    spawn_roll2B = random.random()
                    if spawn_roll2B < 0.10:  # 10% duplicated rooms
                        room.spawn_duplicated_rooms_event()
                    elif spawn_roll2B < 0.70:  # 60% entities (10-70)
                        room.spawn_entity()
                    else:  # 30% obstacles (70-100)
                        room.spawn_obstacle()
            else: # 0001-0089 that's not a dark room, puzzle or special rooms
                if spawn_roll < 0.30:
                    spawn_roll2C = random.random()
                    if spawn_roll2C < 0.30:  # 30% duplicated rooms
                        room.spawn_duplicated_rooms_event()
                    elif spawn_roll2C < 0.70:  # 40% entities (30-70)
                        room.spawn_entity()
                    else:  # 30% obstacles (70-100)
                        room.spawn_obstacle()
    
    def handle_special_room(self):
        """Main function to handle special rooms"""
        room_num = self.current_room
        room_data = SPECIAL_ROOMS.get(room_num, {}) # Fetch special rooms info from the list
        
        if room_num == 49:  # Preparation room
            self.fancy_text("\nThis is a safe room to prepare for the upcoming puzzle.")
        
        elif room_num == 51:  # Throne room
            if not self.player.special_room_visited and random.random() < room_data.get("special_item_chance", 0): # Find a rare item in the throne room
                self.fancy_text("\nYou found a rare item in the throne room!")
                self.player.add_item(random.choice(list(ITEMS.keys()))) # Plot twist: the item is not rare at all (it's literally just a random common item)
                self.player.special_room_visited = True # Mark special rooms as true
        
        elif room_num == 52:  # Levin's Shop
            self.visit_shop()
        
        elif room_num == 99:  # Final preparation room
            heal_amount = room_data.get("heal_amount", 0) # Fetch the heal amount from the room data
            self.player.heal(heal_amount) # Heal fuunction
            self.fancy_text(f"\nYou feel refreshed! +{heal_amount} HP") # Immediately heal player up when they reach room 0099 as a reward for getting that far
    
    def visit_shop(self):
        """
        Function to handle Levin's Shop
        
        This code was ripped off from the economy game function of a Discord bot I made in Python a few years prior.
        """
        self.fancy_text("\nWelcome to Levin's Shop!")
        self.fancy_text(f"Your coins: {self.player.coins}") # Retrieve coin amount from player class
        
        shop_items = SPECIAL_ROOMS[52]["shop_items"]
        while True:
            self.fancy_text("\nAvailable items:") # Display all items
            for i, (item, price) in enumerate(shop_items.items(), 1): 
                # Loop through each available item in the shop
                # Display their item name and price as well as description
                self.fancy_text(f"{i}. {item} - {price} coins ({ITEMS[item]['description']})")
            
            self.fancy_text("0. Exit shop") # Exit
            
            try:
                choice = int(input("\nWhat would you like to buy? "))
                if choice == 0:
                    break # Exit function
                
                # Convert the shop's item keys to a list and using the player's choice (minus one, since lists are zero-indexed) to get the correct item.
                item_name = list(shop_items.keys())[choice-1]
                price = shop_items[item_name]
                
                # If the player has enough coins, the item's price is subtracted from their coin total, the item is added to their inventory
                if self.player.coins >= price:
                    self.player.coins -= price
                    self.player.add_item(item_name)
                    self.fancy_text(f"You bought {item_name}!")
                else:
                    self.fancy_text("Not enough coins!") # Not enough coins
            except (ValueError, IndexError):
                self.fancy_text("Invalid choice!") # Error handler for invalid inputs

    def handle_entity_encounter(self):
        """Main function for handling entity encounters"""
        room = self.rooms[self.current_room]
        if not room.has_entity:
            return True # Return true if room has entity
            
        # Entity variables
        entity_name = room.entity
        entity_data = ENTITIES[entity_name]
        interaction = entity_data["interaction"]
        
        self.fancy_text(f"\nOh no! {entity_name} appears!")
        self.fancy_text(interaction["prompt"])
        
        # Special case for Tung Sahur (timing-based)
        if entity_name == "Tung Tung Tung Sahur":
            start_time = time.time()
            end_time = start_time + 5  # 5 second challenge
            
            try:
                # Windows version using msvcrt
                while time.time() < end_time:
                    if msvcrt.kbhit():  # If any key was pressed
                        _ = msvcrt.getch()  # Clear the keypress
                        self.fancy_text(interaction["fail_msg"])
                        return self.resolve_entity_damage(entity_data)
                    
                # If we get here, no keys were pressed
                self.fancy_text(interaction["success_msg"])
                room.has_entity = False
                return True
            except ImportError:

                # Msvcrt is a Windows-based module. Computers running MacOS or Linux would not be able to use Msvcrt, which could result in import errors
                # So this is directed to specifically computers running these OS systems, since they wouldn't be able to use Msvcrt unless they're on Windows
                # In this case, we will use sys stdin as a workaround to this issue
                # The following code works basically the same as to the code above, just modified to fit sys-stdin into the code.

                # Unix version using sys and select
                while time.time() < end_time:
                    if select.select([sys.stdin], [], [], 0)[0]: # this code was kind of copied from Stack Overflow but anyways
                        _ = sys.stdin.read(1)  # Clear the keypress
                        self.fancy_text(interaction["fail_msg"])
                        return self.resolve_entity_damage(entity_data)
                    
                # If we get here, no keys were pressed
                self.fancy_text(interaction["success_msg"])
                room.has_entity = False
                return True
        
        # NOW FOR ANY ENTITY THAT IS NOT TUNG SAHUR

        # Set time limit for response (3 seconds)
        self.fancy_text("\nYou have 3 seconds to respond!")
        start_time = time.time()

        # The following code is learnt and written from YouTube tutorials
        
        try:
            # For Windows
            end_time = start_time + 3
            while time.time() < end_time:
                if msvcrt.kbhit():  # Check if key was pressed
                    user_input = msvcrt.getch().decode().lower()
                    if user_input == interaction["success_key"]:
                        self.fancy_text(interaction["success_msg"])
                        room.has_entity = False
                        return True
                    else:
                        break  # Wrong key pressed
            # Time ran out or wrong key
            self.fancy_text("\nTime's up or wrong key!")
            self.fancy_text(interaction["fail_msg"])
            return self.resolve_entity_damage(entity_data)
        except ImportError:
            # Unix/non-Windows OS (sys and select instead of msvcrt)
            end_time = start_time + 3
            while time.time() < end_time:
                if select.select([sys.stdin], [], [], 0)[0]: # Copied off internet my bad
                    user_input = sys.stdin.read(1).lower()
                    if user_input == interaction["success_key"]:
                        self.fancy_text(interaction["success_msg"])
                        room.has_entity = False
                        return True
                    else:
                        break  # Wrong key pressed
            # Time ran out or wrong key
            self.fancy_text("\nTime's up or wrong key!")
            self.fancy_text(interaction["fail_msg"])
            return self.resolve_entity_damage(entity_data) # Resolve entity damage
    
    def resolve_entity_damage(self, entity_data):
        """Resolve entity damage with this function"""
        damage = entity_data["damage"] # Fetch damage
        self.player.health -= damage # Deduct damage from player HP
        self.fancy_text(f"You lost {damage} HP! (Current HP: {self.player.health})")
        
        if self.player.health <= 0:
            return False # If health less than 0, just die.
        return True # Otherwise keep going
    
    def handle_obstacle(self):
        """
        Handles obstacle encounters in the current room.
        Presents obstacle description and available options to player,
        processes their choice, and resolves the outcome.
        """
        
        # Get reference to current room object
        room = self.rooms[self.current_room]
        
        # Early return if no obstacle exists in this room
        if not room.has_obstacle:
            return True  # No obstacle to handle
        
        # Get obstacle details from constants
        obstacle_name = room.obstacle
        obstacle_data = OBSTACLES[obstacle_name]

        # Display obstacle description to player
        self.fancy_text(f"\n{obstacle_data['description']}")
        
        # Main interaction loop - continues until obstacle is resolved
        while True:  
            # Get all available options for this obstacle
            options = list(obstacle_data["options"].items())

            # Display each option with numbered choices (starting at 1)
            for i, (option, _) in enumerate(options, 1):
                self.fancy_text(f"{i}. {option}")

            try:
                # Get player's choice (convert to 0-based index)
                choice = int(input("\nChoose an option: ")) - 1
                
                # Validate choice is within available options range
                if 0 <= choice < len(options):
                    # Get details of selected option
                    option_name, outcome = options[choice]
                    
                    # Resolve the outcome of chosen option
                    success = self.resolve_obstacle_outcome(option_name, outcome)

                    if success:
                        # Clear obstacle flag if successfully resolved
                        room.has_obstacle = False
                        return True  # Obstacle cleared
        
                    # If not successful, loop continues to retry
                else:
                    # Handle out-of-range number input
                    self.fancy_text("Invalid choice! Please pick a valid option.\n")
                    
            except ValueError:
                # Handle non-numeric input
                self.fancy_text("Please enter a number!\n")
    
    def resolve_obstacle_outcome(self, option_name, outcome):
        # Check for item requirement first
        # This part is specifically for lockpicks against locked-door obstacle
        if "item_required" in outcome:
            if not self.player.has_item(outcome["item_required"]):
                self.fancy_text(f"You need a {outcome['item_required']}!")
                return False
            
            self.player.use_item(outcome["item_required"])
        
        # Handle success chance
        if "success_chance" in outcome:
            if random.random() <= outcome["success_chance"]:
                self.fancy_text(outcome["success"])
                
                # Special case for finding key
                # Not up to my expectations for this part but had to go like this because I was running out of time
                # And this was the easiest to code as well
                if option_name == "Search for key" and outcome["success"] == "You found a key!":
                    self.player.add_item("Key")
                return True
            else:
                # Fail scenario
                self.fancy_text(outcome["fail"])
                if "damage" in outcome:
                    return self.player.take_damage(outcome["damage"]) # Take damage
                return True
        
        # Handle time cost outcomes
        if "time_cost" in outcome:
            self.fancy_text(outcome["time_cost"]) # Another fail scenario right here
            if "coin_loss" in outcome:
                loss = random.randint(*outcome["coin_loss"]) # Lose some coins as the fail scenario
                self.player.coins = max(0, self.player.coins - loss) # Player's coins after coin loss cannot go below 0
                self.fancy_text(f"Lost {loss} coins!")
        
        # Handle damage from actions
        if "damage" in outcome:
            return self.player.take_damage(outcome["damage"])
        
        return True
    
    def loot_room(self):
        """Loot room function. Part of the user interface and is very important"""
        room = self.rooms[self.current_room]
        if room.looted: # If room is already looted:
            self.fancy_text("You've already looted this room. You can't seem to find anything else.")
            time.sleep(0.5)
            return
            
        # Check for Starlight Jug in special room
        if self.current_room == self.starlight_room and not self.player.has_item("Starlight Jug"):
            self.fancy_text("\nAmong the items, you find the legendary Starlight Jug!")
            time.sleep(0.5)
            self.player.add_item("Starlight Jug") # Add Jug to inventory
            room.looted = True # Set looted to true
            return
        
        # Guaranteed coins
        coins_found = random.randint(2, 5)
        self.player.coins += coins_found # Add 2-5 coins to inventory
        self.fancy_text(f"\nFound {coins_found} coins!")
        
        # Determine if player gets an item or encounters Peter (mutually exclusive)
        outcome = random.random()
        
        if outcome <= 0.35:  # 35% chance for item
            # Random item
            item = random.choice(list(ITEMS.keys()))
            # Don't give Starlight Jug as random loot
            while item == "Starlight Jug":
                item = random.choice(list(ITEMS.keys()))
                
            # Add the loot into the player inventory
            self.player.add_item(item)
            self.fancy_text(f"Among the coins, you discover a {item}! ({ITEMS[item]['description']})")
        
        elif outcome > 0.85:  # 15% chance for Peter the Spider to appear and attack
            damage = random.randint(3, 5) # Random 3-5 damage
            self.player.health -= damage # Deal damage
            self.fancy_text(f"\nPeter the Spider jumps out and scratches you! (-{damage} HP)")
            self.fancy_text(f"He quickly scurries away into the darkness...")
            self.fancy_text(f"Current HP: {self.player.health}/100")
        
        room.looted = True # Set room looted to true
        time.sleep(0.5)
        self.game_data["looted_rooms"].add(self.current_room) # Add the current room to looted room

    def use_item(self):
        """Main use item function. Part of user interface and very important"""
        if not self.player.inventory: # If nothing is in inventory
            self.fancy_text("Your inventory is empty!")
            time.sleep(0.5)
            return
            
        inventory = self.player.get_consolidated_inventory() # Fetch the player's consolidated inventory
        self.fancy_text("\nAvailable items:")
        # Loop through the consolidated inventory using enumerate, which provides both an index (starting from 1) and the item data. 
        # For each item, print a line showing the item's number in the list, its name, the total number of uses as well as description
        for i, (name, props) in enumerate(inventory.items(), 1):
            self.fancy_text(f"{i}. {name} x{props['uses']} - {props['description']}")
        
        try:
            choice = int(input("\nSelect item (number) or 0 to cancel: "))
            if choice == 0:
                return # 0 to cance;
                
            item_name = list(inventory.keys())[choice-1] # Previously explained
            item_data = ITEMS[item_name]
            
            # Handle item effects
            if item_data["effect"] == "heal":
                if self.player.health == self.player.max_health: # Cannot heal if player at max health
                    self.fancy_text("You're already at full health!")
                    time.sleep(0.5)
                    return
                
                self.player.heal(item_data["amount"]) # Otherwise heal specified amount
                self.player.use_item(item_name)
                self.fancy_text(f"Used {item_name}! HP restored to {self.player.health}/100")
            
            elif item_data["effect"] == "full_heal": # For Starlight Jug, which is used to fully heal
                self.player.full_heal()
                self.player.use_item(item_name)
                self.fancy_text(f"Used {item_name}! HP fully restored to {self.player.health}/100")
            
            elif item_data["effect"] == "light_room": # Flashlight item
                room = self.rooms[self.current_room]
                if room.is_dark:
                    self.fancy_text("You light up the room!")
                    room.is_dark = False # Mark dark room as false since it's lit now
                    # Remove from dark rooms set if it exists there
                    if self.current_room in self.game_data["dark_rooms"]:
                        self.game_data["dark_rooms"].remove(self.current_room) # Remove current room from dark rooms
                    # Generate new normal room description
                    self.player.use_item(item_name)
                    # Redisplay room info
                    self.show_status()
                    self.fancy_text(f"Room {self.current_room:04d}: {random.choice(ROOM_TYPES)}")
                else:
                    self.fancy_text("No need to use this in a lit room!") # Don't use in lit rooms
            
            elif item_data["effect"] in ("unlock", "open_door"):
                self.fancy_text(f"You can use {item_name} when facing a locked door!") # Lockpicks
            
            else:
                self.fancy_text(f"Used {item_name}!")
                self.player.use_item(item_name)
                
        except (ValueError, IndexError):
            self.fancy_text("Invalid selection!") # Error handler

        time.sleep(0.5)
    
    def attempt_puzzle(self, room_num):
        """Main function for puzzle rooms"""
        puzzle = PUZZLES[room_num] # Fetch all puzzle rooms (0025, 0050, 0075, 0100)
        self.fancy_text(puzzle["description"])
        
        if room_num == 25:  # Lever puzzle
            while True:
                choice = input("\nWhich lever will you pull? (1-5) or H for hint: ").strip().lower()
                
                try:
                    choice_int = int(choice)
                    if 1 <= choice_int <= 5:
                        if choice_int == puzzle["solution"]:
                            # Right choice
                            self.fancy_text("The path ahead opens!")
                            self.game_data["completed_puzzles"].add(room_num)
                            return True  # Puzzle solved
                        else:
                            # Wrong choice
                            # 50% chance to damage player, 50% chance to do nothing
                            RNG = random.random()
                            if RNG < 0.50:
                                self.fancy_text("Nothing happens. Try again.")
                            else:
                                self.player.health -= 5
                                self.fancy_text("\nThe lever activates a trap, damaging you for 5 HP!")
                                self.fancy_text(f"Current HP: {self.player.health}/100")
                                
                                # Check for death
                                if self.player.health <= 0:
                                    self.fancy_text("\nYou've run out of health!")
                                    return False  # Player died
                    else:
                        self.fancy_text("Please enter a number between 1-5!") # Error handlers
                except ValueError:
                    self.fancy_text("Please enter a number between 1-5 or H for hint!") # Same with this one
        
        elif room_num == 50:  # Riddle at room 50
            while True:
                answer = input("Your answer (or H for hint): ").strip().lower()
                if answer == 'h':
                    self.fancy_text(f"Hint: {puzzle['hint']}")
                    continue
                
                if answer == puzzle["solution"]:
                    self.fancy_text("Correct! The way forward is clear.")
                    time.sleep(0.5)
                    self.game_data["completed_puzzles"].add(room_num)
                    return True
                else:
                    self.fancy_text("Incorrect. Try again.")
        
        elif room_num == 75:  # Pressure plates at room 75
            while True:
                self.fancy_text("Enter the sequence (e.g., '2 4 1 3') or H for hint: ")
                choice = input().strip().lower()
                if choice == 'h':
                    self.fancy_text(f"Hint: {puzzle['hint']}")
                    continue
                
                try:
                    sequence = list(map(int, choice.split())) # Arange the pressure plates into a sequence using list
                    if sequence == puzzle["solution"]:
                        self.fancy_text("The plates click into place!")
                        time.sleep(0.5)
                        self.game_data["completed_puzzles"].add(room_num)
                        return True
                    else:
                        self.fancy_text("Nothing happens. Try again.")
                except ValueError:
                    self.fancy_text("Please enter numbers separated by spaces!")
        
        elif room_num == 100:  # Final puzzle before players beat game
            while True:
                self.fancy_text("Your answer (or H for hint): ")
                answer = input().strip().lower()
                if answer.lower() == 'h':
                    self.fancy_text(f"Hint: {puzzle['hint']}")
                    continue
                
                try:
                    if int(answer) == puzzle["solution"]:
                        # Special handling for final puzzle
                        self.game_data["completed_puzzles"].add(room_num)
                        self.current_room = 100  # Ensure we're at room 100
                        self.move_forward()  # This will handle the victory outro
                        return True
                    else:
                        self.fancy_text("The gate remains sealed. Try again.")
                except ValueError:
                    self.fancy_text("Please enter a number!")
    
    def show_status(self):
        """Main function to handle status display. Part of the UI too"""
        room = self.rooms[self.current_room]
        # Duplicated rooms will show "Room ????", normal rooms show normal room numbers, e.g. "Room 0053"
        room_display = "????" if room.has_duplicated_rooms else f"{self.current_room:04d}" 
        # Status bar that's displayed to the user throughout the game. Very important!
        self.fancy_text(f"Room: {room_display} | HP: {self.player.health}/{self.player.max_health} | Coins: {self.player.coins}") 
        if self.player.inventory:
            # Display inventory
            inventory = self.player.get_consolidated_inventory()
            # Construct a string that lists each item and its quantity in the format "ItemName xUses" (for example, "Potion x2")
            # This is done using a list comprehension that iterates over the consolidated inventory's items and formats each entry accordingly
            self.fancy_text("Inventory: " + ", ".join([f"{name} x{props['uses']}" for name, props in inventory.items()]))
    
    def show_intro(self):
        try:
            with open("data/intro.md", "r", encoding='utf-8') as f: # read intro from intro.md
                intro_text = f.read() # file handling skills that we learnt in class came in clutch for this one
                self.fancy_text(intro_text)
                
            while True:
                choice = input("\nPress Enter to begin your nightmare... (or enter H for help / Q to surrender) > ").strip().lower()
                if choice == '':
                    return  # Start the game
                elif choice == 'h':
                    self.show_help() # HELPPPPP
                    return
                elif choice == 'q':
                    self.fancy_text("\nThanks for checking out the game! Goodbye.") # Goodbye :(
                    exit()
                else:
                    self.fancy_text("Invalid choice. Please press Enter, H, or Q.") # Invalid choice

        except FileNotFoundError: # Special FileNotFoundError exception just in case if somehow intro.md is missing
            # WHICH SHOULD NEVER HAPPEN IN THEORY, BUT I'M JUST PUTTING IT HERE TO ENSURE EXCELLENT ERROR HANDLING
            self.fancy_text("Welcome to Rooms!") # Short and brief
            input("\nPress Enter to begin > ")
    
    def show_help(self):
        # Define the help slides
        help_slides = [ # 4 help slides in total
"""===== HELP GUIDE (1/4) =====

Game Controls:
W - Move forward
S - Move backward
L - Loot current room
U - Use item from inventory
""",
"""===== HELP GUIDE (2/4) =====

Game Controls (continued):
Q - Quit game
H - Show this help menu
            
Game Basics:
- Explore 100 rooms with challenges
- Watch your health (100 max)
""",
"""===== HELP GUIDE (3/4) =====

Entities:
- Various creatures inhabit the rooms
- Each has unique behaviors
- Some can be avoided with quick thinking
            
Items:
- Find useful items while looting
- Manage your inventory carefully
""",
"""===== HELP GUIDE (4/4) =====

Puzzles & Obstacles:
- Every 25 rooms contain puzzles
- Solve them to progress
- Some rooms have obstacles to overcome
            
What will you do?
[P] Play Game
[Q] Quit
"""
        ]
        
        current_slide = 0 # Start at slide 0
        while True:
            print("\033c", end='')  # Clear screen
            self.fancy_text(help_slides[current_slide])
            
            if current_slide == len(help_slides) - 1:
                # Last slide - offer play/quit options
                choice = input("Choose: ").lower()
                if choice == 'p':
                    return  # Return to game
                elif choice == 'q':
                    self.fancy_text("\nThanks for checking out the game! Goodbye.")
                    exit()
                else:
                    self.fancy_text("Invalid choice. Please press P or Q.")
                    continue
            else:
                # Navigation for other slides
                choice = input("Press D for next page or A for previous page > ").lower()
                if choice == 'd' and current_slide < len(help_slides) - 1:
                    current_slide += 1 # Next slide
                elif choice == 'a' and current_slide > 0:
                    current_slide -= 1 # Previous slide
                elif choice in ('q', 'p'):
                    # Allow early exit if player wants
                    if choice == 'p':
                        return
                    else:
                        self.fancy_text("\nThanks for checking out the game! Goodbye.")
                        exit()
                else:
                    self.fancy_text("Invalid input. Use A/D to navigate.")
    
    def replay_prompt(self):
        """Replay option after death. Quite important"""
        while True:
            choice = input("\nWould you like to (R) replay or (Q) quit? > ").strip().lower()

            if choice == 'r': # Replay
                while True:
                    skipIntro = input("Skip the introduction? (Y/N) > ").strip().lower()
                    if skipIntro == 'y': # No intro
                        self.__init__() # Skip intro and just __init__
                        return True
                    elif skipIntro == 'n': # Yes intro
                        self.__init__()  # Reset game state
                        print("\033c", end='')  # Clear screen
                        self.show_intro() # Show the intro again
                        return True
                    else:
                        self.fancy_text("Invalid choice. Please enter Y or N.\n")  # This will loop again
            elif choice == 'q':
                self.fancy_text("\nThanks for playing! Goodbye.")
                exit()
            else:
                self.fancy_text("Invalid choice. Please enter R or Q.")

    @staticmethod
    def fancy_text(text):
        """
        A fancy text function to simulate typing effect
        I learnt this effect from Stack Overflow a few weeks ago, found it quite interesting, and adapted it for my game. Thank God I did.

        This is the sole reason why so many people praised my game, I owe it too much
        """
        for char in text:
            time.sleep(0.02) # Print character every 20 miliseconds
            print(char, end='', flush=True)
        print()