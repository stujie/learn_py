"""
Exercise 8: Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""
import random

number = random.randint(1,9)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("Enter a guess between 1 and 9: ")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    count = count + 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Exactly Right!")
        print ("It took you " + str(count) + " tries to guess correctly!")




