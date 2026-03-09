# source: https://www.youtube.com/watch?v=ISfxEV4b7po

# index operator [] = gives access to a sequence's element (str, list, tuples)

file_name = "indexing notes"

if(file_name[0].islower()):
    file_name = file_name.capitalize()
print(file_name)

# substrings
file_name = "indexing notes"
first_word = file_name[:8].upper()
print(first_word)
second_word = file_name[9:].lower()
print(second_word)
last_character = file_name[-1]
print(last_character)