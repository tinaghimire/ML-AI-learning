# This code
casts = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]

lower_cast = []
for cast in casts:
    lower_cast.append(cast.lower())

print(lower_cast)

# is reduced to
lower_cast = [cast.lower() for cast in casts]
print(lower_cast)

# Conditionals in List Comprehension
squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)

# To add else 
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)

# Extract first names
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

# Multiple of 3
multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)

# Filter names by scores
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)