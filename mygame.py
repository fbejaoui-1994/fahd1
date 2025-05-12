import streamlit as st
import random

# --- Configuration ---
st.set_page_config(page_title="Guess the Number", page_icon="🎯", layout="centered")

# --- Helper Functions ---
def generate_number(difficulty):
    ranges = {'Easy': (1, 50), 'Medium': (1, 100), 'Hard': (1, 200)}
    return random.randint(*ranges[difficulty])

# --- Initialize Session State ---
if "game_started" not in st.session_state:
    st.session_state.game_started = False
    st.session_state.difficulty = "Medium"
    st.session_state.number_to_guess = None
    st.session_state.attempts = 0
    st.session_state.game_over = False

# --- Title ---
st.title("🎯 Guess the Number")
st.markdown("Can you guess the number I'm thinking of? Select a difficulty level and start playing!")

# --- Difficulty Selection ---
if not st.session_state.game_started:
    st.session_state.difficulty = st.radio(
        "Select Difficulty:",
        options=["Easy", "Medium", "Hard"],
        horizontal=True
    )

    if st.button("Start Game"):
        st.session_state.number_to_guess = generate_number(st.session_state.difficulty)
        st.session_state.attempts = 0
        st.session_state.game_started = True
        st.session_state.game_over = False
        st.success(f"Game started! I'm thinking of a number in the range for {st.session_state.difficulty} difficulty.")

# --- Game Play ---
if st.session_state_
