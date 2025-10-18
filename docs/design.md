# Progression 1 — Design

## Problem Statement
Save the Watermelon is a small Python word-guessing game played in the terminal.  
The player must guess letters to reveal a hidden word before running out of slices (lives).  
This project helps beginners practice loops, conditionals, functions, and clean structure while having fun with a simple goal.

---

## Target Audience
This game is made for **beginner Python students** or anyone learning how to build basic projects that use input, logic, and repetition.  
It’s meant to be simple to run and easy to understand without needing any extra software.

---

## Game Rules
1. A random secret word is chosen from a short list.  
2. The word starts hidden with underscores (example: `_ _ _ _`).  
3. The player guesses one letter at a time.  
4. If the guess is correct, that letter shows up in the word.  
5. If the guess is wrong, one slice (life) is taken away.  
6. The player starts with 6 slices total.  
7. If all letters are guessed before slices reach 0 → **win**.  
8. If slices reach 0 before the word is finished → **lose**.  
9. After a game ends, the player can choose to play again.

---

## Win and Lose Conditions
- **Win:** all the letters in the secret word have been guessed.  
- **Lose:** the player’s slices reach zero.

---

## Core Features (Must-Have)
- Picks a random word from a built-in list.  
- Displays the hidden word with underscores.  
- Lets the player enter one letter per turn.  
- Checks if the letter is in the word.  
- Removes one slice if the guess is wrong.  
- Prevents duplicate guesses from counting again.  
- Ends the game with a clear win/lose message.  
- Gives a replay option when finished.

---

## Stretch Goals (Nice-to-Have)
These are fun ideas to add later but not required:
- ASCII art that shows the watermelon getting sliced.  
- Difficulty options (easy, medium, hard).  
- Word categories (fruits, animals, school, etc.).  
- A scoreboard that tracks your number of wins.

---

## Basic Flow (Bullet Flow)
Start → load the word list → choose a random secret word  
→ set slices = 6 and guessed_letters = empty  
→ while slices > 0 and the word isn’t fully revealed:  
 • show the word with blanks  
 • ask the player for a letter  
 • check if it’s valid (one letter, alphabetic, not already guessed)  
 • if it’s in the word → reveal the letter(s)  
 • if it’s not → subtract one slice  
→ when done, show win or lose message  
→ ask if player wants to play again  

---

## Data Design
The game keeps track of:
- `secret_word`: the word that the player is trying to guess  
- `guessed_letters`: the set of all letters the player has guessed  
- `remaining_slices`: how many lives are left  
- `display_word`: what the player currently sees (with blanks for hidden letters)  

Each of these values gets updated every time the player guesses a new letter.

---

## Module and Function Responsibilities
- **game.py** — runs the main game loop, takes user input, and prints results.  
- **logic.py** — has helper functions that check guesses, show the current word, and check for a win.  
- **words.py** — holds the list of words and randomly picks one for the game.  
- **test_logic.py** — includes small tests to make sure the helper functions work correctly.
