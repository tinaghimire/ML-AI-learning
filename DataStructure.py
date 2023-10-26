# List
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']

print(months[-1])   # Jul
print(months[2])    # Mar
print(len(months))  # 7

# Slicing in list 
half_mon = months[:4] # 'Jan', 'Feb', 'Mar', 'Apr'

# Use of in and not in list
print('Apr' in months)
print('Oct' not in months)

# Methods
num = [21, 2, 15, 98, 12]
print(len(num))
print(max(num))
print(min(num))
print(sorted(num))

num_word = ['Twenty-one', 'Two', 'Fifteen', 'Ninety-eight', 'Twelve']
print(len(num_word))
print(max(num_word))
print(min(num_word))
print(sorted(num_word))

# Join function in list
print("/".join(num_word))

# Append function in list
num_word.append('Fifty')
num.append(50)
print(num)
print(num_word)

# Iterate in list
for month in months:
    print(month)

# Create new list
lower_word = []
for word in num_word:
    lower_word.append(word.lower())

print(lower_word)

# Tuple
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

# Iterate in Tuple
for loc in location:
    print(loc)

# Tuple with multiple variable names
dimensions = 52, 40, 100
length, width, height = dimensions  # Called Tuple unpacking
print("The dimensions are {} x {} x {}".format(length, width, height))

# Sets
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_num = set(numbers)    #  {1, 2, 6, 3}
print(unique_num)

# Iterate in sets
for num in unique_num:
    print(num)

# Methods in set
fruit = {"apple", "banana", "orange", "grapefruit"}
print("watermelon" in fruit)

fruit.add("watermelon")
print(fruit)

print(fruit.pop())
print(fruit)

# Dictionary in python
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])   # 2
elements["lithium"] = 3     # Values can be changed
print(elements)

# Iterate in Dictionary
for key, val in elements.items():
    print(key,val)

# in keyword
print("carbon" in elements)
print(elements.get("dilithium"))

# Identity operators: is and is not
n = elements.get("dilithium")
print(n is None)
print(n is not None)

# get method with default value "No such element"
print(elements.get("dilithium", "No such element"))

# Compound data structures
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
elements['oxygen']['is_noble_gas'] = False

for key, val in elements.items():
    print(key.capitalize())
    for k,v in val.items():
        print(k, v)

