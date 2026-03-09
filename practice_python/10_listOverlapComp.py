"""
Exercise 10: (Revisit of Exercise 5)

Take 2 lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. 

Use at least one list comprehension
"""
import random
a_size = random.randint(1,20)
b_size = random.randint(1,20)

a = random.sample(range(1,100), a_size)
b = random.sample(range(1,100), b_size)
overlap = [i for i in a if i in b]

print("a: ", a)
print("b: ", b)
print("overlap: ", overlap)