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

# String method: split()
new_str = "The cow jumped over the moon."
print(new_str.split())
print(new_str.split(' ', 3)) # Here the separator is space, and the maxsplit argument is set to 3.
print(new_str.split('.'))    # Period as a separator.
print(new_str.split(None, 4)) # Using no separators but having a maxsplit argument of 3.

str_count = "One fish, two fish, red fish, blue Fish"
# To find the first occurence of word
print(str_count.index('fish'))
print(str_count.rindex('fish'))

# Slicing a string
greeting = "Hello World"
print(greeting[:5])

# Use of in and not in string
print('ll' in greeting)
print('llo' not in greeting)

# Taking input
name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))

num = int(input("Enter an integer"))
print("hello" * num)

# We can also interpret user input as a Python expression using the built-in function eval.
result = eval(input("Enter an expression: "))
print(result)