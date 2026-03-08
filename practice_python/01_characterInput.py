"""
Exercise 1: Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 
"""
name = input("What is your name?: ")
age = input("What is your age?: ")

hundred_year_old = 2026 - int(age) + 100

print("Hi " + name + "! You will be 100 in " + str(hundred_year_old) + "!")

"""
Extra: Add on to the previous program by asking the user for another number and printing out that many copies of the previous message on separate lines. 
"""
name = input("What is your name?: ")
age = input("What is your age?: ")
number = input("Input a number: ")

hundred_year_old = 2026 - int(age) + 100

for i in range(0,int(number)):
    print("Hi " + name + "! You will be 100 in " + str(hundred_year_old) + "!")
