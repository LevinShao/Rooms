from functions import * # Import everything from functions.py
from constants import * # Import everything from constants.py

def main():
    """Main function to run the game."""
    global current_room, player_health, inventory, coins, game_data # Initialize global variables

    show_intro() # Show the intro text to the player
    game_data["dark_rooms"] = generate_dark_rooms() # Generate dark rooms at the start of the game

    while True: # Main game loop
        show_status() # Show the current status of the player, such as their health, inventory, coins, and room number
        
        # Add the current room to the set of visited rooms immediately after player enters it
        if current_room not in game_data["visited_rooms"] and current_room > 0: # Except if the room is 000
            game_data["visited_rooms"].add(current_room)

        fancy_text(get_room_description()) # Display the room description

        # Give player the replay option when they die to an entity
        if not spawn_entities():
            replay_prompt()
            continue

        command = input("\nOptions: [W] Forward | [S] Backward | [L] Loot Room | [U] Use Item | [Q] Quit > ").lower() # Options bar right here

        if command == "w":
            move_forward() # Move forward to the next room
        elif command == "s":
            move_backward() # Move backward to the previous room
        elif command == "l":
            loot_room() # Loot the current room
            print("\033c", end="") # Clear screen
            continue
        elif command == "u":
            use_item() # Use an item from the inventory
            print("\033c", end="") # Clear screen
            continue
        elif command == "q":  # Quit the game
            fancy_text("\nThanks for playing! Goodbye :D")
            exit()
        else: # Invalid command error handler
            fancy_text("Invalid command! Please enter a valid option.")
            time.sleep(1)
            print("\033c", end="")
            continue

if __name__ == "__main__":
    main() # Start the game