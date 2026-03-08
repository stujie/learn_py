# 1. math library - some advanced math functions
import math
# math functions
print("pi:", math.pi) 
print("square root:", math.sqrt(25)) 
print("round up:", math.ceil(99.2))
print("round down:", math.floor(89.4))

# 2. random library - randomly output values
import random
# random functions
print("random int generator:", random.randint(1,10))
print("random choice generator:", random.choice(["sushi", "burger", "pasta"]))

# 3. os - interact with your operating system
import os
print("current directory:")
print(os.getcwd())
print("files in folder:")
print(os.listdir())
