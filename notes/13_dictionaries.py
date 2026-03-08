# source: https://www.youtube.com/watch?v=MZZSMaEAC2g

# dictionary = collcetion of {key:value} pairs
# ordered and changeable. # no duplicates

# define a dictionary
capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}
print(capitals)

# dictionary methods
print(capitals.get("USA"))  # prints capital associated with USA

if(capitals.get("Japan")):  # using .get() with if statements
    print("That capital exists")
else:
    print("That capital doesn't exist")
    

capitals.update({"Germany":"Berlin"}) # add new {key:value}
capitals.update({"USA":"Detroit"}) # update pre-existing {key:value}
capitals.pop("China")   # remove keyvalue pair
capitals.popitem()      # remove latest keyvalue pair
# capitals.clear()    # clear dictionary

keys = capitals.keys()     # get all keys without values in dictionary
print(keys)

for key in capitals.keys():     # iterate through keys
    print(key)

values = capitals.values()  # get all values without keys in dictionary
print(keys)

for value in capitals.values():     # iterate through values
    print(value)

# items method - returns dictionary object (resembles 2d list of tuples)
items = capitals.items()
print(items)

for key, value in capitals.items(): # 2 counters
    print(f"{key}: {value}")        # f-string
