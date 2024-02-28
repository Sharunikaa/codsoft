import tkinter as tk
import random

player_score = 0
computer_score = 0

def get_winner(player_choice):
    global player_score, computer_score
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        player_score += 1
        return "You win! Computer chose " + computer_choice
    else:
        computer_score += 1
        return "You lose! Computer chose " + computer_choice

def play_game(choice):
    result = get_winner(choice)
    result_label.config(text=result)
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create labels
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 18))
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Select your move:", font=("Helvetica", 12))
instruction_label.pack()

# Create buttons
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_game('Rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_game('Paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_game('Scissors'))
scissors_button.pack(pady=5)

# Create result and score labels
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Player: {player_score}  Computer: {computer_score}", font=("Helvetica", 12))
score_label.pack()

# Run the main event loop
root.mainloop()
