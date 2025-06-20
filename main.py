from constants import * # Import everything from constants.py
from functions import Game # Only need to import Game class since Player and Room will be background, game is the major class here
import time

def main():
    """Main user interface"""
    game = Game() # Main game functions
    print("\033c", end='') # Clear screen
    game.show_intro() # Intro
    print("\033c", end='')
    
    while True:
        print("\033c", end='')
        game.show_status() # Show player the status bar
        
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
        
        # Handle entity, obstacle or dupe rooms event
        if game.current_room in PUZZLES and game.current_room not in game.game_data["completed_puzzles"]:
            if not game.attempt_puzzle(game.current_room):
                game.fancy_text("\n💀  YOU DIED! Game over.")
                game.fancy_text(f"You made it to Room {game.current_room:04d}")
                game.fancy_text(f"Coins collected: {game.player.coins}")
                if not game.replay_prompt(): # Replay or nah
                    break
                continue
        elif room.has_entity:
            if not game.handle_entity_encounter():
                game.fancy_text("\n💀  YOU DIED! Game over.")
                game.fancy_text(f"You made it to Room {game.current_room:04d}")
                game.fancy_text(f"Coins collected: {game.player.coins}")
                if not game.replay_prompt():
                    break
                continue
        elif room.has_obstacle:
            if not game.handle_obstacle():
                game.fancy_text("\n💀  YOU DIED! Game over.")
                game.fancy_text(f"You made it to Room {game.current_room:04d}")
                game.fancy_text(f"Coins collected: {game.player.coins}")
                if not game.replay_prompt():
                    break
                continue
        
        # Get player input
        command = input("\nOptions: [W] Forward | [S] Backward | [L] Loot | [U] Use Item | [Q] Quit > ").lower()
        
        if command == "w":
            if not game.move_forward(): # Forward
                continue
        elif command == "s":
            game.move_backward() # Backward
        elif command == "l":
            game.loot_room() # Looting rooms
        elif command == "u":
            game.use_item() # Use item
        elif command == "q":
            game.fancy_text("\nThanks for playing! Goodbye.")
            exit() # Exit
        else:
            game.fancy_text("Invalid command! Please enter a valid command.")
            time.sleep(0.5) # Error handling

if __name__ == "__main__":
    main()