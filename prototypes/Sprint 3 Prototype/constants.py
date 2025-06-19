import random

# Entity dictionary
ENTITIES = {
    "Tralalero Tralala": {
        "damage": 5, 
        "interaction": {
            "prompt": "Quickly! Press R to make him retreat!",
            "success_key": "r",
            "success_msg": "You scared Tralalero Tralala away!",
            "fail_msg": "You hesitated! Tralalero Tralala attacks you!"
        }
    },
    "Bombardino Crocodilo": {
        "damage": 10, 
        "interaction": {
            "prompt": "Press H to hide!",
            "success_key": "h",
            "success_msg": "You hid just in time!",
            "fail_msg": "You didn't hide! Bombardino Crocodilo attacks you!"
        }
    },
    "Boneca Ambalabu": {
        "damage": 5, 
        "interaction": {
            "prompt": "Don't look! Close your eyes (press C)",
            "success_key": "c",
            "success_msg": "You avoided eye contact!",
            "fail_msg": "You looked directly at Boneca Ambalabu!"
        }
    },
    "Tung Tung Tung Sahur": {
        "damage": 10, 
        "interaction": {
            "prompt": "Stay still! Don't press anything for 2 seconds",
            "success_key": None,  # Special timing-based interaction
            "success_msg": "You remained still and survived!",
            "fail_msg": "You moved and attracted Tung Tung Tung Sahur!"
        }
    }
}

# Items dictionary
ITEMS = {
    "Flashlight": {
        "description": "Lets you see in dark rooms",
        "effect": "light_room"
    },
    "Bandage": {
        "description": "Restores 10 HP",
        "effect": "heal",
        "amount": 10
    },
    "Lockpick": {
        "description": "50% chance to unlock doors",
        "effect": "unlock"
    },
    "Key": {
        "description": "Opens locked doors",
        "effect": "open_door"
    },
    "Starlight Jug": {
        "description": "Fully restores your health",
        "effect": "full_heal",
        "special": True  # Only found in special room
    }
}

# Obstacles dictionary
OBSTACLES = {
    "Broken Floor": {
        "description": "The floor ahead is crumbling. What will you do?",
        "options": {
            "Jump over": {
                "success_chance": 0.5, 
                "success": "You made it across safely!", 
                "fail": "You fell and took some damage!", 
                "damage": 10
            },
            "Go around": {
                "time_cost": "You take a much longer path, losing some coins.", 
                "coin_loss": (7, 13)
            },
        }
    },
    "Locked Door": {
        "description": "A sturdy locked door blocks your path.",
        "options": {
            "Use lockpick": {
                "item_required": "Lockpick", 
                "success_chance": 0.5, 
                "success": "The lock clicks open!", 
                "fail": "The lockpick broke!"
            },
            "Search for key": {
                "success_chance": 0.3, 
                "success": "You found a key!", 
                "fail": "No key here.", 
                "time_cost": "You wasted time searching."
            },
            "Break door": {
                "strength_check": 0.4, 
                "success": "You broke the door down!", 
                "fail": "The door breaks open, but you hurt your leg from kicking it too hard.", 
                "damage": 10
            }
        }
    },
    "Collapsed Ceiling": {
        "description": "Rubble blocks your path. How will you proceed?",
        "options": {
            "Climb over": {
                "success_chance": 0.6,
                "success": "You carefully climb over the debris!",
                "fail": "You slip and take damage!",
                "damage": 10
            },
            "Clear a path": {
                "time_cost": "It takes time to clear the path.",
                "damage": 5
            }
        }
    }
}

# Room descriptions
ROOM_TYPES = [
    "A dimly lit hallway with flickering lights.",
    "A spacious chamber with strange markings on the walls.",
    "A narrow passageway that creaks with every step.",
    "A circular room with an eerie humming sound.",
    "A damp corridor with water dripping from the ceiling.",
    "The thick layer of dust on every surface suggests no one has been here in years. Your footsteps leave clear prints.",
    "A cramped hotel room lie before you. You have to turn sideways to get through some sections.",
    "A formal conference room with a large table and high-backed chairs.",
    "A long, narrow aisle with torches spaced evenly along the walls."
]

# Dark room descriptions
DARK_ROOM_DESCRIPTIONS = [
    "Pitch black... you can't see anything. Who knows what might lurk here?",
    "Complete darkness surrounds you. You shiver in fear as you hear quiet whispers of God-knows-what.",
    "The lights have gone out completely. You are completely engulfed in darkness.",
]

# Special room puzzles
PUZZLES = {
    25: {
        "description": "You see three levers on the wall. Only one opens the path forward.",
        "solution": random.randint(1, 3),
        "hint": "The middle lever looks slightly more worn than the others.",
        "reward": {"item": "Bandage", "uses": 2}
    },
    50: {
        "description": "A riddle is inscribed on the wall: 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'",
        "solution": "echo",
        "hint": "It's what you hear in mountains and caves.",
        "reward": {"coins": 20}
    },
    75: {
        "description": "There are four pressure plates on the floor. Step on the correct sequence to proceed.",
        "solution": [2, 4, 1, 3],
        "hint": "The sequence forms a simple pattern.",
        "reward": {"item": "Lockpick", "uses": 1}
    },
    100: {
        "description": "The final challenge! Solve this math puzzle: What is the sum of the first 10 prime numbers?",
        "solution": 129,
        "hint": "The primes are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29",
        "reward": {"victory": True}
    }
}

# Special rooms with their unique properties
SPECIAL_ROOMS = {
    49: {
        "description": "Preparation Room: A safe space before the big puzzle.",
        "is_safe": True
    },
    51: {
        "description": "Grand Throne Room: Where the king once resided.",
        "is_safe": True,
        "special_item_chance": 0.3
    },
    52: {
        "description": "Levin's Shop: A place to spend your hard-earned coins.",
        "is_safe": True,
        "shop_items": {
            "Bandage": 10,
            "Lockpick": 15,
            "Flashlight": 20
        }
    },
    99: {
        "description": "Final Preparation Room: Rest before the last challenge.",
        "is_safe": True,
        "heal_amount": 50
    }
}

# In constants.py, remove Brr Brr Patapim from ENTITIES and add:
DUPLICATED_ROOMS_EVENT = {
    "description": "The room number is obscured... something feels wrong here.",
    "consequence": {
        "damage": 10,
        "message": "Brr Brr Patapim attacks you from the fake door!"
    }
}