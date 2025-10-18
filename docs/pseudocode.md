# Progression 2 — Pseudocode

This pseudocode shows how the Save the Watermelon game works step-by-step before writing the Python code. It includes the main game loop, input checks, win/lose conditions, and the replay system.

FUNCTION main_game
    secret_word ← pick_random_word()
    guessed_letters ← empty set
    slices ← 6

    WHILE slices > 0 AND NOT all_letters_revealed(secret_word, guessed_letters)
        DISPLAY hidden version of secret_word (example: "_ a _ e")
        DISPLAY number of slices left

        guess ← ask player to enter a letter
        guess ← lowercase(guess)

        IF guess is not a single alphabetic letter THEN
            DISPLAY "Please enter one letter only."
            CONTINUE
        ENDIF

        IF guess already in guessed_letters THEN
            DISPLAY "You already guessed that letter."
            CONTINUE
        ENDIF

        ADD guess TO guessed_letters

        IF guess is in secret_word THEN
            DISPLAY "Good guess!"
        ELSE
            slices ← slices - 1
            DISPLAY "Wrong guess. Slices left: " + slices
        ENDIF
    ENDWHILE

    IF all_letters_revealed(secret_word, guessed_letters) THEN
        DISPLAY "You saved the watermelon!"
    ELSE
        DISPLAY "Oh no! The watermelon was sliced."
    ENDIF
END FUNCTION


FUNCTION start_game
    play_again ← TRUE
    WHILE play_again = TRUE
        CALL main_game()
        answer ← ask "Play again? (y/n)"
        IF answer = "y" THEN
            play_again ← TRUE
        ELSE
            play_again ← FALSE
        ENDIF
    ENDWHILE
    DISPLAY "Thanks for playing!"
END FUNCTION


FUNCTION pick_random_word
    RETURN a random word from the list
END FUNCTION


FUNCTION all_letters_revealed(secret_word, guessed_letters)
    RETURN TRUE if every letter in secret_word is inside guessed_letters
END FUNCTION

NOTES:
- Only accepts one letter at a time.
- Wrong letters remove one slice.
- Repeated guesses do not take a slice.
- Game ends when player wins or loses.
- Player can replay after finishing.
