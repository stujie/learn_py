# variable - holds values

# type str - string (aka text)
name = "Stutie"
language = "Python"
print ("My name is " + name + " and i'm learning how to code in " + language + ".")

# type int - integer
year = 2026
print ("The year is " + str(year) + ".")

# type float - decimals
height = 172.5 
print ("My height is " + str(height) + " cm.")

# type bool - boolean (t/f)
happy = True
print("Are you happy today?: " + str(happy))

# type casting
# ex: str(a) - convert variable a to data type str

# scope: region that a variable is recognized

name = "Stutie" # global scope (available inside & outside of functions)

def name2():
    name2 = "Stu"   # local scope (available only inside this function)
    print(name2)

print(name)
print(name2) # will not print correctly, because cannot access variable out of function scope
name2()