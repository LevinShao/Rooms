# **11ASE Assessment Task 2**
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
2. System displays updated door number (e.g. "Room 024"), room description, and health status.
3. If an event triggers (e.g. monster spawning), system retrieves and displays the event details (e.g. "You hear Rush charging at you in the distance! Press H to hide!").

&nbsp;&nbsp;&nbsp;&nbsp; **Alternative Flow:**

1. Player presses H for help.
2. System repeats current room/status without progression.

&nbsp;&nbsp;&nbsp;&nbsp; **Postconditions:** Player sees real-time updates of door number, health, and event context.

### Use Case 2: User Interface

&nbsp;&nbsp;&nbsp;&nbsp; **Actor:** Player

&nbsp;&nbsp;&nbsp;&nbsp; **Preconditions:** Python environment is fully set up; game is launched in code terminal.

&nbsp;&nbsp;&nbsp;&nbsp; **Main Flow:**
1. Player uses W/S to navigate the rooms, and the system processes input instantly.
2. During events, player uses A/D for actions, and the system validates input.
3. Player presses Q, leading to the system exiting gracefully after confirmation ("Quit? Y/N").

&nbsp;&nbsp;&nbsp;&nbsp; **Alternative Flow:**

1. Player inputs an invalid command/key during interaction (e.g. Z)
2. System ignores input and displays controls reminder ("Use W or S!").

&nbsp;&nbsp;&nbsp;&nbsp; **Postconditions:** Player interacts with the game seamlessly via CLI; invalid inputs never crash the game.

### Use Case 3: Data Display

&nbsp;&nbsp;&nbsp;&nbsp; **Actor:** Player

&nbsp;&nbsp;&nbsp;&nbsp; **Preconditions:** Player is mid-game; an event occurs.

&nbsp;&nbsp;&nbsp;&nbsp; **Main Flow:**
1. System outputs event description (e.g. "Door 056: The lights flicker...").
2. Any critical information is highlighted (e.g. "⚠️ Health: 10/100").
3. Success/failure outcomes are clear (e.g. "You solved the puzzle! +20 HP").

&nbsp;&nbsp;&nbsp;&nbsp; **Alternative Flow:**
1. Player health goes down to 0 and they die in-game.
2. The system displays loss screen and prompts restart.

&nbsp;&nbsp;&nbsp;&nbsp; **Postconditions:** Information is formatted for clarity; urgent statuses like low health are emphasized.

## **Design**

### Game Introduction Storyboard
![Game Intro Storyboard](/images/Storyboards/Game%20Intro%20Storyboard.png)

### Normal Room Storyboard
![Normal Room Storyboard](/images/Storyboards/Normal%20Room%20Storyboard.png)

### Entity Room Storyboard
![Entity Room Storyboard](/images/Storyboards/Entity%20Room%20Storyboard.png)

### Game Outro Storyboard
![Game Outro Storyboard](/images/Storyboards/Game%20Outro%20Storyboard.png)

### Level 0 Data Flow Diagram/Context Diagram
![Level 0 DFD](/images/DFDs/Level%200%20DFD.png)

### Level 1 Data Flow Diagram
![Level 1 DFD](/images/DFDs/Level%201%20DFD.png)

### Gantt Chart
![Gantt Chart](/images/Gantt%20Chart.png)