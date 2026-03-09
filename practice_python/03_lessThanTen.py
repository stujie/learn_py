"""
Exercise 3: Take a list and write a program that prints out all the elements of the list that are less than 5.

"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for number in a:
    if number < 5:
        print(number)

"""
- Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for number in a:
    if number < 5:
        b.append(number)
print(b)

"""
- write this in one line of Python
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print( [ number for number in a if number < 5 ] )

"""
- Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user = int(input("Enter a number: "))
print([number for number in a if number < user])