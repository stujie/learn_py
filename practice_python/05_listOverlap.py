"""
Exercise 5: Take 2 lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates)
"""
import random

# define 2 lists of varying lengths
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# define overlap list
overlap = []

# range max will be larger list length
range_max = max(len(a), len(b))

if(max(len(a), len(b)) == len(a)):
    list_1 = a
    list_2 = b
else:
    list_1 = b
    list_2 = a

for number in list_1:
    if (number in list_2) & (number not in overlap):
        overlap.append(number)

print(overlap)

"""
- write this in one line of Python
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(set(a) & set(b)))

"""
- randomly generate two lists to test this
"""
# define lists
a = []
b = []
overlap = []

# randomize list lengths
min_length = 2
max_length = 20
list_length = random.randint(min_length, max_length)

# randomize each list value
min_num = 1
max_num = 100
for i in range(0, list_length):
    a.append(random.randint(min_num, max_num))
for i in range(0, list_length):
    b.append(random.randint(min_num, max_num))

# range max will be larger list length
range_max = max(len(a), len(b))

if(max(len(a), len(b)) == len(a)):
    list_1 = a
    list_2 = b
else:
    list_1 = b
    list_2 = a

for number in list_1:
    if (number in list_2) & (number not in overlap):
        overlap.append(number)

print("a: ", a)
print("b: ", b)
print("overlap: ", overlap)
