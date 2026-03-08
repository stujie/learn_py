# string methods
name = "StutieBanerjie"
age = "24"

# prints length of string
print(len(name))
# find first instance of a character & prints index
print(name.find("e")) 
# capitalize first letter in string
print(name.capitalize())
# capitalize entire string
print(name.upper())
# lowercase entire string
print(name.lower())
# check if string is a number
print(name.isdigit())
print(age.isdigit())
# check if string only contains alphabetical letters
print(name.isalpha())
print(age.isalpha())
# print number of instances of a character in a string
print(name.count("i"))
# replace instance of one character with another character
print(name.replace("e", "x"))
# extra: print string multiple times
print(name * 3)

# string slicing
alphabet = "abcdefghijklmnopqrstuvwxyz"

# blank index value, assume 0
first_10 = alphabet[:10]
print(first_10)
# start index is included, end index is not included
second_10 = alphabet[10:20]
print(second_10)
# blank stop index, assumes end of string
last_6 = alphabet[20:]
print(last_6)
# step of 2 skips every other letter
every_other_letter = alphabet[::2]
print(every_other_letter)
# step of -1 reverses the string
rev_alphabet = alphabet[::-1]
print(rev_alphabet)
# start 12 index from start, end 4 index from end
slice_middle = slice(8,18)
print(alphabet[slice_middle])
