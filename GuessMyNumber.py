# Guess My Number
# Pawelski
# 10/7/2024
# Programming Fundamentals

import random

mystery_number = random.randint(1, 100)

guess = int(input("Guess my number (its between 1 and 100) >> "))
while guess != mystery_number:
    if guess > mystery_number:
        print("You guessed too high!")
    # Add your code here!
    guess = int(input("Guess my number (its between 1 and 100) >> "))
print("You found my number!")
