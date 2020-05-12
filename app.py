# importing the random module to access the random function
import random
# generation of random number
number = random.randint(0, 20)
# taking the user's input as a guess
number_input = input("Whats your guess? (between 0 and 20):  ")
if number > int(number_input):
    print("too low, try entering it again")
    while number != int(number_input):
        number_input = input("Whats your guess? (between 0 and 20):  ")
        if number > int(number_input):
            print("too low, try entering it again")
        elif number == int(number_input):
            print(f"Correct guess: {number}")
        else:
            print("too high, try entering it again")
elif number == int(number_input):
    print(f"Correct guess: {number}")
else:
    print("too high, try entering it again")
    while number != int(number_input):
        number_input = input("Whats your guess? (between 0 and 20):  ")
        if number > int(number_input):
            print("too low, try entering it again")
        elif number == int(number_input):
            print(f"Correct guess: {number}")
        else:
            print("too high, try entering it again")
