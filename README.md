# Rock Paper Scissors Game
**Overview**
This project is a Python implementation of the classic Rock Paper Scissors game. It offers an interactive command-line interface for the user to play against the computer. The program tracks the score, handles input validation, and allows the player to end the game gracefully.

**Architecture**
The program follows a simple yet effective structure to ensure smooth gameplay and maintainability. The core components include:

Game Loop: The main loop that continuously runs until the player decides to end the game.
Input Handling: A function to capture and validate player inputs.
Random Choice Generation: Utilizes Python's random.choice to simulate the computer's decision.
Game Logic: A set of conditional statements to determine the outcome of each round.
Score Management: Variables to keep track of the player's and computer's scores.
End Game Handling: A mechanism to terminate the game and display final scores.

**How to Play**
Start the Game: Run the script to start the game.
Make a Choice: When prompted, enter your choice of 'Rock', 'Paper', or 'Scissors'. You can also type 'End' to finish the game.
View Results: The game will display the result of each round (win, lose, or tie) and update the scores.
End the Game: Type 'End' to stop playing and see the final scores.

**Code Details**

The game is implemented in a single Python script with a simple loop to handle user input and determine the winner of each round. Here is a brief overview of the main parts of the code:

Input Handling: Takes user input and processes it.
Random Choice: Uses Python's random.choice method to select the computer's move.
Game Logic: Determines the winner of each round based on the rules of Rock Paper Scissors.
Score Keeping: Maintains and updates scores for both the player and the computer.
Exit Condition: Allows the player to end the game and view final scores.
