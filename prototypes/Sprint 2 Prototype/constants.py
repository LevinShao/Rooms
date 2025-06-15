import random

# Introducing the new constants.py file for the Sprint 2 Prototype of the game
# This file contains all the necessary constants and configurations for the game

# I'm going to substitute the original Doors entities with Italian brainrot characters.
# Just for the sake of copyright infringements, but I doubt that the original Doors game developers will even notice this game.

# Wiki for all the Doors entities: https://doors-game.fandom.com/wiki/List_of_Entities

# Current entity plan:
# Tralalero Tralala: Screech from the real Doors game
# Bombardino Crocodilo: Rush from the real Doors game
# Brr Brr Patapim: Dupe from the real Doors game
# Tung Tung Tung Sahur: Hide from the real Doors game
# Boneca Ambalabu: Eyes from the real Doors game

# Peter: Not an Italian brainrot character, but will act like Timothy from the real Doors game
# Peter won't included in the entity dictionary because a section in the loot_room function already handles him.

# Entity dictionary
ENTITIES = {
    "Tralalero Tralala": {"damage": 5},
    "Bombardino Crocodilo": {"damage": 10},
    "Brr Brr Patapim": {"damage": 10},
    "Boneca Ambalabu": {"damage": 10},
    "Tung Tung Tung Sahur": {"damage": 5}
}

# Items dictionary, will add more items soon
ITEMS = {
    "Flashlight": {"description": "Lets you see in dark rooms"},
    "Bandage": {"description": "Restores 10 HP"},
    "Lockpick": {"description": "50% chance to unlock doors"}
}

# All of the current room types. I tried to make them as generic as possible.
ROOM_TYPES = [
    "A dimly lit hallway with flickering lights.",
    "A spacious chamber with strange markings on the walls.",
    "A narrow passageway that creaks with every step.",
    "A circular room with an eerie humming sound.",
    "A damp corridor with water dripping from the ceiling."
] # This is a set, not a dictionary unlike the two above :)

# Dark room descriptions
def get_dark_room_description():
    return random.choice([
        "Pitch black... you can't see anything. Who knows what might lurk here?",
        "Complete darkness surrounds you. You shiver in fear as you hear quiet whispers of God-knows-what.",
        "The lights have gone out completely. You are completely engulfed in darkness.",
    ])