# **Weldor Game**

## **Overview**
Weldor is a word-guessing game **and huge-ly inspired from Wordle; The New York Times game** where the user has to guess a secret word by suggesting letters. The game has three difficulty levels: easy, medium, and hard, with varying numbers of attempts to guess the word.

## **Features**
- Difficulty Levels: Easy, Medium, and Hard, with increasing difficulty and decreasing number of attempts.
- Word Guessing: User has to guess a secret word by suggesting letters.
- Feedback: The game provides feedback on the user's guess, indicating correct and incorrect letters.
- Autosave: The game autosaves the user's progress, allowing them to resume from where they left off.
- Leaderboard: The game updates a leaderboard with the user's score, including their username, difficulty level, and number of attempts.

## **Implementation**
The game is implemented in Python, using the following modules:

1. random for generating random words
2. json for saving and loading game data
3. msvcrt for reading single characters without echoing to the console (Windows only)
4. tty and termios for reading single characters without echoing to the console (Unix-based systems only)
5. os for file operations and system commands

## **How to Play**
1. Run the game by executing the weldor.py file.
2. Choose a difficulty level and start a new game or load a saved game.
3. Guess a letter, and the game will provide feedback on your guess.
4. Keep guessing until you correctly guess the word or run out of attempts.
5. The game will update the leaderboard with your score.

### **Note**
This is a basic implementation of the Weldor game, and there is room for improvement and expansion.
