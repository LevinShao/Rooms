import json
import random

# load the room descriptions from the md file into a dictionary
def load_room_data():
    with open("data/room_narrative.md", "r", encoding="utf-8") as f:
        data = f.read().split("#")[1:]
    
    return {title.strip(): narrative.strip() for title, narrative in [d.split(":") for d in data]}

def create_grid():
    """Create a 10x10 grid representing the game map with special room placement."""
    room_narrative_dict = load_room_data()
    
    # Initialize the grid
    grid = {}
    for row in range(10):
        grid[row] = {}
        for column in range(10):
            grid[row][column] = {
                "title": "Empty Room",
                "coordinates": (row, column),
                "narrative": "A nondescript empty room with nothing of interest."
            }

    # Force specific rooms
    grid[0][0] = {  # Entrance Hall (player spawn)
        "title": "Entrance Hall",
        "coordinates": (0, 0),
        "narrative": "You enter a large hall, the floor is made of marble and the walls are adorned with ancient tapestries. The room is dimly lit, but you can see the silhouette of a figure in the distance.",
        "P": True
    }

    # Place throne room in a random location (but not at spawn)
    throne_room_pos = (random.randint(3, 9), random.randint(3, 9))
    grid[throne_room_pos[0]][throne_room_pos[1]] = {
        "title": "Throne Room",
        "coordinates": throne_room_pos,
        "narrative": "You enter a grand throne room, with a majestic throne at the far end. The room is filled with guards, and you can see the king sitting on his throne, looking down at you."
    }

    # List of main rooms to place (excluding throne room and entrance)
    main_rooms = [
        "Dungeon Cell", "Torture Chamber", "Armory", "Kitchen", 
        "Dining Hall", "Treasury", "Guard Room", "Courtyard",
        "Stable", "Library", "Laboratory", "Observatory",
        "Secret Passage", "Cavern", "Underwater Chamber",
        "Lava Cave", "Ice Cavern", "Chapel",
        "Royal Bedchamber", "Dungeon Crypt", "Kai Cenat's Tower",
        "Training Grounds", "Potion Storage", "Shrek's Swamp",
        "Ancient Ruins", "Moonlit Garden", "Clockwork Workshop"
    ]

    # Place main rooms
    for room in main_rooms:
        while True:
            row, col = random.randint(0, 9), random.randint(0, 9)
            # Don't overwrite entrance, throne room, or already placed main rooms
            if (row, col) != (0, 0) and (row, col) != throne_room_pos and grid[row][col]["title"] == "Empty Room":
                grid[row][col] = {
                    "title": room,
                    "coordinates": (row, col),
                    "narrative": room_narrative_dict[room]
                }
                break

    # Fill remaining rooms with generic descriptions
    generic_rooms = [
        "Storage Room", "Servant's Quarters", "Corridor", 
        "Abandoned Room", "Meeting Chamber", "Waiting Area",
        "Small Hallway", "Forgotten Alcove", "Dusty Chamber"
    ]
    
    for row in range(10):
        for column in range(10):
            if grid[row][column]["title"] == "Empty Room":
                room_type = random.choice(generic_rooms)
                grid[row][column] = {
                    "title": room_type,
                    "coordinates": (row, column),
                    "narrative": room_narrative_dict.get(room_type, "A nondescript room with nothing remarkable.")
                }

    # Place exit (not in throne room)
    while True:
        exit_row, exit_col = random.randint(5, 9), random.randint(5, 9)
        if (exit_row, exit_col) != throne_room_pos:
            grid[exit_row][exit_col]["E"] = True
            break

    # Place items and special features
    grid = place_items(grid)
    grid = place_cuddly_spirit(grid)
    grid = place_monsters(grid)
    grid = place_daphne(grid)

    # Save the grid
    with open("saves/game_data.json", "w") as f:
        json.dump(grid, f)
    return grid

# create a list of monsters with random hitpoints
def create_monsters():
    monsters = [
        {"name": "Amoogus", "hitpoints": 5},
        {"name": "Rick Astley", "hitpoints": 10},
        {"name": "Elon Musk", "hitpoints": 20},
        {"name": "Zhong Xina", "hitpoints": 25},
        {"name": "Shrek", "hitpoints": 30},
        {"name": "Lirili Larila", "hitpoints": 45},
        {"name": "Kai Cenat", "hitpoints": 60, "type": "minor_boss"},
    ]
    return monsters

# place the monsters in random rooms
def place_monsters(grid):
    monsters = create_monsters()
    for monster in monsters:
        while True:
            row, col = random.randint(0, 9), random.randint(0, 9)
            # Special placement rules
            if monster['name'] == "Shrek":
                # Find Shrek's Swamp room
                for r in range(10):
                    for c in range(10):
                        if grid[r][c]["title"] == "Shrek's Swamp":
                            row, col = r, c
                            break
            elif monster['name'] == "Kai Cenat":
                # Kai Cenat can appear in any non-starting room
                pass
            elif monster['name'] == "Duke Dennis":
                # Duke Dennis only appears in final encounter
                continue
                
            # Don't place monsters in starting room
            if (row, col) != (0, 0):
                monster["coordinates"] = (row, col)
                grid[row][col]["M"] = monster
                break
    return grid

def place_items(grid):
    """Place game items in random rooms with enhanced variety"""
    items = {
        "Rusty Key": (random.randint(1,5), random.randint(1,5)),
        "Magic Rune": [(random.randint(0,5), random.randint(0,5)) for _ in range(3)],
        "Health Potion": [(random.randint(0,5), random.randint(0,5)) for _ in range(2)],
        "Magic Scroll": [(random.randint(0,5), random.randint(0,5)) for _ in range(2)]
    }
    
    for item, coord in items.items():
        if isinstance(coord, list):
            for c in coord:
                while True:
                    if "M" not in grid[c[0]][c[1]] and "D" not in grid[c[0]][c[1]]:
                        grid[c[0]][c[1]]["item"] = item
                        break
                    c = (random.randint(0,5), random.randint(0,5))
        else:
            while True:
                if "M" not in grid[coord[0]][coord[1]] and "D" not in grid[coord[0]][coord[1]]:
                    grid[coord[0]][coord[1]]["item"] = item
                    break
                coord = (random.randint(0,5), random.randint(0,5))
    return grid

# put Daphne in a random room
def place_daphne(grid):
    """Place Daphne in a single random room that's not the starting position"""
    while True:
        row, col = random.randint(1, 9), random.randint(1, 9)  # Expanded range to 9x9
        # Check if room is empty and not special rooms
        if ("M" not in grid[row][col] and "item" not in grid[row][col] 
            and grid[row][col]["title"] not in ["Throne Room", "Shrek's Swamp"]):
            daphne = {
                "name": "Daphne", 
                "hitpoints": 70,
                "requires_key": True
            }
            grid[row][col]["D"] = daphne
            # Special description for Daphne's room
            grid[row][col]["title"] = "Dungeon Heart"
            grid[row][col]["narrative"] = "The air crackles with dark energy. Daphne is trapped in a magical cage at the center of the room, surrounded by the Rat King's sigils."
            return grid
        
def place_cuddly_spirit(grid):
    """Place a secret room with a 10% chance"""
    if random.random() < 0.1:  # 10% chance for secret room
        while True:
            row, col = random.randint(1,5), random.randint(1,5)
            if "M" not in grid[row][col] and "D" not in grid[row][col] and "item" not in grid[row][col]:
                grid[row][col]["title"] = "Fortune Chamber"
                grid[row][col]["narrative"] = "You found the fortune chamber! A cute Cuddly Spirit floats towards you."
                grid[row][col]["secret"] = {
                    "name": "Cuddly Spirit",
                    "type": "pet",
                    "heal_power": 5,
                    "luck_boost": 2
                }
                break
    return grid

# print where the player it
def print_player_location(grid):
    for row in grid:
        for column in grid[row]:
            if "P" in grid[row][column]:
                print(f"You are in the {grid[row][column]['title']}")
    return grid

# print where daphne is
def print_daphne_location(grid):
    for row in grid:
        for column in grid[row]:
            if "D" in grid[row][column]:
                print(f"Daphne is in the {grid[row][column]['title']}")
    return grid

# print where the monsters are
def print_monster_location(grid):
    for row in grid:
        for column in grid[row]:    
            if "M" in grid[row][column]:
                print(f"There is a {grid[row][column]['M']['name']} in the {grid[row][column]['title']}")
    return grid