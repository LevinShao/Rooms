# **11ASE Assessment Task 2**
## **By Levin Shao**
=======================================================================
## **Sprint 1**
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