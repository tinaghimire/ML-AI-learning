# Best way to define a variable
variable_num = 5

# Int type gets converted to float type when needed
print(11/2)

# To convert float to int
print(int(19.6))

# To display type of data
print(type(variable_num))

print(.1 + .1 + .1 == .3)  # False

# String methods

str_word = "sebastian thrun"
print(str_word.title())     # Capitalize first letter of each word
print(str_word.islower())   # Checks if the string is lowercase

str_count = "One fish, two fish, red fish, blue Fish"
print(str_count.count('fish'))  # 3 not Fish

animal = "dog" 
action = "bite" 
print("Does your {} {}?".format(animal, action))

maria_string = "Maria loves {} and {}" 
print(maria_string.format("math", "statistics"))
