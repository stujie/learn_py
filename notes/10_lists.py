# list[] = ordered and changeable. duplicates ok

# define a list
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)
print(fruits[0])    # index 0 of list fruit
print(fruits[0:2])  # 0 inclusive, 2 exclusive
print(fruits[::2])  # every other fruit
print(fruits[::-1]) # reverse list
print(len(fruits))  # length of list
print("apple" in fruits)    # if value is in a list

# fruits[0] = "pineapple"     # alter list value at index

# list methods
fruits.append("pineapple")  # insert value at end of list
fruits.remove("apple")      # remove specified value
fruits.insert(1, "grape")   # index to insert specified value
fruits.sort()       # sort list in asc order
fruits.reverse()    # reverse sorted list
# fruits.clear()      # clear list
print(fruits.count("banana")) # count instances of value
print(fruits.index("pineapple")) # returns index of specified value
fruits.pop() # removes the last value

