# CMPSC132-Project
Number Guessing Game

Description
    Number Crunch is a simple command-line number guessing game written in Python. The player selects a difficulty level, and the program generates a random number within a specific range. The player continues guessing until they correctly identify the number, receiving feedback after each guess.

Features
    Three difficulty levels:
        Easy (1–20)
        Medium (1–50)
        Hard (1–100)
    Input validation: ensures guesses are numbers
    Feedback system:
        "Too high"
        "Too low"
    Tracks number of guesses
    Random number generation using Python’s random

How to Play
    Enter a difficulty level: easy, medium, or hard
    Enter guesses when prompted
    Continue guessing until you get the correct number
    The program will display how many guesses you used

Example Gameplay
    Welcome to Number Crunch: the best number guessing game!
    Enter your choice of difficulty: Easy, Medium, or Hard: easy
    Enter your guess! 10
    Too low
    Enter your guess! 15
    Too high
    Enter your guess! 12
    Correct!
    Number of guesses: 3
    Congratulations!

Code Structure
    number_generator(level)
        Generates a random number based on difficulty
    checker(number, guess)
        Compares guess to the number and provides feedback
    Main loop
        Handles user input and game flow

