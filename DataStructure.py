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