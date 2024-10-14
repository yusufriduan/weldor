import core_logic

option = core_logic.main_menu()

if option == 'load':
    core_logic.os.system('cls')
    
    Username = input("Enter your username: ").strip()
    game_data = core_logic.load_game(Username)
    if game_data:
        core_logic.os.system('cls')
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
        core_logic.get_enter()
        
    else:
        core_logic.os.system('cls')

        print("No saved game found.\nStarting a new game.\n")
        print("Press enter to continue...")
        core_logic.get_enter()
        core_logic.os.system('cls')

        difficulty = core_logic.difficulty()
        secret_word = core_logic.choose_word(difficulty)
        attempts = core_logic.attempts(difficulty)
        
else:
    core_logic.os.system('cls')

    print("Starting a new game.")
    core_logic.get_enter()
    core_logic.os.system('cls')

    Username = input("Enter your username: ").strip()
    core_logic.os.system('cls')

    difficulty = core_logic.difficulty
    secret_word = core_logic.choose_word(difficulty)
    attempts = core_logic.attempts(difficulty)
core_logic.os.system('cls')

# The game commence!
print("You have chosen",difficulty,"difficulty.\nYour guess must be",len(secret_word),"letters long.\nYou have",attempts,"attempts to guess the word.")

for attempt in range(attempts):
    guess = core_logic.get_guess()
    if guess == "exit":
        print("Exiting the game.\nGoodbye!")
        e=core_logic.get_enter()
        core_logic.os.system('cls')
        exit()

    if len(guess) != len(secret_word):
        print("Your guess must be",len(secret_word),"letters long.")
        continue

    if guess == secret_word:
        print("Congratulations!\nYou've guessed the word correctly!")
        n = input("Enter enter to continue...")
        core_logic.os.system('cls')

        #Update the leaderboard
        core_logic.update_leaderboard(Username, difficulty, attempts - attempt) # Using attempts - attempt to get more accurate number of tries

        # Check if file exist and remove the save file (if exist)
        if core_logic.os.path.exists('saves/{}_checkpoint.json'.format(Username)):
            core_logic.os.remove('saves/{}_checkpoint.json'.format(Username))
            print("Save game file removed.\nPress enter to continue.")
            e = core_logic.get_enter()
            core_logic.os.system('cls')
            core_logic.main_menu()
        else:
            core_logic.main_menu()
    
    feedback = core_logic.give_feedback(secret_word, guess)
    print("Feedback:",feedback)

    # Autosaves the guesses
    core_logic.save_game(Username, difficulty, secret_word, attempts - attempt -1, guess)
core_logic.os.system('cls')

# If User ran out of attempts
if attempt == attempts:    # type: ignore
   print("Sorry, you've used all your attempts.\nThe correct word was ",secret_word)
   e = core_logic.get_enter()
   core_logic.os.system('cls')

   # Remove the save game file
   core_logic.os.remove('saves/{}_checkpoint.json'.format(Username))
   print("Save game file removed.")
   core_logic.main_menu()