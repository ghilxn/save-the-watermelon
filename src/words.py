"""
Word list and random word picker for Save the Watermelon.
"""

import random

def get_random_word():
    """Picks a random word from the list."""
    words = [
        "watermelon",
        "python",
        "miramar",
        "basketball",
        "focus",
        "summer",
        "energy",
        "engineer",
        "sunset",
        "coffee",
        "school",
        "friday",
        "gym",
        "study"
    ]
    return random.choice(words)
