"""
Save the Watermelon - Main Game File
This file runs the main game loop and handles player input.
"""

from src.words import get_random_word
from src.logic import show_hidden_word, check_win, clean_input


def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    slices = 6

    print("Welcome to Save the Watermelon!")
    print("Try to guess the word before your slices run out.\n")

    while slices > 0 and not check_win(secret_word, guessed_letters):
        print("Word:", show_hidden_word(secret_word, guessed_letters))
        print("Slices left:", slices)
        guess = input("Guess a letter: ")
        guess = clean_input(guess)

        if not guess:
            print("Please enter ONE alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!\n")
        else:
            slices -= 1
            print("Wrong! You lost one slice.\n")

    if check_win(secret_word, guessed_letters):
        print(f"You saved the watermelon! The word was '{secret_word}'.")
    else:
        print(f"Oh no! The watermelon was sliced. The word was '{secret_word}'.")

    print("Game over!\n")


def main():
    play_again = "y"
    while play_again.lower() == "y":
        play_game()
        play_again = input("Play again? (y/n): ")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
