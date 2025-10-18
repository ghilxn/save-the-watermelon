# Progression 4 — Testing

This file explains how the Save the Watermelon game was tested. It includes test cases for normal inputs, invalid inputs, repeated guesses, and win or lose situations.

---

## Test Cases

T1 - Guessing a correct letter  
Example: enter "a"  
Expected: the letter shows up in the word, slices stay the same  

T2 - Guessing a wrong letter  
Example: enter "z"  
Expected: lose one slice, message says it was wrong  

T3 - Typing a number  
Example: enter "3"  
Expected: message says “Please enter ONE alphabet letter.”  

T4 - Typing more than one letter  
Example: enter "ab"  
Expected: message says “Please enter ONE alphabet letter.”  

T5 - Leaving blank input or pressing Enter  
Expected: message asks for valid input again  

T6 - Repeating a guess  
Example: guess "a" twice  
Expected: message says “You already guessed that letter.” and no slices lost  

T7 - Winning the game  
Example: last correct letter guessed  
Expected: message says “You saved the watermelon!”  

T8 - Losing the game  
Example: all slices are gone after wrong guesses  
Expected: message says “The watermelon was sliced.”  

T9 - Playing again  
Example: typing “y” after finishing  
Expected: game restarts with a new word  

T10 - Quitting the game  
Example: typing “n” after finishing  
Expected: program ends with “Thanks for playing!”

---

## Manual Test Transcript

Example 1 - Winning Game
Welcome to Save the Watermelon!
Word: _ _ _ _ _ _
Guess a letter: a
Good guess!
Word: _ a _ a _ a
Guess a letter: n
Good guess!
Word: b a n a n a
You saved the watermelon! The word was 'banana'.
Play again? (y/n): n
Thanks for playing!

Example 2 - Losing Game
Welcome to Save the Watermelon!
Word: _ _ _ _ _
Guess a letter: x
Wrong! You lost one slice.
Guess a letter: z
Wrong! You lost one slice.
Guess a letter: q
Wrong! You lost one slice.
Guess a letter: e
Wrong! You lost one slice.
Guess a letter: r
Wrong! You lost one slice.
Guess a letter: y
Wrong! You lost one slice.
Oh no! The watermelon was sliced. The word was 'focus'.
Play again? (y/n): n
Thanks for playing!

---

## How to Test the Game

1. Open a terminal inside the project folder.  
2. Type this command and press Enter:
   python -m src.game
3. Try different types of guesses:
   - Correct and wrong letters
   - Repeating letters
   - Numbers or multiple letters
   - Playing again after winning or losing

Optional (for logic functions only):
   python -m unittest discover -s tests

---

## Notes

- Invalid inputs are rejected correctly.  
- Repeated guesses don’t remove slices.  
- Both win and lose endings show the right message.  
- Replay option works fine.  
- No errors or crashes while playing normally.
