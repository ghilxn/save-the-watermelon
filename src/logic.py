"""
Game logic helper functions.
These handle word display, input cleanup, and win checking.
"""

def show_hidden_word(secret_word, guessed_letters):
    """Shows the secret word with underscores for unguessed letters."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)


def check_win(secret_word, guessed_letters):
    """Returns True if all letters in the word have been guessed."""
    return set(secret_word).issubset(guessed_letters)


def clean_input(user_input):
    """Makes sure the guess is one lowercase alphabet letter."""
    letter = user_input.strip().lower()
    if len(letter) != 1 or not letter.isalpha():
        return ""
    return letter
