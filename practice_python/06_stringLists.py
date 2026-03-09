"""
Exercise 6: Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""
word_forward = str(input("Please enter a word: "))
word_reverse = word_forward[::-1]

if word_forward == word_reverse:
    print("This is a palindrome :)")
else:
    print("This is not a palindrome :(")