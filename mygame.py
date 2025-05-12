import streamlit as st
import random

# --- Session State Initialization ---
def init_game():
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.guess_history = []
    st.session_state.game_over = False

if 'number_to_guess' not in st.session_state:
    init_game()

# --- UI Setup ---
st.set_page_config(page_title="🎯 Guess the Number", layout="centered")
st.markdown("## 🎯 Guess the Number Game")
st.markdown("I'm thinking of a number between **1 and 100**. Try to guess it!")

with st.expander("🔢 Game Rules", expanded=False):
    st.markdown("""
    - Enter a number between 1 and 100.
    - You'll receive hints whether your guess is too high or too low.
    - Try to guess in the fewest attempts possible!
    """)

# --- Input Form ---
with st.form(key="guess_form"):
    guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)
    submitted = st.form_submit_button("Submit Guess")

# --- Guess Logic ---
if submitted and not st.session_state.game_over:
    st.session_state.attempts += 1
    st.session_state.guess_history.append(guess)

    if guess < st.session_state.number_to_guess:
        st.warning("🔽 Too low! Try again.")
    elif guess > st.session_state.number_to_guess:
        st.warning("🔼 Too high! Try again.")
    else:
        st.success(f"🎉 Correct! You guessed the number **{st.session_state.number_to_guess}** in **{st.session_state.attempts}** attempts.")
        st.session_state.game_over = True

# --- Display Guess History ---
if st.session_state.attempts > 0:
    st.markdown("### 📜 Guess History")
    st.write(st.session_state.guess_history)

# --- Game Over Actions ---
if st.session_state.game_over:
    st.balloons()
    if st.button("🔁 Play Again"):
        init_game()

# --- Footer ---
st.markdown("---")
st.caption("🧠 Built with Streamlit | Game logic by OpenAI's GPT")
