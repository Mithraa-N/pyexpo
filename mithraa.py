import streamlit as st
import random

st.title("Number Guessing Game")

# Initialize session state variables
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.guess_count = 0
    st.session_state.last_guess = None

# Function to reset the game
def reset_game():
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.guess_count = 0
    st.session_state.last_guess = None

# Input for the user's guess
user_guess = st.number_input("Enter your guess (between 1 and 100):", min_value=1, max_value=100)

# Button to submit the guess
if st.button("Submit Guess"):
    st.session_state.guess_count += 1
    st.session_state.last_guess = user_guess

    if user_guess < st.session_state.number_to_guess:
        st.write("Too low! Try again.")
    elif user_guess > st.session_state.number_to_guess:
        st.write("Too high! Try again.")
    else:
        st.write(f"Congratulations! You've guessed the number {st.session_state.number_to_guess} in {st.session_state.guess_count} tries!")
        if st.button("Play Again"):
            reset_game()

# Option to reset the game manually
if st.button("Reset Game"):
    reset_game()
    st.write("Game has been reset. A new number has been generated.")
