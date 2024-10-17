import random
import os
import json
import msvcrt

def choose_word(level):
    word_list = {
        'easy' : ['chair', 'start', 'world', 'peach', 'wears'],
        'medium' : ['compare', 'reptile', 'bargain', 'traders', 'dynasty'],
        'hard' : ['franchised', 'facetious', 'flabbergasted', 'amendment', 'accumulate']
    }
    return random.choice(word_list[level])

def get_enter():
        while True:
            char = msvcrt.getch()
            if char == b'\r': #Enter key
                return
            else:
                print('', end='\r')  # overwrite the input with a blank space
    
def get_guess():
    return input("Enter your guess: ").strip().lower()

def give_feedback(secret, guess):
    feedback = ['_'] * len(secret)
    guess_counts = {}
    secret_counts = {}

    # First pass: Check for correct possitions
    for i in range(len(secret)): # i is the letter guessed by the user
        if guess[i] == secret [i]:
            feedback[i] = guess [i]
        else:
            # count the letters for second pass
            guess_counts[guess[i]] = guess_counts.get(guess[i],0)
            secret_counts[secret[i]] = secret_counts.get(secret[i],0) + 1

    # Second pass: Check for correct letters in incorrect placement
    for i in range(len(secret)): # i is the letter guessed by the user
        if feedback[i] == '_': # '_' is for letters not exists in the answer
            if guess[i] in secret_counts and secret_counts[guess[i]] > 0:
                feedback[i] = '*' # '*' is means the letter is not in the right position
                secret_counts[guess[i]] -= 1
    return ''.join(feedback)

def save_game(Username, difficulty, secret_word, attempts, guesses):
    game_data = {
        'username':Username,
        'difficulty': difficulty,
        'secret_word': secret_word,
        'attempts': attempts,
        'guesses': guesses
    }
    # Define directory and filename for game file
    save_dir = 'saves'
    save_file = '{}_checkpoint.json'.format(Username)

    # Create the directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    #saves file for this case will be "C:\Users\yusuf\OneDrive_MMU\Foundation\1st trimester\Assignment\Program design project\saves"
    full_path = os.path.join(save_dir,save_file)

    # Open the file and dump the game data
    with open(full_path, 'w') as f:
        json.dump(game_data, f, indent=4)

def load_game(Username):
    save_dir = 'saves'
    save_file = '{}_checkpoint.json'.format(Username)

    full_path = os.path.join(save_dir, save_file)

    # Check if save game exist
    if os.path.exists(full_path):
        with open(full_path, 'r') as f: # 'r' is stands for read mode
            game_data = json.load(f)
            if 'username' in game_data and 'difficulty' in game_data and 'secret_word' in game_data and 'attempts' in game_data and 'guesses' in game_data:
                return game_data
    else:
        return None

#For leaderboard data
def update_leaderboard(Username, difficulty, attempts):
    leaderboard_file = "leaderboard.txt"

    # Create the file if it doesn't exist
    if not os.path.exists(leaderboard_file):
        with open(leaderboard_file, "w") as f:
            f.write("{:<20}\t{:<10}\t{:<10}\n".format("Username", "Difficulty", "Attempts"))

    # Write the new score to the file
    with open(leaderboard_file, "a") as f:
        f.write("{:<20}\t{:<10}\t{:<2}\n".format(Username, difficulty, attempts))

    print("Leaderboard updated successfully!")

# Display leaderboard
def display_leaderboard():
    leaderboard_file = "leaderboard.txt"
    with open(leaderboard_file, 'r') as f:
        print(f.read())
    return(None)

# Display menu
def main_menu():
    print("----------------------------------------")
    print("Welcome to Weldor!\n")
    print(" 1. Load Data\n 2. Start New Game\n 3. Leaderboard\n 4. Exit")
    print("----------------------------------------")

        # Get the user's choice and validate the user's choice
    while True: # True means while user is not choosing either load or new yet
        option = input("Enter your response (load or new or leaderboard): ").lower()
        if option in ['new','load']:
            return option
        elif option == 'leaderboard':
            os.system('cls')
            print("-----------------------------------------------------")
            display_leaderboard()
            print("-----------------------------------------------------")
            print("Press enter to continue.")
            get_enter()
            os.system('cls')
            continue
        elif option == 'exit':
            os.system('cls')
            print("Exiting the game. Goodbye!")
            print("Press enter to exit")
            get_enter()
            os.system('cls')
            exit()
        else:
            print("Please choose either new game or load your progress.")
    
option = main_menu()

if option == 'load':
    os.system('cls')
    
    Username = input("Enter your username: ").strip()
    game_data = load_game(Username)
    if game_data:
        os.system('cls')
        print("Welcome back", Username, "! \n")
        difficulty = game_data['difficulty']
        secret_word = game_data['secret_word']
        attempts = game_data['attempts']
        guesses = game_data['guesses']
        print("Last saved data")
        print("Difficulty is", difficulty)
        print("Attempts left is", attempts)
        print("Last guessed word is", guesses,"\n")
        print("Press enter to continue...")
        get_enter()
        
    else:
        os.system('cls')

        print("No saved game found.\nStarting a new game.\n")
        print("Press enter to continue...")
        get_enter()
        os.system('cls')

        print("----------------------------------------")
        print("Select Difficulty Level\n")
        print(" 1. Easy\n 2. Medium\n 3. Hard")
        print("----------------------------------------")

        #Keep looping until user choose the difficulty
        while True: # True means while user is not choosing any difficulty yet
            difficulty = input("Enter your difficulty: ").lower()
            if difficulty in ['easy','medium','hard']:
                break

            # Auto-detect difficulty level if user enters a number
            elif difficulty.isdigit():
                difficulty_level = int(difficulty)
                if difficulty_level == 1:
                    difficulty = 'easy'
                    break
                elif difficulty_level == 2:
                    difficulty = 'medium'
                    break
                elif difficulty_level == 3:
                    difficulty = 'hard'
                    break
                elif difficulty_level not in [1, 2, 3]:
                    print("Sorry what number are you typing again?")

            else:
                print("Sorry I understand you're having difficulty to type properly.\nPlease type your difficulty. (easy, medium or hard): ")
    
        secret_word = choose_word(difficulty)
    
    # Different attempts based on difficulty
    if difficulty == 'easy':
        attempts = 4
    elif difficulty == 'medium':
        attempts = 5
    else:
        attempts = 6
        
else:
    os.system('cls')

    print("Starting a new game.")
    get_enter()
    os.system('cls')

    Username = input("Enter your username: ").strip()
    os.system('cls')

    print("----------------------------------------")
    print("Select Difficulty Level\n")
    print(" 1. Easy\n 2. Medium\n 3. Hard")
    print("----------------------------------------")

    #Keep looping until user choose the difficulty
    while True:
        difficulty = input("Enter your difficulty: ").lower()
        if difficulty in ['easy','medium','hard']:
            break
            
        # Auto-detect difficulty level if user enters a number
        elif difficulty.isdigit():
            difficulty_level = int(difficulty)
            if difficulty_level == 1:
                difficulty = 'easy'
                break
            elif difficulty_level == 2:
                difficulty = 'medium'
                break
            elif difficulty_level == 3:
                difficulty = 'hard'
                break
                break
            elif difficulty_level not in [1, 2, 3]:
                print("Sorry what number are you typing again?")

        else:
            print("Sorry I understand you're having difficulty to type properly.\nPlease type your difficulty. (easy, medium or hard): ")

    # Different attempts based on difficulty
    if difficulty == 'easy':
        attempts = 5
    elif difficulty == 'medium':
        attempts = 5
    else:
        attempts = 4
    
    secret_word = choose_word(difficulty)
os.system('cls')

# The game commence!
print("You have chosen",difficulty,"difficulty.\nYour guess must be",len(secret_word),"letters long.\nYou have",attempts,"attempts to guess the word.")

for attempt in range(attempts):
    guess = get_guess()
    if guess == "exit":
        print("Exiting the game.\nGoodbye!")
        e=get_enter()
        os.system('cls')
        exit()

    if len(guess) != len(secret_word):
        print("Your guess must be",len(secret_word),"letters long.")
        continue

    if guess == secret_word:
        print("Congratulations!\nYou've guessed the word correctly!")
        n = input("Enter enter to continue...")
        os.system('cls')

        #Update the leaderboard
        update_leaderboard(Username, difficulty, attempts - attempt) # Using attempts - attempt to get more accurate number of tries

        # Check if file exist and remove the save file (if exist)
        if os.path.exists('saves/{}_checkpoint.json'.format(Username)):
            os.remove('saves/{}_checkpoint.json'.format(Username))
            print("Save game file removed.\nPress enter to continue.")
            e = get_enter()
            os.system('cls')
            main_menu()
        else:
            main_menu()
    
    feedback = give_feedback(secret_word, guess)
    print("Feedback:",feedback)

    # Autosaves the guesses
    save_game(Username, difficulty, secret_word, attempts - attempt -1, guess)
os.system('cls')

# If User ran out of attempts
if attempt == attempts:    # type: ignore
   print("Sorry, you've used all your attempts.\nThe correct word was ",secret_word)
   e = get_enter()
   os.system('cls')

   # Remove the save game file
   os.remove('saves/{}_checkpoint.json'.format(Username))
   print("Save game file removed.")
   main_menu()