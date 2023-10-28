num = int(input("Enter any number: "))

# My code
count = 0 
for i in range(1,num+1):
    if num % i == 0:
        count += 1
    if count > 2:
        print(f"{num} is not a prime")
        break

if count == 2:
    print(f"{num} is a prime")
    
# Alternative
count = 0

for i in range(2,num):
    if num % i == 0:
        count += 1
        print(f"{num} is not a prime")
        break

if count == 0:
    print(f"{num} is a prime")