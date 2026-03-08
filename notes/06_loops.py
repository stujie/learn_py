# while loop - block of code that executes while condition remains true

# INFINITE LOOP
#while (1 == 1):
    #print("You're stuck in an infinite loop!")

# ex 1
x = 0
while (x < 5):
    print(x)
    x = x+1
    
# ex 2
happy = input("Are you happy? (Yes/No): ")
while (happy == "No"):
    print("Oh no! Let's change that.")
    happy = input("Are you happy now? (Yes/No): ")

# for loop - block of code 

# ex 1
for x in range(5,10):
    print(x)

# ex 2 - skips specific value ("Thu")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for d in days:
    if(d == "Thu"):continue
    print(d)

# nested loops = loop within another loop
for i in range(0,5):
    for j in range(0,5):
        # end = : prevents from moving to next line
        print("*", end="")
    print()  
    
