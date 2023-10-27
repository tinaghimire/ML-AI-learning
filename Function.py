# Define a function
def cylinder_vol(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

# Function call
result = cylinder_vol(2, 2)
print(f'Volume of cylinder is {result}')

# Define a function with default arguments
def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height  *pi*  radius ** 2

cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name

# Lambda function
double = lambda x : x * 2
print(double(3))

area = lambda x, y : x * y
print(area(4,10))