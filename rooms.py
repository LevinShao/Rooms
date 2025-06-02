from typing import Dict, List
import time
import random


# Entity definitions (Doors-inspired)
ENTITIES = {
    "Tung Tung Tung Sahur": {"health": 50, "damage": (5, 15), "description": "A tall, faceless creature stalks you..."}, # Tung Tung Tung Sahur in the real Doors Game
    "Boneca Ambalabu": {"health": 70, "damage": (10, 20), "description": "The walls melt as a monstrous presence chases you!"}, # Seek in the real Doors Game
    "Lirili Larila": {"health": 20, "damage": (2, 8), "description": "Glowing Lirili Larila watch from the darkness..."}, # Lirili Larila in the real Doors Game
    "Bombardino Crocodilo": {"health": 30, "damage": (8, 12), "description": "A blur of motion charges toward you!"}, # Rush in the real Doors Game
    "Tralalero Tralala": {"health": 20, "damage": (8, 12), "description": "A blur of motion charges toward you!"}, # Tralalero Tralala in the real Doors Game
    "Brr Brr Patapim": {"health": 20, "damage": (8, 12), "description": "A blur of motion charges toward you!"}, # Hide in the real Doors Game
    "Udin Din Din Dun": {"health": 20, "damage": (8, 12), "description": "A blur of motion charges toward you!"} # Dupe in the real Doors Game
}


ITEMS = {
    # Common items (60% chance)
    "Lockpick": {"description": "Unlocks a door once.", "uses": 1, "rarity": 60},
    "Flashlight": {"description": "Reveals hidden paths.", "uses": 5, "rarity": 60},
    "Bandage": {"description": "Heals 10-20 HP.", "uses": 1, "rarity": 60},
   
    # Uncommon items (30% chance)
    "Vitamins": {"description": "Reduces damage from any incoming entities. Lasts through 10 doors", "uses": 3, "rarity": 30},
    "Crowbar": {"description": "Breaks down a door.", "uses": 1, "rarity": 30},
   
    # Rare items (10% chance)
    "Health Potion": {"description": "Heals all your HP.", "uses": 1, "rarity": 10},
    "Crucifix": {"description": "Repels entities for 3 turns.", "uses": 1, "rarity": 10}
}


NORMAL_ROOMS = [
    {"title": "Standard Hallway", "description": "A narrow corridor with peeling wallpaper. The air smells of mildew."},
    {"title": "Abandoned Lounge", "description": "Broken furniture litters this once-elegant sitting area. A TV flickers with static."},
    {"title": "Maintenance Closet", "description": "Shelves of cleaning supplies. Something moves behind the mop bucket."},
    {"title": "Elevator Lobby", "description": "A broken elevator with its doors stuck open. The shaft yawns blackly below."},
    {"title": "Boiler Room", "description": "Pipes hiss steam in the oppressive heat. The metal floor creaks unnaturally."},
    {"title": "Guest Room", "description": "A perfectly made bed with mint on the pillow. Too perfect."},
    {"title": "Laundry Room", "description": "Industrial washers vibrate violently. Something thumps inside one."},
    {"title": "Staff Break Room", "description": "Cold coffee in a pot. The bulletin board has disturbing employee notices."},
    {"title": "Linen Closet", "description": "Towers of fresh towels. The scent of bleach can't mask something worse."},
    {"title": "Abandoned Office", "description": "Papers scattered everywhere. A single computer monitor glows with garbled text."}
]


DARK_ROOM_ADDENDUM = "\nThe lights flicker and die. An unnatural darkness swallows the room. Your breath fogs in the sudden chill."


# =========== TYPING EFFECT ===========
def typing_effect(text):
    for char in text:
        time.sleep(0.02)
        print(char, end='', flush=True)


def print_with_typing(text):
    typing_effect(text + "\n")


def generate_rooms() -> List[Dict]:
    """Generate 101 rooms (0-100) with special rooms and random variants"""
    rooms = []
   
    for i in range(101):  # Doors 0-100
        # Special rooms
        if i == 0:
            rooms.append({
                "number": 0,
                "title": "Reception",
                "description": "A dusty lobby with broken chandeliers. The exit is boarded up. A faded sign reads 'CHECK OUT... NEVER.'",
                "is_safe": True,
                "entity": None,
                "item": None,
                "is_special": False,
                "is_dark": False
            })
            continue
           
        if i == 1:
            rooms.append({
                "number": 1,
                "title": "Grand Hallway",
                "description": "A massive marble hallway with towering columns. The ceiling stretches into darkness.",
                "is_grand": True,
                "entity": None,
                "item": None,
                "is_special": False,
                "is_dark": False
            })
            continue
           
        if i == 50:
            rooms.append({
                "number": 50,
                "title": "Library",
                "description": "Books float in mid-air. A whispering voice demands you 'shelve the knowledge.'",
                "is_special": True,
                "puzzle": "books",
                "entity": None,
                "item": None,
                "is_dark": False
            })
            continue
           
        if i == 100:
            rooms.append({
                "number": 100,
                "title": "The Final Door",
                "description": "An obsidian door pulses like a heartbeat. The air hums with static.",
                "is_special": True,
                "entity": {"name": "Tung Tung Tung Sahur", **ENTITIES["Tung Tung Tung Sahur"]},
                "item": None,
                "is_dark": False
            })
            continue
           
        # Normal rooms
        room = random.choice(NORMAL_ROOMS).copy()
        room.update({
            "number": i,
            "is_special": False,
            "is_grand": False,
            "entity": None,
            "item": None,
            "is_dark": False
        })
       
        # 30% chance to become dark (except Grand Hallway)
        if random.random() < 0.3 and i != 1:
            room["description"] += DARK_ROOM_ADDENDUM
            room["is_dark"] = True
            if random.random() < 0.5:  # 50% chance for entity in dark rooms
                room["entity"] = {"name": random.choice(["Lirili Larila", "Tralalero Tralala"]),
                                 **ENTITIES[random.choice(["Lirili Larila", "Tralalero Tralala"])]}
        else:
            if random.random() < 0.2:  # 20% chance for entity in normal rooms
                room["entity"] = {"name": random.choice(list(ENTITIES.keys())),
                                 **ENTITIES[random.choice(list(ENTITIES.keys()))]}
       
        rooms.append(room)
   
    return rooms


# Add this new function
def get_random_item():
    """Return a random item based on rarity weights"""
    total = sum(item["rarity"] for item in ITEMS.values())
    rand = random.uniform(0, total)
    current = 0
    for item_name, item_data in ITEMS.items():
        if current + item_data["rarity"] > rand:
            return {"name": item_name, **item_data}
        current += item_data["rarity"]
    return None


# Modify the handle_movement function
def handle_movement(current_room: int, move: str, rooms: List[Dict]) -> int:
    """Validate and process movement with clear error messages"""
    if move == "W":
        if current_room >= 100:
            print_with_typing("A force blocks your path. The door won't budge.")
        else:
            return current_room + 1
    elif move == "S":
        if current_room <= 0:
            print_with_typing("The reception desk blocks your way. No turning back now.")
            print_with_typing("You must keep moving forward.")
        else:
            return current_room - 1
    elif move == "Q":
        confirm = input("Abandon your escape? (Y/N): ").upper()
        if confirm == "Y":
            return -1  # Quit signal
    elif move == "L":
        # 40% chance to find an item when looting
        if random.random() < 0.4 and "item" not in rooms[current_room]:
            item = get_random_item()
            if item:
                rooms[current_room]["item"] = item
                print_with_typing("You search the room carefully...")
                time.sleep(1)
                print_with_typing(f"You found: {item['name']}!")
            else:
                print_with_typing("You search the room but find nothing useful.")
        else:
            print_with_typing("You don't find anything useful here.")
    else:
        print_with_typing(f"'{move}' isn't a valid command. Use [W] forward, [S] back, [L] loot, or [Q] quit.")
    return current_room