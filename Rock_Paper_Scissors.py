from flask import Flask, render_template, request, session
import random

rps = Flask(__name__)
rps.secret_key = "supersecretkey"  # Needed for session management

@rps.route('/')
def index():
    # Initialize scores in session if they don't exist
    if "player_score" not in session:
        session["player_score"] = 0
    if "cpu_score" not in session:
        session["cpu_score"] = 0
    return render_template('index.html')

@rps.route('/play', methods=['POST'])
def play():
    choices = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(choices)
    player = request.form['choice'].capitalize()

    if player not in choices and player != "End":
        return "Invalid choice. Please enter 'Rock', 'Paper', or 'Scissors'."

    # Handle end condition
    if player == "End":
        final_score = f"Final Score:<br>Computer Score: {session['cpu_score']}<br>Player Score: {session['player_score']}"
        session["player_score"] = 0
        session["cpu_score"] = 0
        return final_score

    # Determine winner
    if player == computer:
        result = "It's a Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        result = "You win!"
        session["player_score"] += 1
    else:
        result = "You lose!"
        session["cpu_score"] += 1

    return f"Computer chose: {computer}<br>{result}<br>Computer Score: {session['cpu_score']}<br>Player Score: {session['player_score']}"

if __name__ == '__main__':
    rps.run(debug=True)
