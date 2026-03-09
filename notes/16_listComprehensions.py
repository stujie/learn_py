# source: https://www.youtube.com/watch?v=fcLDzKH_5XM

# list comprehension = a way to create a new list with less syntax
#                    = can mimic certain lambda functions, easier to read

# list = [expression for item in iterable]

# example 1: for loop
squares = []                # create an empty list
for i in range(1, 11):      # create a for loop
    squares.append(i * i)   # define what each loop iteration should do
print(squares)

# example 2: list comprehension
squares = [i*i for i in range(1,11)]
print(squares)

# list = [expression for item in iterable if conditional]

# example 2: lambda function
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

# example 2: list comprehension
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = [i for i in students if i >= 60]
print(passed_students)

# list = [expression (if/else) for item in iterable ]
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = [i if i >= 60 else "FAIL" for i in students ]
print(passed_students)