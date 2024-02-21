import tkinter as tk
from PIL import Image, ImageTk
import random

# Function to determine the winner
def determine_winner(user_choice):
    global user_wins, computer_wins, draws, games_played
    computer_choice = random.randint(0, 2)
    computer_label.config(image=choice_images[computer_choice])
    computer_label.image = choice_images[computer_choice]

    if user_choice == computer_choice:
        result_label.config(text="It's a Draw", fg="blue")
        draws += 1
    elif (user_choice - computer_choice) % 3 == 1:
        result_label.config(text="You Win!", fg="green")
        user_wins += 1
    else:
        result_label.config(text="You Lose!", fg="red")
        computer_wins += 1
    
    games_played += 1
    update_scoreboard()

# Function to update the scoreboard
def update_scoreboard():
    scoreboard_label.config(text=f"Games Played: {games_played}  |  Your Wins: {user_wins}  |  Computer Wins: {computer_wins}  |  Draws: {draws}")

# Function to handle button clicks
def button_click(choice):
    user_label.config(image=choice_images[choice])
    user_label.image = choice_images[choice]
    determine_winner(choice)

# Function to reset the scores
def reset_scores():
    global user_wins, computer_wins, draws, games_played
    user_wins = 0
    computer_wins = 0
    draws = 0
    games_played = 0
    update_scoreboard()

# Main GUI window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg="lightblue")

# Options
options = ["rock.png", "paper.png", "scissors.png"]

# Load images
choice_images = [ImageTk.PhotoImage(Image.open(option)) for option in options]

# Labels
scoreboard_label = tk.Label(root, text="", font=("Helvetica", 12), bg="lightblue", fg="black")
scoreboard_label.pack(pady=10)

user_label = tk.Label(root, text="You: ", font=("Helvetica", 10), bg="lightblue", fg="black")
user_label.pack()

computer_label = tk.Label(root, text="Computer: ", font=("Helvetica", 10), bg="lightblue", fg="black")
computer_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="lightblue")
result_label.pack(pady=10)

# Buttons
buttons_frame = tk.Frame(root, bg="lightblue")
buttons_frame.pack()

buttons = []
for i, option in enumerate(options):
    button = tk.Button(buttons_frame, text=option.capitalize(), font=("Helvetica", 12), width=10, command=lambda i=i: button_click(i))
    button.pack(side=tk.LEFT, padx=10, pady=10)
    buttons.append(button)

# Reset button
reset_button = tk.Button(root, text="Reset Scores", font=("Helvetica", 10), width=15, command=reset_scores)
reset_button.pack(pady=10)

# Initialize scoreboard variables
user_wins = 0
computer_wins = 0
draws = 0
games_played = 0
update_scoreboard()

root.mainloop()
