# Guess the number game

#import modules
import random
import time

aim_number = random.randint(1,50)

while True:
    guess_number = int(input("Enter your guess number (1-50) :"))
    if guess_number > aim_number:
        print("I'm checking..")
        time.sleep(1)
        print("Enter smaller number")
    elif guess_number < aim_number:
        print("I'm checking..")
        time.sleep(1)
        print("Enter bigger number")
    else:
        print("I'm checking..")
        time.sleep(1)
        print("Congrat!")
        break



