import random

def number_generator(level):
    #returns a ranom number between 1 and 100
    high = 0
    if level=="easy":
        high = 20
    elif level=="medium":
        high = 50
    elif level=="hard":
        high = 100
    return random.randint(1, high)

def checker(number, guess):
    #tests if a guess is =, >, or < than the number
    if number==guess:
        return True
    elif number<guess:
        print("Too high")
        return False
    else:
        print("Too low")
        return False


is_correct = False
num_guesses = 0
print("Welcome to Number Crunch: the best number guessing game!")

level = input("Enter your choice of difficulty: Easy, Medium, or Hard").lower()

#verifies that level choice is real
if level == "easy" or level == "medium" or level == "hard":
    number = number_generator(level)
    while is_correct == False:
        num_guesses+=1
        #goes until the guess is = to the number
        curr_guess = input("Enter your guess!")
        #makes sure the guess is an int
        try:
            curr_guess = int(curr_guess)
            is_correct = checker(number, curr_guess)
        except:
            print("Guess needs to be a number")

    print("Correct!")
    print(f"Number of guesses: {num_guesses}")
    print("Congratulations!")
    
else:
    print("That's not an available difficulty, restart")

    