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
print("Welcome to the Nittany Number Game!")
print("You can choose your own path")
level = input("Enter your choice of difficulty: Easy, Medium, or Hard").lower()

if level == "easy" or level == "medium" or level == "hard":
    number = number_generator(level)
    while is_correct == False:
        #goes until the guess is = to the number, might add a guess limit later
        curr_guess = int(input("Enter your guess!"))
        is_correct = checker(number, curr_guess)
    print("Correct!")
else:
    print("That's not a difficulty, restart")

    