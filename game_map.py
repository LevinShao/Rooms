# game_map.py
import json
import random

def load_room_data():
    with open("data/room_narrative.md", "r", encoding="utf-8") as f:
        data = f.read().split("#")[1:]
    
    return {title.strip(): narrative.strip() for title, narrative in [d.split(":", 1) for d in data if ":" in d]}

def create_grid():
    """Create a proper 10x10 grid with special room placement rules and obstacles"""
    room_narrative_dict = load_room_data()
    
    # Initialize grid
    grid = {}
    for row in range(10):
        grid[row] = {}
        for column in range(10):
            grid[row][column] = {
                "title": "Empty Room",
                "coordinates": (row, column),
                "narrative": "A nondescript empty room with nothing of interest."
            }

    # 1. Force specific rooms
    grid[0][0] = {  # Entrance Hall
        "title": "Entrance Hall",
        "coordinates": (0, 0),
        "narrative": room_narrative_dict["Entrance Hall"],
        "P": True
    }

    # 2. Place waiting areas adjacent to entrance
    waiting_areas = [(0,1), (1,0)]  # Right and below entrance
    for row, col in waiting_areas:
        grid[row][col] = {
            "title": "Waiting Area",
            "coordinates": (row, col),
            "narrative": room_narrative_dict["Waiting Area"]
        }

    # 3. Fixed throne room position
    grid[5][5] = {
        "title": "Throne Room",
        "coordinates": (5, 5),
        "narrative": room_narrative_dict["Throne Room"]
    }

    # 4. Place kitchen and dining hall together
    kitchen_placed = False
    dining_hall_placed = False
    attempts = 0
    while (not kitchen_placed or not dining_hall_placed) and attempts < 100:
        attempts += 1
        row, col = random.randint(0, 9), random.randint(0, 9)
        
        # Find spot for kitchen
        if not kitchen_placed and (row,col) not in [(0,0), (5,5), (9,9)]:
            grid[row][col] = {
                "title": "Kitchen",
                "coordinates": (row, col),
                "narrative": room_narrative_dict["Kitchen"]
            }
            kitchen_placed = True
            kitchen_pos = (row, col)
            
            # Place dining hall adjacent
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            random.shuffle(directions)
            for dr, dc in directions:
                new_row, new_col = row+dr, col+dc
                if (0 <= new_row < 10 and 0 <= new_col < 10 and 
                    grid[new_row][new_col]["title"] == "Empty Room"):
                    grid[new_row][new_col] = {
                        "title": "Dining Hall",
                        "coordinates": (new_row, new_col),
                        "narrative": room_narrative_dict["Dining Hall"]
                    }
                    dining_hall_placed = True
                    break

    # 5. Place remaining main rooms
    main_rooms = [
        "Dungeon Cell", "Torture Chamber", "Armory", 
        "Treasury", "Guard Room", "Courtyard",
        "Stable", "Library", "Laboratory", "Observatory",
        "Secret Passage", "Cavern", "Underwater Chamber",
        "Lava Cave", "Ice Cavern", "Chapel",
        "Royal Bedchamber", "Dungeon Crypt", "Kai Cenat's Tower",
        "Training Grounds", "Potion Storage", "Shrek's Swamp",
        "Ancient Ruins", "Moonlit Garden", "Clockwork Workshop"
    ]

    for room in main_rooms:
        attempts = 0
        while attempts < 100:
            row, col = random.randint(0, 9), random.randint(0, 9)
            if (row, col) not in [(0,0), (5,5), (9,9)] and grid[row][col]["title"] == "Empty Room":
                grid[row][col] = {
                    "title": room,
                    "coordinates": (row, col),
                    "narrative": room_narrative_dict.get(room, "A mysterious room.")
                }
                break
            attempts += 1

    # 6. Fill remaining rooms with generic descriptions
    generic_rooms = [
        "Storage Room", "Servant's Quarters", "Corridor", 
        "Abandoned Room", "Meeting Chamber",
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

    # 7. Place obstacles (reintroduced from old code)
    obstacle_types = [
        {"name": "Spiked Pit", "description": "The floor suddenly gives way beneath you!", "effect": "spiked_pit"},
        {"name": "Poison Gas", "description": "A noxious green gas begins filling the room!", "effect": "poison_gas"},
        {"name": "Collapsing Ceiling", "description": "The ceiling begins to crumble above you!", "effect": "collapsing_ceiling"},
        {"name": "Mysterious Altar", "description": "An ancient altar stands in the center. Interact? (Y/N)", "effect": "mysterious_altar"},
        {"name": "Illusionary Wall", "description": "The walls seem to shift and change!", "effect": "illusionary_wall"}
    ]

    # Place 5-10 obstacles in random rooms
    for _ in range(random.randint(5, 10)):
        attempts = 0
        while attempts < 100:
            row, col = random.randint(0, 9), random.randint(0, 9)
            if (row, col) not in [(0, 0), (5, 5), (9, 9)] and "O" not in grid[row][col]:
                obstacle = random.choice(obstacle_types)
                grid[row][col]["O"] = obstacle
                break
            attempts += 1

    # 8. Place items with special rules
    grid = place_items(grid)
    
    # 9. Place other game elements
    grid = place_cuddly_spirit(grid)
    grid = place_monsters(grid)
    grid = place_daphne(grid)

    # Save the grid
    with open("saves/game_data.json", "w") as f:
        json.dump(grid, f, indent=2, default=lambda o: '<not serializable>')
    return grid

def create_monsters():
    """Create monster definitions with balanced stats"""
    return [
        {"name": "Amoogus", "hitpoints": 5, "damage": (1, 3)},
        {"name": "Rick Astley", "hitpoints": 10, "damage": (2, 4)},
        {"name": "Elon Musk", "hitpoints": 20, "damage": (3, 6)},
        {"name": "Zhong Xina", "hitpoints": 25, "damage": (4, 8)},
        {"name": "Shrek", "hitpoints": 30, "damage": (5, 10), "special": "Onion of Power"},
        {"name": "Lirili Larila", "hitpoints": 45, "damage": (7, 12)},
        {"name": "Kai Cenat", "hitpoints": 60, "damage": (10, 15), "type": "minor_boss"},
    ]

def place_monsters(grid):
    """Place monsters with proper validation"""
    monsters = create_monsters()
    placed_monsters = set()
    
    # Load defeated monsters if available
    defeated_monsters = set()
    try:
        with open("saves/defeated_monsters.json", "r") as f:
            defeated_monsters = set(tuple(loc) for loc in json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    
    for monster in monsters:
        attempts = 0
        while attempts < 100:
            row, col = random.randint(0, 9), random.randint(0, 9)
            
            # Special placement rules
            if monster['name'] == "Shrek":
                for r in range(10):
                    for c in range(10):
                        if grid[r][c]["title"] == "Shrek's Swamp":
                            row, col = r, c
                            break
            elif monster['name'] == "Kai Cenat":
                # Kai Cenat prefers special rooms
                preferred_rooms = ["Kai Cenat's Tower", "Ancient Ruins", "Dungeon Crypt"]
                for r in range(10):
                    for c in range(10):
                        if grid[r][c]["title"] in preferred_rooms and (r,c) not in defeated_monsters:
                            row, col = r, c
                            break
            
            # Don't place in special rooms or cleared rooms
            if ((row, col) not in [(0, 0), (5, 5), (9, 9)] and 
                (row, col) not in placed_monsters and
                (row, col) not in defeated_monsters):
                if "M" not in grid[row][col] and "item" not in grid[row][col] and "D" not in grid[row][col]:
                    monster["coordinates"] = (row, col)
                    grid[row][col]["M"] = monster
                    placed_monsters.add((row, col))
                    break
            attempts += 1
    return grid

def place_items(grid):
    """Place items with special rules for potions"""
    items = {
        "Rusty Key": 1,
        "Magic Rune": 3,
        "Health Potion": 4,  # Increased number
        "Magic Scroll": 2
    }
    
    placed_items = set()
    
    for item, count in items.items():
        for _ in range(count):
            attempts = 0
            while attempts < 100:
                # Potions prefer specific rooms
                if item == "Health Potion":
                    preferred_rooms = ["Potion Storage", "Laboratory", "Kitchen"]
                    room_found = False
                    for r in range(10):
                        for c in range(10):
                            if grid[r][c]["title"] in preferred_rooms and (r,c) not in placed_items:
                                row, col = r, c
                                room_found = True
                                break
                        if room_found:
                            break
                    if not room_found:
                        row, col = random.randint(0, 9), random.randint(0, 9)
                else:
                    row, col = random.randint(0, 9), random.randint(0, 9)
                
                if ((row, col) not in [(0, 0), (5, 5), (9, 9)] and 
                    (row, col) not in placed_items and
                    "M" not in grid[row][col] and "D" not in grid[row][col]):
                    grid[row][col]["item"] = item
                    placed_items.add((row, col))
                    break
                attempts += 1
    return grid

def place_daphne(grid):
    """Place Daphne in fixed position [9,9] with proper setup"""
    grid[9][9] = {
        "title": "Dungeon Heart",
        "coordinates": (9, 9),
        "narrative": "The air crackles with dark energy. Daphne is trapped in a magical cage at the center, surrounded by sinister sigils.",
        "D": {
            "name": "Daphne",
            "hitpoints": 70,
            "requires_key": True
        }
    }
    return grid

def place_cuddly_spirit(grid):
    """Place secret pet with proper validation"""
    if random.random() < 0.1:  # 10% chance
        attempts = 0
        while attempts < 100:
            row, col = random.randint(1, 5), random.randint(1, 5)
            if ("M" not in grid[row][col] and "D" not in grid[row][col] 
                and "item" not in grid[row][col] and "secret" not in grid[row][col]):
                grid[row][col].update({
                    "title": "Fortune Chamber",
                    "narrative": "You found a secret chamber! A cute Cuddly Spirit floats toward you.",
                    "secret": {
                        "name": "Cuddly Spirit",
                        "type": "pet",
                        "heal_power": 5,
                        "luck_boost": 2
                    }
                })
                break
            attempts += 1
    return grid