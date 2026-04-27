import random

def number_generator():
    #returns a ranom number between 1 and 100
    return random.randint(1, 100)

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
    
number = number_generator()
is_correct = False

while is_correct == False:
    #goes until the guess is = to the number, might add a guess limit later
    curr_guess = int(input("Enter your guess!"))
    is_correct = checker(number, curr_guess)
print("Correct!")

    