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