from constants import *
from functions import Game
import time

def main():
    """Main user interface"""
    game = Game()
    print("\033c", end='')  # Clear screen
    game.show_intro()
    print("\033c", end='')  # Clear screen
    
    while True:
        print("\033c", end='')  # Clear screen
        game.show_status()
        
        room = game.rooms[game.current_room]
        
        # Handle puzzle rooms first
        if game.current_room in PUZZLES and game.current_room not in game.game_data["completed_puzzles"]:
            game.attempt_puzzle(game.current_room)
            continue
        
        # Handle duplicated rooms event
        if room.has_duplicated_rooms:
            if not game.move_forward():  # This will trigger the event handling
                continue
        
        # Show room description
        game.fancy_text(room.persistent_description)
        
        # Handle entity or obstacle
        if room.has_entity:
            if not game.handle_entity_encounter():
                game.fancy_text("\n💀  YOU DIED! Game over.")
                if not game.replay_prompt():
                    break
                continue
        elif room.has_obstacle:
            if not game.handle_obstacle():
                game.fancy_text("\n💀  YOU DIED! Game over.")
                if not game.replay_prompt():
                    break
                continue
        
        # Get player input
        command = input("\nOptions: [W] Forward | [S] Backward | [L] Loot | [U] Use Item | [Q] Quit > ").lower()
        
        if command == "w":
            if not game.move_forward():
                continue
        elif command == "s":
            game.move_backward()
        elif command == "l":
            game.loot_room()
        elif command == "u":
            game.use_item()
        elif command == "q":
            game.fancy_text("\nThanks for playing! Goodbye.")
            exit()
        else:
            game.fancy_text("Invalid command! Please enter a valid command.")
            time.sleep(0.5)

if __name__ == "__main__":
    main()