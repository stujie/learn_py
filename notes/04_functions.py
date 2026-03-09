# function - block of code packaged together with a game that performs a specific task; must be defined before being called

# def funcName(): defines function
def print_csc_courses():
    # function variables
    course1 = "CSC 249"
    course2 = "CSC 251"
    # function actions
    print(course1)
    print(course2)

# call function
print_csc_courses()

# function with one argument
def friend_name(name):
    print("My friend's name is " + name)

# call
friend_name("Courtney")
friend_name("Ray")

# function with multiple arguments
def grade_calculator(grade, name):
    if grade < 60:
        print(name + "'s Grade: F")
    elif grade < 70:
        print(name + "'s Grade: D")
    elif grade < 80:
        print(name + "'s Grade: C")
    elif grade < 90:
        print(name + "'s Grade: B")
    else:
        print(name + "'s Grade: A")
        
# call
grade_calculator(73, "Juliet")

# function w/ return values
def next_decade(year):
    next_dec = year + 10
    return next_dec

# call
ten_years_from_now = next_decade(2026)
print("In 10 years it will be the year of " + str(ten_years_from_now))

# nested function calls = function calls inside other function calls. the returned value of the inner most function call is the argument for the next outer function

print(round(abs(float(input("Enter a negative decimal number: ")))))