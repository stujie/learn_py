# source: https://www.youtube.com/watch?v=gOMW_n2-2Mw

# set{} = unordered and unchangeable. add/remove ok. no duplicates

# define a set
fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)
print(len(fruits))  # length of set
print("pineapple" in fruits) # check to see if value is in set

# does not work - unordered
# print(fruits[0]) 
# type error: 'set' object is not subscriptable

# set methods
fruits.add("pineapple") # add specific value to set
fruits.remove("apple")  # remove specific value from set
fruits.pop()        # removes a random value from set
# fruits.clear()    # clear list

# cannot be duplicates
fruits = {"apple", "orange", "banana", "grape", "grape"}
print(fruits)