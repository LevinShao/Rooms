import json
import random
import time
from game_map import create_grid, place_monsters, place_daphne, place_items

player_stats = {
    "health": 100,
    "inventory": [],
    "moves_left": 101
}

def typing_effect(text):
    for char in text:
        time.sleep(0.02)
        print(char, end='', flush=True)

def print_with_typing(text):
    """Helper function to print with typing effect and newline"""
    typing_effect(text + "\n")

def combat(player, monster, is_final_boss=False):
    """Handle combat between player and monster with new options"""
    print_with_typing(f"\n⚔️  Combat with {monster['name']} (HP: {monster['hitpoints']})")
    
    has_pet = any(isinstance(item, dict) and item.get('type') == 'pet' for item in player['inventory'])
    pet_heal_chance = 0.3 if has_pet else 0
    
    while monster['hitpoints'] > 0 and player['health'] > 0:
        usable_items = [item for item in player['inventory'] if isinstance(item, str) and item in ["Health Potion", "Magic Scroll"]]
        
        print_with_typing(f"\n❤️  Your HP: {player['health']}")
        print_with_typing(f"🖤 Monster HP: {monster['hitpoints']}")
        print_with_typing("\nWhat will you do?")
        
        if is_final_boss:
            action = input("A - Attack | D - Defend | H - Heal | I - Use Item > ").lower()
        else:
            action = input("A - Attack | D - Defend | H - Heal | I - Use Item | F - Flee > ").lower()
        
        if action == "i" and usable_items:
            print_with_typing("\nAvailable items:")
            for i, item in enumerate(usable_items, 1):
                print_with_typing(f"{i}. {item}")
            choice = input("Use which item? (or cancel) ")
            if choice.isdigit() and 0 < int(choice) <= len(usable_items):
                used_item = usable_items[int(choice)-1]
                if used_item == "Health Potion":
                    heal = random.randint(10, 20)
                    player['health'] += heal
                    print_with_typing(f"Used Health Potion! Healed for {heal} HP!")
                elif used_item == "Magic Scroll":
                    damage = random.randint(5, 15)
                    monster['hitpoints'] -= damage
                    print_with_typing(f"Used Magic Scroll! Dealt {damage} damage!")
                player['inventory'].remove(used_item)
                continue
            else:
                print_with_typing("Invalid choice or no items available")
                continue
                
        if action == "a":
            damage = random.randint(5, 15)
            monster['hitpoints'] -= damage
            print_with_typing(f"You deal {damage} damage!")
            
            if monster['hitpoints'] > 0:
                monster_dmg = random.randint(1, 3)
                player['health'] -= monster_dmg
                print_with_typing(f"{monster['name']} hits you for {monster_dmg} damage!")
                
        elif action == "d":
            reduction = random.randint(1, 3)
            monster_dmg = max(0, random.randint(1, 3) - reduction)
            player['health'] -= monster_dmg
            print_with_typing(f"You brace for impact! Damage reduced by {reduction}.")
            if monster_dmg > 0:
                print_with_typing(f"{monster['name']} hits you for {monster_dmg} damage!")
            else:
                print_with_typing("You completely block the attack!")
                
        elif action == "h":
            heal_amount = random.randint(2, 5)
            player['health'] += heal_amount
            print_with_typing(f"You focus and recover {heal_amount} HP!")
            
            if has_pet and random.random() < pet_heal_chance:
                extra_heal = random.randint(2, 5)
                player['health'] += extra_heal
                print_with_typing(f"Your Cuddly Spirit helps you heal an extra {extra_heal} HP!")
            
            monster_dmg = random.randint(1, 3)
            player['health'] -= monster_dmg
            print_with_typing(f"{monster['name']} hits you for {monster_dmg} damage!")
            
        elif action == "f":
            flee_chance = 0.3 + (0.1 if has_pet else 0)
            if random.random() < flee_chance:
                print_with_typing("You escaped successfully!")
                # Move player to a random adjacent room
                directions = [(0,1), (1,0), (0,-1), (-1,0)]  # N, E, S, W
                random.shuffle(directions)
                for dr, dc in directions:
                    new_row, new_col = player_coordinates[0]+dr, player_coordinates[1]+dc
                    if 0 <= new_row < 10 and 0 <= new_col < 10:
                        player_coordinates = (new_row, new_col)
                        break
                return False  # Combat ended by fleeing
            else:
                print_with_typing("Escape failed!")
    
    if monster['hitpoints'] <= 0:
        print_with_typing(f"\nYou defeated {monster['name']}!")
        return True
    return False

def random_line():
    with open("data/quotes.md", "r", encoding='utf-8') as f:
        lines = f.readlines()
        random_line = random.choice(lines)
        typing_effect(random_line)

def loading_effect(text):
    print("\033c", end='')
    for char in text:
        time.sleep(0.1)
        print(char, end='', flush=True)

def load_game():
    try:
        with open("saves/game_data.json", "r") as f:
            grid_data = json.load(f)
        return grid_data
    except FileNotFoundError:
        print_with_typing("Game data not found. Creating new game...")
        return create_grid()

def start_game():
    typing_effect("\nPress Enter to begin > ")
    input()
    print("\033c", end='')

def game_loader():
    grid = load_game()
    time.sleep(1)
    print("\033c", end='')
    try:
        with open("data/loader.md", "r", encoding='utf-8') as f:
            loader = f.read()
            typing_effect(loader)
    except FileNotFoundError:
        typing_effect("Welcome to The Navigation Game!")

# Main game execution
grid = create_grid()
grid = place_monsters(grid)
grid = place_daphne(grid)
game_loader()
start_game()

print("\033c", end='')

objectives = {
    "find_daphne": False,
    "find_key": False,
    "runes_collected": 0
}

player_coordinates = (0, 0)
last_coordinates = (0, 0)

while True:
    current_room = grid[player_coordinates[0]][player_coordinates[1]]
    player_stats['moves_left'] -= 1
    
    if current_room["title"] == "Shrek's Swamp" and "M" in current_room and current_room["M"]["name"] == "Shrek":
        print_with_typing("\n👹 WHAT ARE YOU DOING IN MY SWAMP?!")
        monster = current_room["M"]
        if combat(player_stats, monster):
            del current_room["M"]
            current_room["item"] = "Onion of Power"
            print_with_typing("\nShrek drops a magical onion as he falls!")
        else:
            continue
    
    if player_stats['health'] <= 0:
        print_with_typing("\nYou died! Game Over. Better luck next time!")
        break
    if player_stats['moves_left'] <= 0:
        print_with_typing("\nTime's up! The Duke sacrificed Daphne.")
        print_with_typing("Her screams echo in your mind. You drop down to your knees and cry.")
        print_with_typing("Game Over. Better luck next time.!")
        break
        
    print("\033c", end='')
    random_line()
    print()
    
    print_with_typing(f"Moves left: {player_stats['moves_left']} | Health: {player_stats['health']}")
    print_with_typing(f"Coordinates: [{player_coordinates[0]}, {player_coordinates[1]}]")
    
    print_with_typing("\n" + "="*40)
    typing_effect(current_room["title"])
    print_with_typing("\n" + "="*40)
    typing_effect(current_room["narrative"])
    
    if "item" in current_room:
        item = current_room["item"]
        if "Rune" in item:
            objectives["runes_collected"] += 1
            print_with_typing(f"\n✨ You found a Magic Rune! ({objectives['runes_collected']}/3)")
            if objectives["runes_collected"] == 3:
                print_with_typing("A mysterious power surges through you! The runes glow brightly.")
        elif item == "Rusty Key":
            objectives["find_key"] = True
            print_with_typing("\n🔑 You found the Rusty Key! It hums with ancient magic.")
        elif item == "Onion of Power":
            print_with_typing("\n🧅 You got the Onion of Power! It makes you cry tears of strength!")
            player_stats["health"] += 30
            print_with_typing("Your health increased by 30!")
        player_stats['inventory'].append(item)
        del current_room["item"]
    
    if "secret" in current_room:
        secret = current_room["secret"]
        print_with_typing(f"\n🌟 {secret['name']} wants to join you!")
        print_with_typing("It will help you in combat and increase your luck!")
        player_stats['inventory'].append(secret)
        del current_room["secret"]
    
    if "M" in current_room:
        monster = current_room["M"]
        print_with_typing(f"\n\n👹 You encountered {monster['name']}!")
        if combat(player_stats, monster):
            del current_room["M"]
        else:
            continue

    if "D" in current_room:
        if objectives["find_key"] and objectives["runes_collected"] >= 3:
            print_with_typing("\nYou insert the Rusty Key into the magical lock.")
            time.sleep(2)
            print_with_typing("The three runes float from your pocket and shatter the barrier!")
            time.sleep(2)
            
            # Duke Dennis appears!
            duke_dennis = {
                "name": "Duke Dennis", 
                "hitpoints": 70,
                "type": "final_boss"
            }
            print_with_typing('\nSuddenly, a dark figure emerges from the shadows!')
            print_with_typing('"NOT SO FAST!" bellows Duke Dennis, the final boss himself!')
            
            if combat(player_stats, duke_dennis, is_final_boss=True):
                print_with_typing("\nWith Duke Dennis defeated, the magic cage shatters completely!")
                time.sleep(2)
                typing_effect('\nDaphne: "You did it! You really did it! The Duke\'s magic is broken!"')
                time.sleep(2)
                typing_effect('\nYou and Daphne embrace and share a passionate kiss, the magic of the runes swirling around you')
                print_with_typing("\n\n🎉 VICTORY! You rescued Daphne!")
                print_with_typing("Thanks for playing!")
                break
            else:
                print_with_typing("\nDuke Dennis strikes you down as Daphne watches in horror!")
                print_with_typing("Game Over. Better luck next time!")
                break
        else:
            print_with_typing("\nBefore you stands Daphne, trapped in a shimmering magical cage.")
            time.sleep(2)
            typing_effect('\nDaphne: "You found me! But... the Duke\'s magic..."')
            time.sleep(1)
            
            missing_items = []
            if not objectives["find_key"]:
                missing_items.append("Rusty Key")
            if objectives["runes_collected"] < 3:
                missing_items.append(f"{3 - objectives['runes_collected']} more runes")
            
            print_with_typing(f"\nYou need: {', '.join(missing_items)} to break the enchantment.")
            time.sleep(2)
            print_with_typing("\nThe magic repels you backward!")
            input("\nPress Enter to continue > ")
            
            player_coordinates = last_coordinates
            print("\033c", end='')
            continue

    while True:
        movement = input("\n\nUse W, A, S, D to move > ").lower()
        
        new_coordinates = player_coordinates
        if movement == "w":
            new_coordinates = (player_coordinates[0] - 1, player_coordinates[1])
        elif movement == "a":
            new_coordinates = (player_coordinates[0], player_coordinates[1] - 1)
        elif movement == "s":
            new_coordinates = (player_coordinates[0] + 1, player_coordinates[1])
        elif movement == "d":
            new_coordinates = (player_coordinates[0], player_coordinates[1] + 1)
        else:
            print_with_typing("Invalid input. Use W, A, S, D to move.")
            continue
            
        if (0 <= new_coordinates[0] < 10) and (0 <= new_coordinates[1] < 10):
            last_coordinates = player_coordinates
            player_coordinates = new_coordinates
            break
        else:
            print_with_typing("\nYou tried to go this way, but there's a wall blocking your path.")
            print_with_typing("Try another direction!")