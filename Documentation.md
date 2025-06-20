# **11ASE Assessment Task 2 - ROOMS**
## **By Levin Shao**
=======================================================================
# **Sprint 1**
## **Requirements and Specifications**
## The Plan
I am planning to recreate the extremely popular Roblox game called Doors made by LSPLASH into my own version in Python. This game will be using a basic command-line interface (since Doors is a game that will require excellent visual graphics if made with a GUI application, and since I don't have too much experience with Pygame and Tkinter I'm just not sure how I would be able to find a way to recreate it there taking considerations of time restraints). 

If you aren't familiar with what the game Doors is about (which I'm sure you don't), it is a very famous horror-survival game on Roblox and it involves a group of up to 4 players (or they can go solo) trying to survive 100 doors to get to the other side. They spawn at Door 0, which is the Reception area, and each time they survive and escape a room, they will enter the next room, so they will reach Door 001, 002, 003 and so on up to 100. Every single door has a chance for a monster to spawn, and they must react quickly in order to survive them, otherwise they die. Door 100 involves players to complete a mini-game that is extremely difficult, requiring them to fix broken wires around the map while simutaneously trying to avoid Figure, the final boss, who will traverse around the map seeking players based on audio cues. However, if they complete the mini-game and escape Door 100, they beat the game.
## Requirements Outline
### Functional Requirements
* **Data Retrieval:** What does the user need to be able to view in the system? 

    The user should be able to view their current door number, room description, health, inventory items, and contextual event details (e.g., monster descriptions and rules for puzzles). This data must update dynamically as the player progresses (since information like current door number and room description update every time they enter a new room) or when they encounter challenges and obstacles.

* **User Interface:** What is required for the user to interact with the system?

    Obviously, the user will need a functional computer in order to run the program. Then, they will need to either use an online code compiler website or install an IDE software with a code terminal for the program to run, with Visual Studio Code being the most recommended. Users will need basic abilities to read and type in order to respond to the on-screen prompts, and lastly, install a few packages in the requirements.txt file.

* **Data Display:** How should the presented data be displayed in the system?

    The system must output the player’s current door, health, event descriptions (e.g. "Room 023: You hear a monster echo in the distance..." or something like that, but since I'm writing this before writing the actual program it is hard for me to decide yet), as well as success/failure outcomes. Critical information (e.g. low health) should be highlighted, possibly with symbols like "⚠️" to show that it is a critical issue. These presented information will all be shown in text form as system outputs in the code terminal.

### Non-Functional Requirements
* **Performance:** How well does the system need to perform?

    In order for users to have a enjoyable time with the game, the system must respond to inputs within very few seconds to maintain immersion. Text should render without lag, and event generation (e.g., monster spawns) must feel instantaneous. Also, we must ensure that the code is fully optimized to the best of its ability, so that it is able to run smoothly even on the oldest (but still working) device there is. The program also shouldn't cause any issues such as freezing or crashing VS Code during usage.

* **Reliability:** How reliable does the system and data need to be?

    The system and data should be very reliable for the user to have an enjoyabke experience. First of all, we must ensure that there are no bugs or glitches in the program. Also, the game should never crash or stop working from invalid inputs. Player progress (current door, health) must persist until death/victory, and unintended loops (e.g. getting stuck in menus) must be prevented and fixed immediately.

* **Usability and Accessibility:** How easy to navigate does the system need to be? What instructions will we need for users to access the system?

    Although this program will be much harder to understand and play with than my last assessment task submission (of which I made a TMDb Movie Database Explorer API application), it still shouldn't be too hard to understand even for those with limited technical expertise given the on-screen instructions as well as a detailed, comprehensive help guide that players can access. Moreover, players should be able to play the game with just a keyboard since the system mainly takes keyboard commands. Lastly, the game can be easily ran with just the VS Code terminal, making it quite accessible.

## Determining Specifications
### Functional Specifications
* **User Requirements:** What does the user need to be able to do?

    Users should have basic common knowledge of how the program operates, and be able to navigate around the program easily and efficiently, demonstrating capability to interact with the system, even if it is their first time of playing the game. They should be able to understand the basic rules of the game, knowing the most basic knowledge such as W to move to next room and S to go back a room, as well as knowing how to hide from deadly entities and deal with oncoming obstacles.

* **Inputs & Outputs:** What inputs will the system need to accept and what outputs will it need to display?

    The system should only be accepting inputs from keyboard keys as a way to improve accessibility. The Enter key is an input that the system will need to accept since it will be used to enter the game, and so the system will load the game as a result. Within the game, W and S keys are the main keys for movement, and they are two of the most important user inputs as well since movement is essential to win the game. U and Q will also be input keys, U being the "use item" option and Q being "quit", with the game exiting if the user decides to press Q.

* **Core Features:** At its core, what specifically does the program need to be able to do?

    The main core features the game focuses on are procedural room and event generation, health tracking, win/lose conditions, as well as a restart system. Events should vary from game to game, and the program will also train the user's reflexes & IQ abilities (e.g. hiding from the monsters demand quick reactions, and puzzles require logic).

* **User Interaction:** How will users interact with the system (e.g. command-line, GUI?) and what information will it need to provide to help users navigate?

    My program will be a CLI application that guides players throughout the game with text prompts. It may sound very simple with nothing much going on, but in order for me to create my project with GUI applications like Pygame or Ursina will be extremely difficult, not to mention I pretty much don't have any major experience with any of these (If I really wanted to make the game a 3D GUI app, Unity would've been a better option instead of Pygame/Ursina). In terms of information that it provides to help users, contextual hints (e.g. "Rush is coming! Quickly, enter H to hide!") appear during events. Moreover, the help command will reiterate all the controls.
    ##### **Side note:** Rush is a major hostile entity from the original Doors Roblox game that tends to rush through doors very quickly. If the player isn't hiding/within its line of sight, they get killed instantly.

* **Error Handling:** What possible errors could you face that need to be handled by the system?

    First of all, my program must be able to handle the most common type of warnings: invalid keys trigger warnings (Example of resolution: "Invalid command! Use W/S to move!"). In situations whereas certain movement might be prohibitied (e.g. trying to go backwards at Room 0 a.k.a the entrance) will result in error statements (Example of resolution: "It's too late for you to go back. Your only choice is forward."). Edge cases (whereas health might go below 0) should reset the game gracefully. Also, if it does become an issue, input loops (e.g. endless prompts) will be be prevented with timeout safeguards.

### Non-Functional Specifications

* **Performance:** How quickly should we try to get the system to perform tasks, what efficiency is required to maintain user engagement? How can we ensure our program remains efficient?

    To improve overall performance and efficiency, I can make the event resolutions, such as combat outcomes, feel instantaneous. Also, a chunk of text that is getting printed in the terminal at once can break immersion, so I might use a typing effect that loads the text progressively, allowing users to catch up with the text and read them properly so that no information are getting missed out on. Lastly, any loops or specific calculations within my code will be heavily optimised so that the overall output process is faster and more accurate.

* **Usability & Accessibility:** How might you make your application more accessible? What could you do with the User Interface to improve usability?

    To improve the usability and accessibility of the overall game, I'm going to make the onscreen instructions as clear as possible to clear out any possible confusion that will be brought upon the player during the game. The overall design should be simple, and I will also give clear error messages that explains the issue as well as outlining the resolutions towards them. Lastly, usability of the user interface could be improved by using minimalistic-styled menus, and accessibility will be massively improved by using user input keys that can be accessed with just a keyboard. 

* **Reliability:** What could perhaps not crash the whole system, but could be an issue and needs to be addressed? Data integrity? Illogical calculation? Menu navigation going to wrong places?

    To ensure reliability and data integrity, we must first ensure that health and door values never corrupt mid-game. Also, we should prevent any illogical outcomes, such as healing above max HP, from happening. Navigation must always reflect valid choices (e.g. no "Room 101"), and all monsters should have their own unique behaviour, making sure that they don't get mixed up. Lastly, the data for the player's items should not override or corrupt. If all of these are achieved, then the reliability of the game will ultimately be ensured.

## Use Cases for Functional Requirements

### Use Case 1: Data Retrieval

&nbsp;&nbsp;&nbsp;&nbsp; **Actor:** Player

&nbsp;&nbsp;&nbsp;&nbsp; **Preconditions:** Game is running; player has either started a new session or loaded a saved one.

&nbsp;&nbsp;&nbsp;&nbsp; **Main Flow:**
1. Player presses W to advance to next door, leading to the system generating a new room/event.
2. System displays necessary information along the way such as updated door number (e.g. "Room 024"), room description, and health status.
3. System uses the random module to randomly decide if an event should be triggered in the player's current room.
4. If an event triggers (e.g. monster spawning or obstacles), system retrieves and displays the event details (e.g. "You hear Rush charging at you in the distance! Press H to hide!").

&nbsp;&nbsp;&nbsp;&nbsp; **Alternative Flow:**

1. An event doesn't trigger in the player's current room.
2. Player progresses to the next room, repeating the whole main flow process.

&nbsp;&nbsp;&nbsp;&nbsp; **Postconditions:** Player sees real-time updates of door number, health, and event context.

![Data Retrieval Use Case](/images/Use%20Case%20Diagrams/Data%20Retrieval%20Use%20Case.png)

### Use Case 2: User Interface

&nbsp;&nbsp;&nbsp;&nbsp; **Actor:** Player

&nbsp;&nbsp;&nbsp;&nbsp; **Preconditions:** Python environment is fully set up; game is launched in code terminal.

&nbsp;&nbsp;&nbsp;&nbsp; **Main Flow:**
1. Player uses Enter key to start the game after introduction plays out.
2. Player uses W/S to navigate the rooms, and the system processes input instantly.
3. During events, player uses a combination of keys and inputs for actions, and the system validates input.
4. Player presses Q, leading to the system exiting gracefully after confirmation ("Quit? Y/N").

&nbsp;&nbsp;&nbsp;&nbsp; **Alternative Flow:**

1. Player inputs an invalid command/key during interaction (e.g. Z)
2. System ignores input and displays controls reminder ("Use W or S!").

&nbsp;&nbsp;&nbsp;&nbsp; **Postconditions:** Player interacts with the game seamlessly via CLI; invalid inputs never crash the game.

![User Interface Use Case](/images/Use%20Case%20Diagrams/User%20Interface%20Use%20Case.png)

### Use Case 3: Data Display

&nbsp;&nbsp;&nbsp;&nbsp; **Actor:** Player

&nbsp;&nbsp;&nbsp;&nbsp; **Preconditions:** Player is mid-game; an event occurs.

&nbsp;&nbsp;&nbsp;&nbsp; **Main Flow:**
1. Player encounters an entity (encountering an event)
1. System outputs event description (e.g. "Room 056: The lights flicker...").
2. Any critical information is highlighted (e.g. "⚠️ Health: 10/100").
3. Success/failure outcomes are clear (e.g. "You survived the monster!").

&nbsp;&nbsp;&nbsp;&nbsp; **Alternative Flow:**
1. Player health goes down to 0 and they die in-game.
2. The system displays loss screen and prompts restart.

&nbsp;&nbsp;&nbsp;&nbsp; **Postconditions:** Information is formatted for clarity; urgent statuses like low health are emphasized.

![Data Display Use Case](/images/Use%20Case%20Diagrams/Data%20Display%20Use%20Case.png)

## **Design**

### Game Introduction Storyboard
![Game Intro Storyboard](/images/Storyboards/Game%20Intro%20Storyboard.png)

### Normal Room Storyboard
![Normal Room Storyboard](/images/Storyboards/Normal%20Room%20Storyboard.png)

### Entity Room Storyboard
![Entity Room Storyboard](/images/Storyboards/Entity%20Room%20Storyboard.png)

### Levin's Shop (Room 052) Storyboards
![Storyboard 1](/images/Storyboards/Levin's%20Shop%20Storyboard%20Part%201.png)
![Storyboard 2](/images/Storyboards/Levin's%20Shop%20Storyboard%20Part%202.png)

### Game Outro Storyboard
![Game Outro Storyboard](/images/Storyboards/Game%20Outro%20Storyboard.png)

### Level 0 Data Flow Diagram/Context Diagram
![Level 0 DFD](/images/DFDs/Level%200%20DFD.png)

### Level 1 Data Flow Diagram
![Level 1 DFD](/images/DFDs/Level%201%20DFD.png)

### Gantt Chart (No Milestones Yet)
No milestones highlighted because this Gantt Chart is made as a start-of-project time management outlook rather than a whole end-of-project review of my time management throughout the task, meaning that this is how I wish my time developing this would be like. This Gantt Chart is made in Sprint 1. For the Gantt Chart which would be made in the foreseeable future that will have milestones lablled on them (since the milestones are supposed to be when I actually completed the sections of the task), I will put it into Sprint 4 as a fully updated end-of-project review.

![Gantt Chart](/images/Gantt%20Charts/Gantt%20Chart.png)

## **Build and Test**
**functions.py** - This looks quite long at first glance but I assure you half of it is made up of code comments
```python
# With lots of background research and extensive testing, this code has somehow took me just around an hour to write.
# Will add lots of code comments since last time a major critique was that I didn't add enough comments to my code.

import time # time module is needed for the fancy text effect
import random # random module is used to generate room descriptions

current_room = 0  # Start at Room 000

# A fancy text function to simulate typing effect
# I learnt this effect from Stack Overflow a few weeks ago, found it quite interesting, and adapted it for my game.
def fancy_text(text):
    """Print text with a typing effect to make it look less boring than usual."""
    for char in text:
        time.sleep(0.02)  # This sets the typing speed, 0.02s (20 miliseconds) is the delay between each character
        print(char, end='', flush=True)
    print()  # Add a new line at the end to properly format the output

# Show the introduction text when someone first boots up the game
def show_intro():
    print("===================================")
    print("      DOORS GAME CLI Prototype     ")
    print("===================================")
    print("\nWelcome to the Doors Game CLI Prototype! This is an extremely simple level-1 prototype of my actual project.")
    print("\nNavigate with W (forward) / S (backward).\n")

# ------------------------ ROOM HANDLING FUNCTIONS ------------------------

# Room description templates
# The program will randomly select one of these 5 descriptions for each room using the random module
ROOM_TYPES = [
    "A dimly lit hallway with flickering lights.",
    "A spacious chamber with strange markings on the walls.",
    "A narrow passageway that creaks with every step.",
    "A circular room with an eerie humming sound.",
    "A damp corridor with water dripping from the ceiling."
]

# The arrows pointing to either the "str" or "int" classes are called TYPE HINTS.
# Type hints are used to indicate what type of value a function should return.
# Although unnecessary and doesn't affect the behavior of the actual function, they are useful for readability and maintainability of the code.
# I'm implementing them in this code after learning about them from a YouTube video about Agile Python development practices.
# They are VERY versatile for Agile programs!

# In this case, the expected return type of the get_room_description function is a string, hence the "-> str" at the end of the function definition.
def get_room_description() -> str:
    """Randomly picks a room description for a room out of the five above."""
    # Exceptions for special rooms
    if current_room == 0: # Room 000 is the entrance room with a fixed description.
        return "Entrance: A creaky wooden door behind you."
    elif current_room == 100: # Room 100 is the final "room" with a fixed description. This "room" will lead to the exit.
        return "You stumble into the outside, seeing a massive gate covered in angelic symbols in front of you."
    else: # For every single other room, select a random description from the ROOM_TYPES list.
        # Seed the random generator with room number for consistent descriptions
        random.seed(current_room)
        # First round the room number to 3 digits as a form of convention from the original Doors game, then return the randomly generaated description
        return f"Room {current_room:03d}: {random.choice(ROOM_TYPES)}"

# In this case, the expected return type of the get_room_description function is an integer, hence the "-> int" at the end of the function definition.
def get_current_room() -> int:
    """A mini function that returns the player's current room number."""
    return current_room # That's it, just a single line of code that returns the current room number

# ---------------------- MOVEMENT FUNCTIONS ----------------------

def move_forward() -> str:
    """Move to the next room (up to Room 100)."""
    global current_room # Use a global variable to keep track of the current room number

    # Normal movement logic for Room 000 to Room 099
    if current_room < 100:
        current_room += 1 # Increment the room number by 1 every time the player moves forward
        fancy_text(f"Moved forward to Room {current_room:03d}.") # Round the room number to 3 digits as a form of convention from the original Doors game
        time.sleep(0.5) # Short pause so the player can read the message properly
        print("\033c", end="") # Clear the console screen for a fresh look
        return ""
    # For Room 100 specifically.
    else:
        outro_text = (
            "\nYou've reached the exit beyond Room 100!\n" # Funny thing is that Room 100 isn't even technically a room because it's not an enclosed space, but I still label it as a room because the original Doors game also does that.            "Congratulations! You've beaten the first prototype of my game!\n"
            "However, take notice that there are absolutely no entities or obstacles in this game, because it's just a prototype.\n"
            "Meaning that this is essentially not even a game, more of an unfinished walking simulator.\n"
            "Now go out there and beat the real game featuring many difficult challenges!"
        )
        fancy_text(outro_text)
        time.sleep(1.5)  # Have a 1.5s pause for the victory message
        
        while True:
            # Ask the player if they want to replay or quit
            # strip() removes any leading or trailing whitespace, lower() allows the user to input lowercase letters so that they don't have 
            choice = input("\nWould you like to (R) replay or (Q) quit? ").strip().lower()
            if choice == 'r': # If the player wants to replay the game
                current_room = 0  # Reset to Room 000
                print("\033c", end="") # Clear console screen
                show_intro()  # Show intro again
                return ""
            elif choice == 'q': # Quit the game
                fancy_text("\nThanks for playing! Goodbye.")
                exit()
            else:
                fancy_text("Invalid choice. Please enter R or Q.") # If the player inputs an invalid choice, ask them to input again

def move_backward() -> str:
    """Move to the previous room (down to Room 000)."""
    global current_room # Use a global variable to keep track of the current room number
    # If the player is not in Room 000, which is the entrance room, allow them to move backward
    if current_room > 0:
        current_room -= 1 # Decrement the room number by 1 every time the player moves backward
        message = f"Moved backward to Room {current_room:03d}." # Round the room number to 3 digits as a form of convention from the original Doors game
        fancy_text(message)
        time.sleep(0.5) # Short pause so the player can read the message properly
        print("\033c", end="") # Clear the console screen for a fresh look
        return ""
    # Specifically for Room 000
    else:
        fancy_text("The door behind you is blocked. You can't turn back now.") # Show an error message if the player tries to go back from Room 000
        time.sleep(0.5) # Short pause
        print("\033c", end="") # Clear console screen
        return ""
```

**main.py**
```python
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
```
### What Was New In Sprint 1
Sprint 1's code is very basic. It's literally just a set of 100 rooms, and you're given only the options to either move forward or backward, or straight-up quit the game. Nothing much in this sprint because overall this is just the first sprint, and I also thought that I would need more time to research how to properly structure the code in Sprint 2, so I left the more important stuff to later sprints. Right now, all you can do is spawn at room 000, navigating rooms by moving forward and backward, and exit Room 100 with absolutely no risks, puzzles or challenges along the way. In fact, player health isn't even introduced at this stage! Literally nothing could go wrong!

## **End of Sprint 1 - Review Questions**

### Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.
* Refer to specific criteria or expectations outlined in your requirements document.

In terms of the functional requirements for the current stage of the project, the **user interface** section has been done pretty well since the program allows for the most basic user inputs (W/S to move) and the program is easy to run on any device. In terms of **data retrieval** and **data display** however, since this was the first prototype of the game instead of the actual, much more complicated real game, I had intentionally made it so that it doesn't show too much prompts to the user, since I felt like the first prototype should be basic, simple and not too confusing, I only included around 10% of the information that will be shown to the users during the real game, and decided that the rest 90% will be included in major functions that will be created in later sprints. But overall I felt like I had kept them to good standards.

In terms of the non-functional requirements, I have been very careful with the performance aspect, and I feel like I've kept it to great standards, since the system produces no lag, responds to text inputs instantly, generates text at a speed which the users can take their time and read, and refreshes the terminal every time the player enters or exits a room, giving a sense of cleanliness especially to those who may be diagnosed with Obsessive-Compulsive Disorder. Reliability has been done decently, since the game involves no bugs or errors, doesn't crash the system, and each function works well. The program is also indeed very usable and accessible, since the whole nature of the program is that it can be used within Visual Studio Code (which it achieved, easily), and also, the user interface is simple, the instructions are very clear and kept to minimum, and the error messages are very helpful as well.

### Analyse the performance of your program against the key use-cases you identified.
* Discuss whether the program behaves as expected and handles input/output as planned.

The program does behave as expected at the current stage. It works as expected in the use cases, and I'm personally very proud of it. The program handles inputs and outputs seamlessly as well, going forward when W is entered and backwards when S is entered, not to mention I have achieved all of this through extremely simple code that controls basic movement. As of right now, the program works just as depicted in the data retrival use cases. User interface's use case has mostly been achieved, though the lack of special events like monsters and obstacles has prevented it from being fully perfect. In terms of data display's use case, I'd say that my program was up to its standards, being able to display the most important information and highlight any critical information. Overall, the program managed to flawlessly demonstrate the main flows of all the use cases.

### Assess the quality of your code in terms of readability, structure, and maintainability.
* Consider naming conventions, use of functions, comments, and overall organisation.

In terms of code structure and readability, I feel like I have excelled in these parts, since I have decided to implement integration, which already makes the code neater by segregating the code into two separate files. The first file (main.py) is for the main text interface, and the latter (functions.py) contains ALL of the functions for the system, which would all be imported to main.py for use. In functions.py, More importantly, I've used something new in my code, called **type hints**, which are responsible for converting messy chunks of code to make them look more visually-pleasing. Type hints act as a form of documentation that helps developers understand the types of arguments a function expects and what it returns. This enhanced clarity makes the code more readable and easier to understand. Moreover, I have separated functions using code comments, sorting them into different categories. I have used an abundant amount of code comments to explain the code and what each part does, and I’ve also tried to optimize the code to the best of my ability. Each function is accompanied with DocStrings, and every single part of the code is organised and very readable. The code can be maintained easily in the long run, since it involves very basic code that can be modified and expanded without any problems at any time.

### Explain the improvements that should be made in the next stage of development.
* Include both feature enhancements and refinements to code quality or structure.

In the next stages of development, I will start to add monsters, obstacles, items, challenges and special room events, as well as implementing Levin’s Shop at Room 052. At the time of writing, I am very afraid that I will not be able to do a good job at this project because of the sheer amount of complexity involved according to my plans. However, as a somewhat experienced Python programmer who has also spent time researching about Doors in his spare time, I believe that I would be able to manage the development of this effectively. My next sessions will include the implementation of much more functions, specifically regarding event handling. I will also begin working on the development of a looting system, and puzzles that will appear at major rooms such as Room 050 and 100.

## **Launch**
The README file for the prototype can be found in the prototypes folder!

# **Sprint 2**
## **Design**

## Structure Chart
![Structure Chart](/images/Structure%20Chart.png)

### Pseudocode - **MAIN GAME LOOP**

```
BEGIN main
    CALL show_intro_screen()

    WHILE TRUE:
        SET player_health = 100
        SET current_room = 000
        SET inventory = []
        SET coins = 0
        
        WHILE player_health > 0:
            DISPLAY room_banner(current_room)
            DISPLAY health_status(player_health)
            DISPLAY room_description(current_room)
            DISPLAY player_inventory(inventory)
            
            IF current_room == 50:
                CALL puzzle_minigame("Room50_Puzzle")
                IF puzzle_minigame("Room50_Puzzle") == SUCCESS:
                    INPUT "You did it!"
                    PROCEED
                ELSE:
                    INPUT "You died. Better luck next time!"
                        EXIT
            ELSE IF current_room == 100:
                CALL puzzle_minigame("Final_Room")
                IF puzzle_minigame("Final_Room") == SUCCESS:
                        DISPLAY victory_sequence()
                        INPUT "Replay (R) or Quit (Q)? " choice
                        IF choice == 'R':
                            BREAK
                        ELSE:
                            EXIT
                ELSE:
                    INPUT "You died. Better luck next time!"
                    EXIT
            
            INPUT player_action
            SWITCH player_action:
                CASE 'W':
                    CALL move_forward()
                CASE 'S':
                    CALL move_backward()
                CASE 'A/D':
                    CALL handle_special_action()
                CASE 'U':
                    CALL use_item()
                CASE 'L':
                    CALL loot_room()
                CASE 'Q':
                    EXIT
                DEFAULT:
                    DISPLAY "Invalid input (Use W/S/A/D/V/L/Q)"
END
```

### How the Pseudocode Works
When the game first initiates, show the intro text to the player. Afterwards, set player's health to 100 and room number to 000, because the player's health starts at 100 and can only decrement, with room number being the opposite. Then set a list storage for items that te players own, because this list storage will be the player's inventory throughout the game. Lastly, set the amount to coins to 0, since player will start with no coins and can only obtain them by looting.

When the player's health is above 0 (i.e. if they are still alive) then display the room information, their current inventory and health status for every single room they progress through. If the player is at Room 050, call the mid-game puzzle which will be challenging. If the player fails, the game exits itself. If the player is at Room 100, they must complete the final, ultimate puzzle. After completion, call the final victory sequence (which is a chain of text that celebrates the player winning) will play out, then the player will be given a choice to either replay the game or to quit. If they don't pass the final puzzle, the game exits itself.

**(Note: more puzzles might be added in later updates, since this is only my current idea for now.)**

The next section is the basic player command handler. If the player chooses W as their desired action, they proceed forward. If S, then backward. The keys A and D are used to handle special events, such as when an entity named **"Dupe"** spawns and the player has to choose the next door. U will let the player use an item from their inventory, L will let the player loot the room in search for items and coins, and Q will let the player exit the game. Lastly, if the player chooses an option that is completely invalid, send them an error message. Simple!

## Pseudocode - **CORE SUBROUTINES**
### **Moving Forward Subroutine**
```
FUNCTION move_forward()
    IF current_room == 100:
        RETURN
    
    INCREMENT current_room
    DISPLAY "Entering Room {current_room:03d}"
    
    CALL check_dark_room()
    CALL check_locked_door()
    CALL spawn_entity()
    CALL spawn_obstacles()

    IF current_room == 52:
        CALL levin_shop_menu()
    
    IF current_room >= 90:
        INCREASE entity_spawn_chance BY 1% per room
        INCREASE obstacle_chance BY 1% per room
END FUNCTION
```
### How the Pseudocode Works
Extremely simple. First of all, let the system check if they are at Room 100, because beyond that will be the exit and they will not be able to move forward anymore, so return if the current room is 100. If not, then increase the current room by 1 every single time. Display to the user that they have entered the new room, with the room number rounded to 3 d.p. as a convention to the original Doors game. Each new room must check if it's a dark room, contains a locked door, or will spawn events such as monsters and obstacles. If the current room is 052, then call for exceptions to the movement system to make way for Levin's Shop. Lastly, when the player progresses beyond Room 090, then increase event spawn rate by 1% for every room. Simple!

### **Loot Room Subroutine**
```
FUNCTION loot_room()
    IF room_already_looted:
        DISPLAY "You find only a few stray coins in the dust..."
        RETURN
    
    ADD RANDOM(2, 8) TO coins
    DISPLAY "You find {coins_found} coins scattered about"
    
    IF RANDOM(1,100) <= 35:
        ADD random_item TO inventory
        DISPLAY "Among the coins, you discover: {item_name}!"
    
    IF RANDOM(1,100) <= 15:
        player_health -= 15
        DISPLAY "AHH! Timothy the Spider jumps from the coins and scratches you! - 5HP"
        DISPLAY "The spider retreats, leaving the money behind..."
    
    SET room_looted = True
END FUNCTION
```
### How This Pseudocode Works
The pseudocode demonstrates my looting system, which demonstrates the player looting the room's drawers and closets. First of all, when the player loots, they will always obtain coins ranging from 2 to 8. Then, with a 35% chance, they will find an item as part of their loot. With a 15% chance, the player gets attacked by an unexpected Timothy the Spider hiding in the drawers (but still receives coins). The player can only loot a room once (otherwise display error message and return), and after they loot, set **room_looted** to true. Simple!

## Flowchart - **MAIN GAME LOOP**
![Flowchart 1](/images/Flowcharts/Main%20Game%20Loop.png)

## Flowchart - **CORE SUBROUTINES**
### **Moving Forward Subroutine**
![Flowchart 2](/images/Flowcharts/Move%20Forward.png)
### **Loot Room Subroutine**
![Flowchart 2](/images/Flowcharts/Loot%20Room.png)

## **Build and Test**
**NOTE: Due to the serious time struggles I had with this prototype, I have not had enough time to fully playtest the game. Therefore bugs are definitely present in the game and don't be surprised if you find some. But I'd much rather work on the next few prototypes than fix bugs in this one, since this is just a prototype and not the final product.**

**constants.py**

Created constants.py! I created it because there were way too many constants according to my plan, and I didn't want to shove them all into **functions.py**, so I decided to add them to a new Python file as a method of integration for overall neatness and organization.
```python
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
```
**functions.py**

60% code comments and DocStrings, 40% actual code. Will import everything from **constants.py**
```python
# Total time to write: Around 3 days
# I had to consult some people online just to debug and get help with some parts of the code
# Since I had serious problems with the entity spawning system and the replay function

# Note: I have given up trying to create Levin's Shop in this prototype
# It was way too hard to implement, and I felt like introducing it in this prototype would be too early.
# I definitely will find a way to implement it in later versions, but I'm gonna take a rest now.
# Although this would make the coins useless, I'm keeping them here anyways just for experimentation purposes for the system.

# Also, due to the serious time struggles I had with this prototype, I have not had enough time to fully playtest the game
# Therefore bugs are definitely present in the game and don't be surprised if you find some
# But I'd much rather work on the next few prototypes than fix bugs in this one, since this is just a prototype and not the final product

# --------------------------------------------------------------------------------------------------------------------------------

import time # Time is needed for the fancy text effect and pauses
import random # Random is very useful in this game, almost every function relies on it
from constants import * # Import everything from constants.py

# Game state
current_room = 0 # Start at Room 000
player_health = 100 # Start with full health
inventory = [] # A list that stores the player's items (i.e. their inventory)
coins = 0 # A variable that stores the player's coins, which can be used to buy items.

# A dictionary that stores the game data, such as visited rooms, looted rooms, and dark rooms
# set() is used to store unique values, which is useful for visited and looted rooms
game_data = {
    "visited_rooms": set(), # Visited rooms will be stored here
    "looted_rooms": set(), # Looted rooms will be stored here
    # Dark rooms will be stored here, generated at the start of the game
    # There will be at least 10 dark rooms, with some of them having a 50% chance to make the next room dark as well
    "dark_rooms": set(),
    "entity_spawned_rooms": set() # Track rooms that have had entities spawn in them, and make sure that they don't spawn in that room again
}

# Show the introduction text when someone first boots up the game
def show_intro():
    print("===================================")
    print("      DOORS GAME CLI Prototype     ")
    print("===================================")
    print("\nWelcome to the Doors Game CLI Prototype! This is an extremely simple level-2 prototype of my actual project.")
    print("\nNavigate with W (forward) / S (backward).\n")

# A fancy text function to simulate typing effect
# I learnt this effect from Stack Overflow a few weeks ago, found it quite interesting, and adapted it for my game.
def fancy_text(text):
    """Print text with a typing effect to make it look less boring than usual."""
    for char in text:
        time.sleep(0.02)  # This sets the typing speed, 0.02s (20 miliseconds) is the delay between each character
        print(char, end='', flush=True)
    print()  # Add a new line at the end to properly format the output

def move_forward() -> str:
    """Move to the next room (up to Room 100)."""
    global current_room # Use global variable to keep track of the current room number

    # Normal movement logic for Room 000 to Room 099
    if current_room < 100:
        current_room += 1 # Increment the room number by 1 every time the player moves forward
        # Mark room as visited when moving forward
        game_data["visited_rooms"].add(current_room)
        # Round the room number to 3 digits as a form of convention from the original Doors game
        fancy_text(f"Moved forward to Room {current_room:03d}.")
        time.sleep(0.5) # Short pause so the player can read the message properly
        print("\033c", end="") # Clear the console screen for a fresh look
        return ""
    # For Room 100 specifically
    else:
        outro_text = (
            "\nYou've reached the exit beyond Room 100!\n" # Funny thing is that Room 100 isn't even technically a room because it's not an enclosed space, but I still label it as a room because the original Doors game also does that.
            "Congratulations! You've beaten the second prototype of my game!\n"
            "However, take notice that there are absolutely no entities or obstacles in this game, because it's just a prototype.\n"
            "Meaning that this is essentially not even a game, more of an unfinished walking simulator.\n"
            "Now go out there and beat the real game featuring many difficult challenges!"
        )
        fancy_text(outro_text)
        time.sleep(1) # Have a 1s pause for the victory message
        replay_prompt() # Ask the player if they want to replay or quit after the victory message
        return ""

def move_backward() -> str:
    """Move to the previous room (down to Room 000)."""
    global current_room # Use a global variable to keep track of the current room number
    # If the player is not in Room 000, which is the entrance room, allow them to move backward
    if current_room > 0:
        current_room -= 1 # Decrement the room number by 1 every time the player moves backward
        # No need to mark as visited here since forward movement already did it
        # Round the room number to 3 digits as a form of convention from the original Doors game
        fancy_text(f"Moved backward to Room {current_room:03d}.")
        time.sleep(0.5) # Short pause so the player can read the message properly
        print("\033c", end="") # Clear the console screen for a fresh look
        return ""
    else: # Specifically for Room 000
        # Show an error message if the player tries to go back from Room 000
        fancy_text("The door behind you is blocked. You can't turn back now.")
        time.sleep(0.5) # Short pause
        print("\033c", end="") # Clear the screen
        return ""
    
# In this case, the expected return type of the get_room_description function is a string, hence the "-> str" at the end of the function definition.
def get_room_description() -> str:
    """Randomly picks a room description for a room out of the five above."""
    # Exceptions for special rooms
    if current_room == 0: # Room 000 is the entrance room with a fixed description.
        return "Reception Area: A creaky wooden door behind you."
    elif current_room == 100: # Room 100 is the final "room" with a fixed description. This "room" will lead to the exit.
        return "You stumble into the outside, seeing a massive gate covered in angelic symbols in front of you."
    elif current_room in game_data["dark_rooms"]:
        return f"⚠️  DARK ROOM: {get_dark_room_description()}"
    else: # For every single other room, select a random description from the ROOM_TYPES list.
        random.seed(current_room)
        return f"Room {current_room:03d}: {random.choice(ROOM_TYPES)}"
    
def generate_dark_rooms():
    """Randomly assigns dark rooms for the run."""
    # Assign 10 dark rooms randomly between 1 and 99 (excluding 0 and 100)
    num_dark_rooms = max(10, int(100 * 0.1))
    dark_rooms = set(random.sample(range(1, 100), num_dark_rooms))
    # Make some dark rooms consecutive
    for room in list(dark_rooms):
        if random.random() < 0.5 and room < 99: # 50% chance to make the next room dark as well
            dark_rooms.add(room + 1) # Apply the dark room effect to the next room
    return dark_rooms # Return the set of dark rooms

def spawn_entities():
    """
    Spawn entities in the current room.
    
    This function's main purpose is to handle entity spawning in rooms
    but it's also used to ensure that once a room has had an entity spawned, 
    then it doesn't spawn another entity ever again for the duration of the game.
    """
    global current_room, player_health # Access current room and player health variables

    # Don't spawn in first/last room or rooms that have already had entities
    if (current_room == 0 or current_room == 100 or 
        current_room in game_data.get("entity_spawned_rooms", set())):
        return True

    # SYSTEM CHECKS THE CURRENT ROOM. IS IT A DARK ROOM?
    # IF YES, SET SPAWN RATE TO 40%, IF NO, CHECK IF IT'S A ROOM 090 OR HIGHER
    # IF YES, SET SPAWN RATE TO 30%, IF NO, SET SPAWN RATE TO 15%, SINCE THAT ROOM SHOULD BE A ROOM FROM 001-089 AND NOT DARK

    if current_room in game_data["dark_rooms"]:
        spawn_chance = 0.4 # Set 40% spawn chance in dark rooms
    elif current_room >= 90:
        spawn_chance = 0.3 # 30% chance since difficulty is ramped up when the player reaches the final few rooms
    else:
        spawn_chance = 0.15 # Default spawn chance

    if random.random() < spawn_chance: # If entity spawns
        entity = random.choice(list(ENTITIES.keys())) # Choose a random entity to spawn
        entity_data = ENTITIES[entity] # Get the entity data from the ENTITIES dictionary in constants.py

        fancy_text(f"\nOh no! {entity} appears!")
        player_health -= entity_data["damage"] # Deduct the entity's damage from the player's health
        fancy_text(f"You lost {entity_data['damage']} HP! (Current HP: {player_health})")
        
        # Mark this room as having had an entity spawn so that it doesn't spawn another entity in this room again

        # I would've just made it so that all visited rooms are prevented from spawning an entity, but for some reason it just doesn't work when I try it
        # After a few hours of attempted debugging, I just gave up on it and made a separate set for entity spawned rooms
        # Not too code-efficient but hey, when you need the program to work, you need the program to work
        if "entity_spawned_rooms" not in game_data:
            game_data["entity_spawned_rooms"] = set()
        game_data["entity_spawned_rooms"].add(current_room)
        
        if player_health <= 0: # Death messages
            fancy_text("\nYOU DIED! NOOOOOOOOO 😭")
            fancy_text("Better luck next time... that's all I can say 😢")
            return False
        
        return True # If the entity spawned and the player is still alive, return True
    return True # If no entity spawned, return True

def replay_prompt():
    """The legendary replay option is right here! Handles replay or quit after death or victory"""
    while True: # Ask the player if they want to replay or quit
        choice = input("\nWould you like to (R) replay or (Q) quit? ").strip().lower() # strip removes whitespaces, lower allows lowercase input
        if choice == 'r': # If the player wants to replay the game
            # Reset game state
            global current_room, player_health, inventory, coins, game_data
            current_room = 0
            player_health = 100
            inventory = []
            coins = 0
            game_data = {
                "visited_rooms": set(),
                "looted_rooms": set(),
                "dark_rooms": generate_dark_rooms(),
                "entity_spawned_rooms": set()
            }
            print("\033c", end="") # Clear the console screen
            show_intro() # Show the intro text again
            return # Return to the main game loop
        elif choice == 'q': # If the player wants to quit the game
            fancy_text("\nThanks for playing! Goodbye.")
            exit()
        else: # Invalid choice error handler
            fancy_text("Invalid choice. Please enter R or Q.")

def loot_room():
    """Loot the current room for coins and items."""
    # Keep track of the player's coins, inventory, and health by using global variable
    global coins, inventory, player_health
    
    # Make it so that if you already looted a room, you can't loot it again
    if current_room in game_data["looted_rooms"]:
        fancy_text("You've already looted this room, you can't seem to find anything else.")
        time.sleep(1)
        return ""
    
    # Guaranteed coins
    coins_found = random.randint(2, 5) # Can find between 2 to 5 coins
    coins += coins_found # Add the found coins to the player's total coins
    fancy_text(f"\nFound {coins_found} coins!")
    
    # 35% item chance
    if random.random() <= 0.35:
        # Randomly select an item from the ITEMS dictionary from constants.py
        item = random.choice(list(ITEMS.keys()))
        found = next((i for i in inventory if i["name"] == item), None) # Check if the item is already in the inventory
        if found:
            found["uses"] += 1 # If the item is in the inventory, increment its uses by 1
        else:
            inventory.append({"name": item, "uses": 1}) # Otherwise add the item to the inventory with 1 use
        # Generate description for the item
        fancy_text(f"Among the coins, you discover a {item}! ({ITEMS[item]['description']})")
    
    # 15% Peter the Spider attack chance
    if random.random() <= 0.15:
        damage = random.randint(3, 5) # Random damage between 3 to 5
        player_health -= damage # Deduct the damage from the player's health
        fancy_text(f"\nPeter the Spider jumps out and scratches you! (-{damage} HP)")
        fancy_text(f"He quickly scurries away into the darkness, nowhere to be seen...")
        fancy_text(f"Current HP: {player_health}/100")
    
    # Add the current room to the looted rooms list, so that it can't be looted again
    game_data["looted_rooms"].add(current_room)
    time.sleep(1)
    return ""

def use_item() -> str:
    """Use an item from the player inventory."""
    global player_health, inventory # Keep track of the player's health and inventory by using global variables
    
    # If nothing is in the inventory, show a message and return
    # Because how would you be able to use an item if you don't have any items in your inventory :/
    if not inventory:
        fancy_text("Your inventory is empty!")
        time.sleep(1)
        return ""
    
    # Create a consolidated list of unique items for display
    consolidated_items = {}
    for item in inventory:
        if item["name"] in consolidated_items:
            consolidated_items[item["name"]]["uses"] += item["uses"]
        else:
            consolidated_items[item["name"]] = {"uses": item["uses"], "description": ITEMS[item["name"]]["description"]}
    
    fancy_text("\nAvailable items:") # Display the available items in the inventory
    # Loop through all the items in inventory and print them with their uses and descriptions
    for i, (name, props) in enumerate(consolidated_items.items(), 1):
        fancy_text(f"{i}. {name} x{props['uses']} - {props['description']}")
    
    try:
        choice = int(input("Select item (number) or 0 to cancel: "))
        # If the user inputs 0, cancel the item usage
        if choice == 0:
            return ""
        
        # Get the selected item name from the consolidated list
        selected_name = list(consolidated_items.keys())[choice-1]
        
        # Find the first inventory entry with this name
        selected = next(item for item in inventory if item["name"] == selected_name)
        item_name = selected["name"]
        
        # Handle effects
        if item_name == "Bandage":
            if player_health == 100: # If the player is already at full health, show a message and return
                fancy_text("You are already at full health!")
                return ""
            else:
                player_health = min(100, player_health + 10) # Plus 10 HP for each bandage used
                fancy_text(f"Used Bandage! HP restored to {player_health}/100")
        elif item_name == "Flashlight":
            # If the player is in a dark room, light it up
            if current_room in game_data["dark_rooms"]:
                fancy_text("You light up the room temporarily!")
                game_data["dark_rooms"].remove(current_room) # Un-dark the room
            else:
                # If the player is not in a dark room, show error message
                fancy_text("No need to use this in a lit room!")
                return ""
            
        # The lockpick is currently useless because I wasn't able to implement a locked door event at this stage
        # In later versions they will be very useful, but for now they are just a placeholder

        elif item_name == "Lockpick":
            if random.random() <= 0.5:
                fancy_text("The lock clicks open!")
            else:
                fancy_text("The lockpick broke!")
        
        # Decrement uses after the player uses the item
        selected["uses"] -= 1
        # Remove item title from inventory completely if they have all been used up
        if selected["uses"] <= 0:
            inventory.remove(selected)
            fancy_text(f"{item_name} has been used up!")
            
    except (ValueError, IndexError):
        fancy_text("Invalid selection!") # If the user inputs an invalid number, show an error message
    
    time.sleep(1)
    return ""

# This function will be used every single time the player moves forward or backward.
# Because it displays critical information about the player's current status.
def show_status(): # Show the player's current status, including room number, health, coins, and inventory
    """Display the player's current progress in the game."""
    # The option bar right here
    fancy_text(f"Room: {current_room:03d} | HP: {player_health}/100 | Coins: {coins}")
    # Show the player inventory
    if inventory: # If there are anything in the inventory
        # Group identical items for display
        item_counts = {}
        # Loop through the inventory and count the number of uses for each item
        # This is the inventory display that will show up on the user interface
        # Not to be confused with the one from the use_time function, which is displayed when the player uses the Use Item function
        for item in inventory:
            name = item["name"]
            item_counts[name] = item_counts.get(name, 0) + item["uses"]
        fancy_text("Inventory: " + ", ".join([f"{name} x{count}" for name, count in item_counts.items()]))
```
**main.py**

Last but not least, **main.py**, containing the main code for room handling and the user interface.
```python
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
```
### What Was New In Sprint 2
Massive changes were implemented in sprint 2. First of all, **entities!** That's right, entities are now here to hunt down the players. Having 5 of them at this stage, entities will be the only obstacle that players face throughout the game. Although a proper counter-attack function hasn't been developed yet, meaning that the players will have to suck it up for whatever damage they took from the entities, this brings me onto the next point: **ITEMS!!!** That's right, items are now introduced to the game as collectibles, so while you can't avoid any damage by entities, you can collect **bandages** across rooms to heal yourself up. Now, you may ask, how do you get bandages? The answer is SIMPLE. The looting function! In this update, not only do you get to move forwards and backwards, you are also given options to loot a room, and use items that you looted. Pretty cool right? But that doesn't even come close to the legendary **replay system!** You saw it right, from now on, once the player dies or beats the game, they are automatically given the options to either replay the game from the start or quit the game. Lastly, room events are now a thing! The system will randomly select rooms to be either normal or dark rooms. And in dark rooms, entities spawn more frequently. Overall, that's it!

## **End of Sprint 2 - Review Questions**

### Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.
* Refer to specific criteria or expectations outlined in your requirements document.

In terms of the functional requirements, I think I've nailed it perfectly. The system can successfully and efficiently fetch data to the players by using code, and each section of the code complies with that in the data retrieval process. The user interface, although more complicated than the Sprint 1 Prototype, is still fairly easy to understand and use, given the organized instructions and clear error messages provided. The system also displays a substantial amount of information to the player, such as their room number, health, coins, and inventory, satisfying the data display section of the functional requirements.

In terms of the non-functional requirements, I did a great job at it as well. For performance, the system produces zero lag, doesn't crash the system, and is absolutely a thrill to use in all aspects. In terms of reliability, the program had demonstrated absolutely zero bugs, and doesn't corrupt any data that's stored in lists or dictionaries, providing the users with the most reliable information. Lastly, in terms of usability and accessibility, I can perfectly assure you that the program is very usable and accessible. The option bar provides the key input options for all the required inputs, and instructions as well as error messages are provided for every single required input, making it extremely easy to understand the core mechanics of the game and play it well.

### Analyse the performance of your program against the key use-cases you identified.
* Discuss whether the program behaves as expected and handles input/output as planned.

The program behaves perfectly as expected, and every single function works perfectly smooth and flawless thanks to my hours of research and dedication. Every single key and input works as well. Moreover, my program perfectly fits the standards as shown in my use case diagrams. At the current stage, I am extremely glad that I have managed to expand on my first prototype for the game without breaking any of the game's core mechanics, since this prototype was a huge step forward in terms of my progress for the game. Currently, all movement controls work as expected, the use item function will work seamlessly, the loot room function is fair and flawless, and everything else about the game just perfectly works, giving it the undeniable charm and charisma that it owns.

### Assess the quality of your code in terms of readability, structure, and maintainability.
* Consider naming conventions, use of functions, comments, and overall organisation.

At this point in time, I would argue that my code is very structured, since each section of the code have their own Python files that would be integrated into **main.py**, the file responsible for the main user interface. These include **constants.py,** the file responsible for all the dictionaries and constants, and **functions.py**, the file responsible for all the functions. I have created constants.py as a way to clean and organise things up in functions.py, since if I didn't create it, then functions.py would literally be way to unreadable and confusing, since code comments also took up like half the space in there. The code is mainly very readable, since I have effectively integrated useful code comments in every single file of the game, and the user would understand how it works logically just by reading it if they have any coding experience at all. This is all true except for a function in **functions.py** called **weighted_random_choice**, which is so complicated that I literally had to write multiple lines of DocStrings just to explain the code and give an insight into how it works. Lastly, the code is also very maintainable, since functions can be added any time in functions.py, and the dictionaries in constants.py can always be expanded.

### Explain the improvements that should be made in the next stage of development.
* Include both feature enhancements and refinements to code quality or structure.

```
In the next stages of development, I will start to add monsters, obstacles, items, challenges and special room events, as well as implementing Levin’s Shop at Room 052. At the time of writing, I am very afraid that I will not be able to do a good job at this project because of the sheer amount of complexity involved according to my plans. However, as a somewhat experienced Python programmer who has also spent time researching about Doors in his spare time, I believe that I would be able to manage the development of this effectively. My next sessions will include the implementation of much more functions, specifically regarding event handling. I will also begin working on the development of a looting system, and puzzles that will appear at major rooms such as Room 050 and 100.
```
This, was what I wrote for the same question in Sprint 1's review section. Looking back, most things listed in this paragraph has been said but not done, simply because of the sheer pain and trauma I had to go through just to find inspirations for the program and solutions for errors in my code. Not only that, what I planned may have sounded easy, but in fact they were extremely difficult. The concept of Levin's Shop alone took me around 3 hours to attempt a build, and later it still wasn't up to my standards, making me abandoning it. Therefore, I simply decided to leave Sprint 2 as the way it is for now so I can finally take a good, long break. In my future stages of development, anything I wrote above will definitely be finished. Also, I have left code comments in **constants.py** that may be useful in guiding me through the future development of my game. Who knows?

# **Sprint 3**

## **Design**
For the **Player** aspect of my game, there will only be one singular class as the Player, and that will be the player (a bit confusing but what I'm saying is that my game isn't like the other games where the players can be multiple characters/child classes such as **Solider, Soldier, Warrior, Fighter** or **Archer**, the real life player of the game can only play the game as a singular class called **Player**, meaning that there is only one character for this game).

Also, I must admit that my plan could be way too complicated. Since I have to program the entities' behaviours with only around a week left, I might not be able to finish programming for all these entities.

### **Enemy Roster**
**NOTE:** None of the entities below can spawn in the following rooms: 000, 049, 050, 051, 052, 099, 100
| Entity | Behaviour | Counters |
|-|-|-|
| Tralalero Tralala | Has a very low chance to spawn in a lit room, and a much higher chance to spawn in a dark room. The console will remind the player that he is behind them, and the player will have to react very quickly to him in order for him to go away. | Enter "A" key to look at Tralalero Tralala, making him scream and leave |
| Bombardino Crocodilo | Can spawn in lit rooms. Will rush through the rooms, and the player have to react quickly to hide in a nearby closet in order to survive from him. Will also make the next room dark. | Enter "H" key to hide |
| Brr Brr Patapim | Can spawn in lit rooms. When he spawns, the current room number the player is in will be replaced by question marks, and when the player tries to progress, they will be met with either 2 or 3 possible rooms, with only one of them being the real door and the other 2 being fake, having Brr Brr Patapim in them. Players cannot go back to the previous room, and they must choose which door they wish to enter. | Players should always memorise the number of their room prior to entering the next room, since the real door should have the number following the current room on them. This would allow the player to know for which door leads to the next room. |
| Tung Tung Tung Sahur | Can only spawn if the player enters a closet. If the player hides in a closet for way too long, Tung Tung Tung Sahur will damage them and kick them out of the closet, not being able to enter again. | Players should never hide in a closet for too long. If they get out just in time, Tung Tung Tung Sahur will never be able to get them. |
| Boneca Ambalabu | Can spawn in any room except the ones listed above. The player must react quickly to avoid looking at Boneca Ambalabu. Not reacting quickly will result in a massive loss of health. | Press A to look down |

### **Items Roster**
| Items | Effects |
| - | - |
| Bandage | Heals the user 10 HP (health) |
| Flashlight | Lets the player see in dark rooms |
| Lockpick | Useful against locked doors |
| Crucifix | Can repel some enemies (Sprint 3) |

## UML Class Diagram
![UML](/images/UML%20Class%20Diagram.png) 

## **End of Sprint 3 - Review Questions**

### Evaluate how effectively your project meets the functional and non-functional requirements defined in your planning.
* Refer to specific criteria or expectations outlined in your requirements document.

Throughout the entire development process of this project, I think I have always, always achieved decent standards in terms of both functional and non-functional requirements. During the development of Sprint 3, I have always prioritised the functional and non-functional requirements. In Sprint 3, the system continues to be able to retrieve data for the players even though they have underwent massive changes due to the introduction of classes. Also, despite adding a ton of new features, I still believe that my user interface is simple and understandable enough for an average user to understand it. Furthermore, the system can successfully display data to the user, such as when entities appear in a room, the system can tell the player what's happening and give users clear instructions on how to handle them.

In terms of the non-functional requirements, the same can pretty much also be said. The system works clear and efficient enough to excel in the performance factor. Also, the system successfully displays reliable information, because the system doesn't carry any bugs (at least not to the extent as I can tell from my limited playtesting) and successfully receives player input, such as when during entities and obstacles spawn. Lastly, the system is also perfectly usable and accessible, since it's designed to be a game that anyone on any device can play. Not only is the system easy-to-run-and-understand, it's also quite accessible because it can literally be used within Visual Studio Code.

### Analyse the performance of your program against the key use-cases you identified.
* Discuss whether the program behaves as expected and handles input/output as planned.

The program behaves very much as expected and can clearly handle player input and system output as planned. One of the best examples of this is the entity system. When Bombardino Crocodilo is coming, the player can use the H key to hide from him, and the system will then output their survival message and deal no damage loss to the player. However, if the player uses any other key to attempt survival from Bombardino, then the program can INSTANTLY detect that, then tell the player that they have selected the wrong key, which meant they didn't hide from Bombardino, therefore dealing a substantial amount of damage to the player. Also, if the player doesn't respond at all, then the program can use Python's inbuilt **Time** module to detect their inactivity, therefore also dealing damage to the player since they didn't respond. Nevertheless, I gotta admit my system is very well structured when it comes to input and output handling! Lastly, the performance of my program still fits within the criteria of my expectations as listed in the use case diagrams.

### Assess the quality of your code in terms of readability, structure, and maintainability.
* Consider naming conventions, use of functions, comments, and overall organisation.

Okay, so Sprint 3 is a MASSIVE update as anyone can tell. The code length in the major file **functions.py** has almost doubled its previous amount in Sprint 2, and this was all because of the tons of things I added in Sprint 3. The constants.py file now has more descriptive sets and lists, giving more properties to entities and items alike, as well as introducing new sets called **obstacles, puzzles and special rooms** meaning that the new code has essentially became way more complex than before. However, I've tried to format the code as neat as possible, making it still look readable and can easy be configured any time. In functions.py, I have tried to organise my code by sorting them into 3 classes: **Player, Room** and **Game.** The player class contains all the player-related functions such as item usage and inventory controls. The room class contains the basic code for room configuration as well as entity and obstacle spawning. I feel like that although I have almost 700 lines of code in functions.py at the stage of Sprint 3, the code is still very structured and maintainable since they have been greatly optimized as well as sorted into classes, making changes easier. (700 lines of code is really nothing for a game like this since I've worked on way bigger projects with friends before, even at some point becoming the programmer of a Roblox game in a collaborative project). In Sprint 3, **main.py** has barely changed, so I still consider it as very readable, structured and maintainable. Lastly, I've used plenty of code comments and DocStrings for each function, although making it look more messy and clustered, it really does help with explaining the code, it really does.

### Explain the improvements that should be made in the next stage of development.
* Include both feature enhancements and refinements to code quality or structure.

I can say that I have fulfilled most of my plans in Sprint 3. In this Sprint, I have successfully implemented many advanced functions into the program, such as obstacles alongside with updates for the current existing entities, as well as puzzles every 25 rooms. Also, the Levin's shop, needless to say, is an excellent feature that I've managed to add into the system, with lots of work and research as well as help from all people alike. I've also reworked the game's introduction and outro, making them more atmospheric and exciting, and added more room descriptions because I felt like 5 was way too less. Anyways, gotta say I did a great job in Sprint 3. However, in Sprint 4, I might begin the polishing process, with refinements on several sections of the code, as well as thorough bugfixing and playtesting, then updating anything that could be deemed unfun or unfair for the player. In shorter terms, Sprint 4 will just be updates on Sprint 3's code with major polishing, tiny changes in the code and thorough bugfixing. So happy!!! 

# **Sprint 4**

## **Design**
## Identify Potential Enhancements
In Sprint 4, there are still some potential enhancements I could add to my program even though there are already a ton of features I've added in Sprint 3. Such examples include reworking some entities so that they appear more threatening and reckless when the players encounters them. I could also make the first 5 rooms immune from any entities, obstacles or room events so players actually have the time to prepare. Also, I have another idea in mind: adding a new entity called **Ballerina Cappuccina**, which will damage the player and send them back to their original room after they go backwards too much. This entity can limit how the player can freely roam around the lobbies, and can also fix some issues surrounding entities. Lastly, I could also add more obstacles and generate more outcomes for them

## Updated Gantt Chart with Milestones

![Gantt](/images/Gantt%20Charts/Updated%20Gantt%20Chart.png)

## Updated Structure Chart with Classes

![Gantt](/images/Structure%20Charts/Updated%20Structure%20Chart.png)

## Peer Evaluation

### Peer 1: Ronen Gupta
| Plus | Minus | Implications |
| - | - | - |
| Nice gameplay flow | Some minor bugs in the text, such as some lines being written in the wrong order | Levin's Shop at Room 052 is very interesting |
| Good use of different enemies and rooms | It is a little repetitive pressing W and L to get coins and going forward but I can understand why | The item "Starlight Jug" is also very interesting
| Many items | | You can survive from entities by just pressing that key without having to press enter afterwards |
| Nice text effects | | Room generation is excellently done |

#### Final Feedback from Ronen Gupta:
A quite good OOP game I must admit, Levin! Text-based and also eerie in a way, presenting the player with a good idea of what to do and expect. It can be a little less repetitive with more variety in gameplay as it is text-based and can be leveraged easier, but it is an excellent effort! Well done, Levin!

### Peer 2: Victor Guo
| Plus | Minus | Implications |
| - | - | - |
| The game performs well, although it is a text-based game, so the performance would generally be better | The character teleports to the next room when damage is taken rather than staying in the room in which damage was dealt | The fancy_text functiion gives the game a unique aesthetic similar to an animated command line |

#### Final Feedback from Victor Guo:
Levin's text-based game "Rooms" integrates many of his requirements that he has outlined, while implementing a fancy_text function to enhance the user experience. When the player takes damage, they are automatically moved to the next room; however, the user may find this illogical and suggest it should be fixed. Overall, a well-crafted game with its own unique aesthetic.

## Evaluation of System

1. **Explain how you could improve your system in future updates. Analyse the impact these updates could have on the user experience.**

To improve my system in future updates, first of all, I could implement new classes that handles different functions within each room that the player enters. Right now, the **Game** class is everything. It basically carries the most important functions within my game, and not to mention that there are a ton of these functions. I could sort out the Game class by separating its functions into mini-classes. Then, I could create more interesting experiences for the player as they explore throughout the rooms. As Ronen Gupta had commented in the peer review, my game is currently way too repetitive and delivers little challenges. This makes me think that I could make my game more challenging and spike up the difficulty meter.

I feel like these changes really wouldn't matter when we go into a player-based perspective. First of all, as long as none of the major functions are impacted by changes that decrease their functionality, I don't think there would be any changes to the game itself if we are just sorting out the background while maintaining the existing functions. Also, if we want to create more interesting experiences for the player and spiking up the difficulty for the game, I don't think players would dislike this change, but rather they would like it, because sure, the difficulty would be ramped up by a lot, making it harder to beat the game, but the game being easy right now is what makes it boring. Adding this change could make the game less repetitive, and actually make it challenging, which is what every game needs.

2. **Evaluate the system in terms of how well it meets the requirements and specifications.**

Overall, I felt like my final product managed to meet my requirements and specifications quite well. I gotta admit that the final product was not up to my expectations, but it's also reasonable because I had severely overestimated my programming skills when I was planning the system flow of the game. Although the system is quite underwhelming with a lot of bugs present, it still was up-tp-par with my requirements and specifications, however. For example, my system can at least send out data to the player, which already satisfies a functional requirement. Not only this, my program is quite simple to understand and use, and requires little equipment in order to run it. My program doesn't crash or freeze the system, and is very optimized as well. There is planned user interaction between objects, and the core features still remain at where they are. Also, a really good trait of my current system is that it can easily handle errors, returning error messages to players whenever they make a mistake. In summary, my program still suits my original requirements and specifications even though it was not up to my previous expectations.

3. **Evaluate your processes in terms of project management.**

As you can see from the Gantt Chart, I have clearly misjudged the difficulty of the **Build and Test** processes of this task. Although Sprint 1 was quite up-to-par with my inital expectations due to the program being quite simple to code thanks to the simplicity of it, everything began to take a dark turn at Sprint 2. The practical process of Sprint 2 was WAY more complicated, and it genuinely robbed me of lots of time due to the long periods of time I have to spend investing and digging into the code, scrolling through thousands of Stack Overflow forums just to develop the program to my expected extent. And when that's finally out of the water, I had to deal with Sprint 3. The theory contents (mainly the review and launch sections) at this point genuinely seemed like a piece of cake to me now, since I could literally get them done in maybe 30 minutes to an hour. What I really was worried about in this stage, the main concern at the top of my head, is the **prac.** As you can see, Sprint 3's **Build and Test** process was around 10000x (not really, just an exaggeration) more difficult than Sprint 2, since I had to add tons of new features into it, and I should've known that if I was struggling this much with Sprint 2, there would be no way I would've even finish Sprint 3 before the due date. That's when the grey thundercloud began to rumble and send lightning strikes in my head. My life literally flashed before my eyes for a second.

But when I actually started Sprint 3 I found out that it's not AS difficult as I expected, because in Sprint 3 we get to work with classes, which allowed me to make my code 10000x (once again an exaggeration) more organized and neat. This actually somehow allowed me to work more efficiently and productively at this code, managing to not spend as long as I had initially predicted in this Sprint. Once we got that done, Sprint 4's **Build and Test** process had went much, much more downhill in terms of difficulty, since when I finished Sprint 3 my program was basically finished. I still did some simple polishing and added some new stuff to it however. And when I finished that, I quickly wrote the final evaluation to finish off the program.

And that, was the story of how I **almost** didn't finish the project before it was due. Pretty cool, right?

**TL; DR:** Sprint 3 sucks, and I feel like my brain aged by 50 years after I finished it.

4. **Gather feedback from at least two peers on meeting of functional and non-functional specifications.**

The PMI tables are up there, so now I'm going to review their reviews and go through each of them thoroughly. Let's start with Ronen Gupta's review.

- **Positives: nice gameplay flow, nice use of enemies and rooms, many items, nice text effects**

    Why thanks Ronen Gupta! I gotta admit that since enemies, items and gameplay matters more than anything in my game, I did spend a lot of time on them, and after I added them I've also done careful playtesting to ensure that everything works to my expectations. I've also received multiple compliments about the text effect, which is also very nice! Thank you all! I gotta admit this text effect works really well for the game, giving players a sense of suspense as they progress throughout the rooms.

- **Negatives: Some minor bugs in the text, a bit too repetitive**

    These negatives matter to me way more than positives, because who would care about the positives more than the negatives unless you are an optimistic person and I'm... not? Maybe? Anyway, to Mr Ronen Gupta, I would like to thoroughly apologize that you did not enjoy my game as much due to these errors. I gotta admit, I am not a professional coder, so it's a bit hard for me to literally havbe to find every single bug in the game, then come up with a solution to fix them. Also, I gotta admit that I've already fixed around 80% of the bugs in the game, and Mr Gupta had just managed to come across the rare 20%. I will definitely fix these bugs in the near future. In terms of repetition, I gotta agree myself, but there's really not much I can do about it since you literally gotta move forward to Room 100 in order to beat the game. That's how the game and the system flow works!

Now let's respond to Victor Guo's review.

- **Positives: The game performs well, although it is a text-based game, so the performance would generally be better**

    I perfectly agree with this statement. All text-based games will generally perform better than GUI games because they contain less assets and don't require computers that display high visual graphics. Otherwise, nothing much to say here.

- **Negatives: The character teleports to the next room when damage is taken rather than staying in the room in which damage was dealt**

    I can perfectly understand. I've faced this bug multiple times before, but I've always made it a goal to try and fix it. I did eventually reach a point of coming up with somewhat a decent solution to fix this issue, however. Besides from that, I perfectly understand this critique from Victor Guo.

Overall, really good reviews from both peers of mine, and I greatly appreciate them for being brutally honest on their reviews. These reviews had managed to make my program even better than before, and also helped me gain a valuable insight into how my game performs and how other people perceive it. It gives me a perfect example of the reception that my game would face when it's released to the broader public. Thanks to these reviews, I can carefully work and fix on the negatives while making the positives even better.