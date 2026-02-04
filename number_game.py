"""
------------------------------------------------------------
|   Project Title : Magic Number Guessing Game              |
|   Author        : Shivansh Vishwakarma                     |
|   Language      : Python (Streamlit)                      |
|   Framework     : Streamlit                               |
|   Version       : 1.0                                     |
------------------------------------------------------------
|   Description:                                            |
|   This is an interactive number guessing game built       |
|   using Streamlit. The program generates a random         |
|   number between 1 and 100 and allows the user to guess   |
|   it with real-time feedback.                             |
|                                                           |
|   Features:                                               |
|   - Uses session_state to preserve game state             |
|   - Styled UI with custom CSS                             |
|   - Visual effects like snow and balloons                 |
|   - Play Again and Quit options                           |
|   - Beginner-friendly structure                           |
------------------------------------------------------------
"""

import random as r              # Used to generate random magic number
import streamlit as st          # Streamlit library for web-based UI


def play_game():
    """
    Main function that controls the flow of the Magic Number game
    """

    # --------------------------------------------------------
    # Step 1: Configure Streamlit page settings
    # --------------------------------------------------------
    st.set_page_config(
        page_title="Magic Number",
        page_icon="D:\DOWNLOAD\Magic_Number_Logo.webp",
        layout="wide"
    )

    # --------------------------------------------------------
    # Step 2: Apply custom CSS for background, text, and buttons
    # --------------------------------------------------------
    st.markdown(
        """<style>
        .stApp{
        background-color:#000000;
        color:white;
        }
        .stButton>button{
        background-color:#1f77b4;
        color:white;
        border:2px solid red;
        border-radius:8px;
        padding:8px 20px;
        .stText{
        color:white;}
        </style>""",
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # Step 3: Display game title
    # --------------------------------------------------------
    st.header("--- Welcome To Number Guessing Game ! ---")

    # --------------------------------------------------------
    # Step 4: Initialize session state variables (only once)
    # --------------------------------------------------------
    if "magic_number" not in st.session_state:
        st.session_state.magic_number = r.randint(1, 100)  # Random number

    if "attempt" not in st.session_state:
        st.session_state.attempt = 0                        # Attempt counter

    if "guessed" not in st.session_state:
        st.session_state.guessed = False                    # Win status

    # --------------------------------------------------------
    # Step 5: Take user input
    # --------------------------------------------------------
    st.write("Enter The Number")
    userno = st.number_input(" ", min_value=1, max_value=100, step=1)

    # --------------------------------------------------------
    # Step 6: Check user guess when button is clicked
    # --------------------------------------------------------
    if st.button("Check Number !"):

        # Case 1: Guess is higher than magic number
        if userno > st.session_state.magic_number:
            st.markdown(
                """<div style ="color:white; background-color:#6113A8;
                padding:12px; border-radius:8px">
                Too high! The magic is lower.
                </div>""",
                unsafe_allow_html=True
            )
            st.session_state.attempt += 1
            st.snow()

        # Case 2: Guess is lower than magic number
        elif userno < st.session_state.magic_number:
            st.markdown(
                """<div style ="color:white; background-color:#6113A8;
                padding:12px; border-radius:8px">
                Too low! The magic is higher.
                </div>""",
                unsafe_allow_html=True
            )
            st.session_state.attempt += 1
            st.snow()

        # Case 3: Correct guess
        else:
            st.markdown(
                f"""<div style ="color:white; background-color:#0DFF29;
                padding:12px; border-radius:8px">
                You Found The Magic Number {st.session_state.magic_number}
                in Attempts {st.session_state.attempt}
                </div>""",
                unsafe_allow_html=True
            )

            st.session_state.guessed = True
            st.balloons()

    st.text(" ")

    # --------------------------------------------------------
    # Step 7: Show Play Again / Quit options after winning
    # --------------------------------------------------------
    if st.session_state.guessed:
        col1, col2 = st.columns(2)

        # Play Again button resets the game
        with col1:
            if st.button("PLay Again"):
                st.session_state.magic_number = r.randint(1, 100)
                st.session_state.attempt = 0
                st.session_state.guessed = False
                st.rerun()

        # Quit button stops the app
        with col2:
            if st.button("Quit"):
                st.stop()


# ------------------------------------------------------------
# Program execution starts here
# ------------------------------------------------------------
if __name__=="__main__":
    play_game()
