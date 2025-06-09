from functions import * # Import everything from functions.py

# Main user interface for the game
def main():
    show_intro() # First of all, show the intro text to the player
    
    while True:
        fancy_text(f"Current Room: {get_current_room():03d}") # Display the current room number, rounded to 3 digits
        fancy_text(get_room_description()) # Display the room description
        
        command = input("\nOptions: [W] Forward | [S] Backward | [Q] Quit > ").strip().lower() # Options bar right here
        
        if command == "w": # Move forward
            move_forward()
        elif command == "s": # Move backward
            result = move_backward()
            if result:  # Only print if there's a message returned
                fancy_text(result)
        elif command == "q": # Quit the game
            fancy_text("\nThanks for playing! Goodbye.")
            break
        else:
            fancy_text("Invalid command. Use W/S to move or Q to quit.") # Invalid command error handler

if __name__ == "__main__":
    main()