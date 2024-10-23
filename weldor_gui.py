import tkinter as tk
from tkinter import messagebox
import core_logic
import random

class WeldorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Weldor")
        self.master.geometry("400x300")

        # Create frames
        self.title_frame = tk.Frame(self.master)
        self.title_frame.pack(fill="x")

        self.difficulty_frame = tk.Frame(self.master)
        self.difficulty_frame.pack(fill="x")

        self.game_frame = tk.Frame(self.master)
        self.game_frame.pack(fill="both", expand=True)

        # Create title label
        self.title_label = tk.Label(self.title_frame, text="Weldor", font=("Times New Roman", 24))
        self.title_label.pack(pady=10)

        # Create difficulty selection
        self.difficulty_label = tk.Label(self.difficulty_frame, text="Select Difficulty:")
        self.difficulty_label.pack(side="left")

        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("easy")  # default value

        self.easy_radio = tk.Radiobutton(self.difficulty_frame, text="Easy", variable=self.difficulty_var, value="easy")
        self.easy_radio.pack(side="left")

        self.medium_radio = tk.Radiobutton(self.difficulty_frame, text="Medium", variable=self.difficulty_var, value="medium")
        self.medium_radio.pack(side="left")

        self.hard_radio = tk.Radiobutton(self.difficulty_frame, text="Hard", variable=self.difficulty_var, value="hard")
        self.hard_radio.pack(side="left")

        # Create game widgets
        self.word_label = tk.Label(self.game_frame, text="", font=("Arial", 24))
        self.word_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.game_frame, width=20)
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(self.game_frame, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.feedback_label = tk.Label(self.game_frame, text="", font=("Arial", 18))
        self.feedback_label.pack(pady=10)

        # Initialize game variables
        self.difficulty = self.difficulty_var.get()
        self.secret_word = core_logic.choose_word(self.difficulty)
        self.attempts = core_logic.attempts(self.difficulty)
        self.guesses = []

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        if len(guess) != len(self.secret_word):
            self.feedback_label.config(text="Your guess must be {} letters long.".format(len(self.secret_word)))
            return

        feedback = core_logic.give_feedback(self.secret_word, guess)
        self.feedback_label.config(text=feedback)

        if guess == self.secret_word:
            self.feedback_label.config(text="Congratulations!\nYou've guessed the word correctly!")
            self.guess_button.config(state="disabled")
        else:
            self.attempts -= 1 # type: ignore
            if self.attempts == 0:
                self.feedback_label.config(text="Sorry, you've used all your attempts. The correct word was {}".format(self.secret_word))
                self.guess_button.config(state="disabled")

root = tk.Tk()
my_gui = WeldorGUI(root)
root.mainloop()