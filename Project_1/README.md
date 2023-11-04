# Project details

## Mutable Data Types and Functions

### Mutable data types

- Can be changed after they are created.
- Are passed into functions as a pointer to the original object.
- Changes that happen to this pointer within the function change the original object.

### Immutable data types

- Can not be changed after they are created.
- Are passed into functions as a copy to the original object.
- Changes that happen to this pointer within the function don't affect the original object.

- **Immutable Data Types**: boolean value(bool), integer(int), float, tuple, string(str)
- **Mutable Data Types**: list, dictionary(dict), set

### Note

- Function is able to change mutable object.
- Mutable object only exists within function.
- Mutable object exists outside of function. (Return mutable object)

## How to read filenames from a folder

- Imports only listdir function from OS module
from os import listdir  

- Retrieve the filenames from folder pet_images/
filename_list = listdir("pet_images/")

- Print 10 of the filenames from folder pet_images/
print("\nPrints 10 filenames from folder pet_images/")
for idx in range(0, 10, 1):
    print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )
