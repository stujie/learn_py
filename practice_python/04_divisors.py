"""
Exercise 4: Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you dont know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

number = int(input("Input an integer:"))
divisors = []

for x in range (1, number+1):
    if number % x == 0:
        divisors.append(x)
print(divisors)