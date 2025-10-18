#  Save the Watermelon

A fun beginner Python word-guessing game!  
You have to **save the watermelon** by guessing letters before your slices (lives) run out.

---

##  What the Game Does
- A random secret word is chosen.
- The word is hidden with underscores `_ _ _ _`.
- You guess one letter at a time.
- If the letter is in the word → it gets revealed!
- If it’s wrong → you lose one slice (life).
- You **win** when you guess all the letters.
- You **lose** if you run out of slices.

---

##  How to Run the Game

Make sure you have **Python 3** installed.

Open your terminal or command prompt in the project folder, then type:

```bash
python -m src.game
# or
python src/game.py
```

## Folder Layout

save-the-watermelon/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ src/
│  ├─ game.py         → main game file (run this)
│  ├─ logic.py        → game functions
│  ├─ words.py        → word list + random picker
│  └─ __init__.py
├─ tests/
│  ├─ test_logic.py   → small tests for logic.py
│  └─ __init__.py
├─ docs/
│  ├─ design.md       → how the game was planned
│  ├─ pseudocode.md   → step-by-step plan
│  ├─ test-plan.md    → how testing was done
│  └─ screenshots/
└─ data/
   └─ words.txt       → list of possible words

##  How to Test

You can test the game to make sure your code works correctly.

### Option 1 — Using unittest (built into Python)
Type this in your terminal:

```bash
python -m unittest discover -s tests
```
