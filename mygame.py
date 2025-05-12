import streamlit as st
import random

# Initialize session state for number and guess count
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.title("🎯 Guess the Number Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess what it is?")

# User input
guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1
        if guess < st.session_state.number_to_guess:
            st.info("Your guess is too low. Try again!")
        elif guess > st.session_state.number_to_guess:
            st.info("Your guess is too high. Try again!")
        else:
            st.success(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
