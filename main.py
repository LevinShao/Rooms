from typing import Dict
import random
import time
from rooms import generate_rooms, typing_effect, print_with_typing, ENTITIES, ITEMS, get_random_item, handle_movement
import os


# Player stats
player = {
    "health": 100,
    "max_health": 100,
    "inventory": [],
    "current_room": 0,
    "has_flashlight": False
}


# Game initialization
def start_game():
    typing_effect("\nPress Enter to begin > ")
    input()
    print("\033c", end='')


def game_loader():
    time.sleep(1)
    print("\033c", end='')
   
    try:
        if os.path.exists("data/loader.md"):
            with open("data/loader.md", "r", encoding='utf-8') as f:
                loader = f.read()
                typing_effect(loader)
        else:
            typing_effect("Welcome to Rooms!")
    except Exception as e:
        typing_effect("Welcome to Rooms!")
        print(f"Error loading intro: {e}")


# Combat system
def combat(entity: Dict) -> bool:
    print_with_typing(f"\n!!! {entity['description']}")
    print_with_typing(f"ENTITY: {entity['name']} (Health: {entity['health']})")


    while entity["health"] > 0 and player["health"] > 0:
        action = input("[A]ttack | [H]ide | [U]se Item | [F]lee: ").upper()


        if action == "A":
            damage = random.randint(5, 15)
            entity["health"] -= damage
            print_with_typing(f"You deal {damage} damage!")
           
            if entity["health"] <= 0:
                return True
               
            entity_dmg = random.randint(*entity["damage"])
            player["health"] -= entity_dmg
            print_with_typing(f"{entity['name']} hits you for {entity_dmg} damage!")


        elif action == "H":
            if random.random() < 0.5:
                print_with_typing("You hide successfully!")
                return True
            print_with_typing("Your hiding spot wasn't good enough!")
            player["health"] -= random.randint(*entity["damage"])


        elif action == "U":
            if not player["inventory"]:
                print_with_typing("No items in inventory!")
                continue
               
            print_with_typing("Inventory: " + ", ".join([item["name"] for item in player["inventory"]]))
            item_name = input("Use which item? ").capitalize()
           
            for item in player["inventory"]:
                if item["name"] == item_name:
                    if item["name"] == "Bandage":
                        player["health"] = min(player["max_health"], player["health"] + 15)
                        print_with_typing("Used Bandage! Healed 15 HP!")
                    elif item["name"] == "Flashlight":
                        player["has_flashlight"] = True
                        print_with_typing("The flashlight cuts through the darkness.")
                    player["inventory"].remove(item)
                    break


        elif action == "F":
            if random.random() < 0.7:
                print_with_typing("You escaped!")
                return False
            print_with_typing("Escape failed!")
            player["health"] -= random.randint(*entity["damage"])


    return player["health"] > 0


# Mini-games
def library_minigame() -> bool:
    print_with_typing("\n=== LIBRARY PUZZLE ===")
    print_with_typing("Arrange the books in the correct order:")
    correct_order = ["3", "1", "4", "2"]
    attempts = 3


    while attempts > 0:
        guess = input("Enter order (e.g., '1 2 3 4'): ").split()
        if guess == correct_order:
            print_with_typing("The books glow! A hidden item appears.")
            player["inventory"].append({"name": "Ancient Tome", "description": "Grants +10 max HP."})
            player["max_health"] += 10
            player["health"] += 10
            return True
        attempts -= 1
        print_with_typing(f"Wrong! {attempts} attempts left.")
    return False


# Main game loop
def main():
    rooms = generate_rooms()
    game_loader()
    start_game()


    while player["health"] > 0:
        room = rooms[player["current_room"]]
       
        # Clear screen and show room
        print("\033c", end='')
        print_with_typing(f"=== {room['title']} (Door {room['number']}) ===")
       
        # Handle dark rooms
        if room.get("is_dark", False):
            if player["has_flashlight"]:
                print_with_typing(room["description"])
            else:
                print_with_typing("Pitch blackness. You can't see anything!")
                print_with_typing("You stumble and take damage!")
                player["health"] -= 5
        else:
            print_with_typing(room["description"])


        # Display player status
        print_with_typing(f"\n❤ Health: {player['health']}/{player['max_health']}")
        if player["inventory"]:
            print_with_typing("🎒 Inventory: " + ", ".join([item["name"] for item in player["inventory"]]))
        else:
            print_with_typing("🎒 Inventory: Empty")


        # Handle items
        if "item" in room and room["item"]:
            print_with_typing(f"\nYou found: {room['item']['name']}!")
            player["inventory"].append(room["item"])
            if room["item"]["name"] == "Flashlight":
                player["has_flashlight"] = True
            del room["item"]


        # Handle entities
        if "entity" in room and room["entity"]:
            if not combat(room["entity"]):
                if player["health"] <= 0:
                    break
                continue  # Player fled
            del room["entity"]


        # Check for death
        if player["health"] <= 0:
            break


        # Special rooms
        if room.get("is_special", False):
            if room["number"] == 50:
                library_minigame()
            elif room["number"] == 100:
                print_with_typing("\nYou reach the final door...")
                if combat(room["entity"]):
                    print_with_typing("\n=== YOU ESCAPED ===")
                    print_with_typing("The hotel's grip releases as you burst into daylight.")
                    print_with_typing("But... you swear you hear something laughing behind you...")
                    return
                break


        # Movement
        move = input("\n[W] Forward | [S] Backward | [L] Loot Items | [Q] Quit: ").upper()
        new_room = handle_movement(player["current_room"], move, rooms)
       
        if new_room == -1:  # Quit signal
            break
        player["current_room"] = new_room


    # Game over
    print_with_typing("\n=== GAME OVER ===")
    print_with_typing(f"You made it to Door {player['current_room']}")
    print_with_typing("The hotel claims another victim...")


if __name__ == "__main__":
    main()
