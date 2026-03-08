# source: https://www.youtube.com/watch?v=gOMW_n2-2Mw

# tuple() = ordered and immutable. duplicates ok. FASTER

# define a tuple
fruits = ("apple", "orange", "banana", "coconut", "coconut")

print(len(fruits))
print("pineapple" in fruits)

# tuple methods
print(fruits.index("apple"))
print(fruits.count("coconut"))

# iterate with for loop
for fruit in fruits:
    print(fruit)