from functions import *
from constants import *

def main():
    global current_room, player_health, inventory, coins # Initialize global variables
    
    show_intro() # Show the intro text to the player
    
    # Main game loop
    while player_health > 0:
        show_status() # As long as the player is alive, show the status bar
        
        # Room entry events
        if current_room not in game_data["visited_rooms"] and current_room > 0: # Skip Room 000
            game_data["visited_rooms"].add(current_room)
            if random.random() < 0.15:  # 15% chance for dark room
                game_data["dark_rooms"].add(current_room)
                # 50% chance to also make the next room dark
                if random.random() < 0.5 and current_room < 100:
                    game_data["dark_rooms"].add(current_room + 1)
        
        # Display room info
        if current_room in game_data["dark_rooms"]:
            fancy_text(f"DARK ROOM: {get_dark_room_description()}")
        else:
            fancy_text(get_room_description())
        
        # Entity encounter chance
        if current_room > 0 and random.random() < 0.2 + (0.01 * max(0, current_room - 90)): # Increase enemy encounter chance from Room 090 and onwards
            if not handle_entity_encounter():
                fancy_text("\nYOU DIED!")
                fancy_text("Better luck next time!")
                break
        
        # Get player input
        command = input("\nOptions: [W] Forward | [S] Backward | [L] Loot Room | [U] Use Item | [Q] Quit > ").lower() # The options bar right here
        
        if command == "w":
            # Move Forward
            move_forward()
        elif command == "s":
            # Move Backward
            move_backward()
        elif command == "l":
            # Loot Room
            loot_room()
            print("\033c", end="")  # Clear screen after looting
            continue  # Skip to next iteration to refresh display
        elif command == "u":
            # Use Item
            use_item()
            print("\033c", end="")  # Clear screen after using item
            continue  # Skip to next iteration to refresh display
        elif command == "q":
            # Quit
            fancy_text("\nThanks for playing! Goodbye :D")
            exit() # Exit the game
        else:
            # If invalid command
            fancy_text("Invalid command!")
    
    refresh_display()  # Force update after every action so the console stays neat and organised

if __name__ == "__main__":
    main()