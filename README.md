# AWS ML-AI

## Python

- Data Types: Integers, Floats, Booleans, Strings
- Operators: Arithmetic, Assignment, Comparison, Logical
- Built-In Functions, Type Conversion
- Whitespace and Style Guidelines
- print() -- Built-in function that displays input values as text in the output
- The usual order of mathematical operations holds in Python, often referred to as
  **PEMDAS**: Parentheses-'()', Exponents-'**', Multiplication-'*'/Division-'/', Addition/Subtraction.
- Modulo '%' gives the remainder after dividing
- '//' divides and rounds down to the nearest integer --Quotient
- Caret '^' performs bitwise XOR not exponent in python
- Logical operators are and, or, not
- For comparison: <,>,<=,>=,==,!=

### Variables

- To assign multiple variables,
    x, y, z = 3, 4, 5
- Keywords in Python

![List of Keywords used in Python](/Materials/keywords_in_py.png?raw=true)

For more tutorial in python [Click here](https://docs.python.org/3/tutorial/)

### String

- Use \ to print ' or "
- To combine strings, use +
- To repeat strings, use *
- len(str_word) is used to count the length of string str_word
- We can take each character from a string and use it
  str_word = "Hello"
  str_word[1]  # e
- Elements cannot be modified individually.
- Ordered

## Tips on successful debugging

- Understand common error messages you might receive and what to do about them.
- Search for your error message, using the Web community.
- Use print statements.

### List

- Mutable ordered sequence of elements.
- Can be sliced, and use in, not in, len.
- Can be modified and are ordered.

### List Method

- len() -- Length
- max() -- Maximum element
- min() -- Minimum element
- sorted() -- Ascending order sorting
- joined() -- To create a string of all list elements joined by a separator string.

Note:

- All data structures are data types.

### Tuples

- Immutable ordered sequences of elements.
- Can be indexed and sliced like a list.
- Used to store related pieces of informations like latitude and longitude, dimensions.
- The parentheses are optional when defining tuples, and programmers frequently omit them if parentheses don't clarify the code.
- You can use **tuple unpacking** to assign the information from a tuple into multiple variables without having to access them one by one and make multiple assignment statements.

Remember
![Quiz question of Tuple](/Materials/quiz_tuple.png?raw=true)

### Sets

- Mutable unordered collections of unique elements.
- One application of a set is to quickly remove duplicates from a list.
- Sets support the in operator the same as lists do.
- To add elements, add method and to remove, pop method.
- Since in sets there is no order, so pop removes a random element.

### Dictionaries

- Mutable data typle that stores mappings of unique keys to values.
- Donot use mutable data type as keys like list but values can be.
- Uses in keyword, get method to lopp up for values in a dictionary and returns None if key isn't found.
- Identity operators: is and is not
  - is -- evaluates if both sides have the same identity
- int, float and string can be used as keys (immutable).
- Add items with append

- is checks for identity i.e. if a and c are identical and b = a then c and b are not identical objects as they point to different objects.
- == checks for equality i.e. if a and c are identical and b = a then c and b are equal.

![Data Structure Table](/Materials/data_structures.png?raw=true)

### Control Flow

- Conditional statements
- for and while loops
- break and continue
- useful built-in functions: Zip and Enumerate
- list comprehensions

**NOTE: Python Style Guide recommends using 4 spaces to indent, rather than a tab.**

#### Good Practice for if statements

1. Don't use True or False as conditions
2. Be careful writing expressions that use logical operators.
3. Don't compare a boolean variable with == True or == False.

Here are most of the built-in objects that are considered False in Python:

- constants defined to be false: None and False
- zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
- empty sequences and collections: '"", (), [], {}, set(), range(0)

#### for loop VS while loop

- for loops are ideal when the number of iterations is known or finite.
- while loops are ideal whrn the iterations need to continue until a condition is met.

#### Break and continue

- To terminate the loop when a condition is met, we use break.
- To skip a condition after it is met or to terminate only one iteration, we use continue.

#### Zip and Enumerate

- Zip returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables.
- Enumerate is a built in function that returns an iterator of tuples containing indices and values of a list.

### Function

- Functions are useful blocks of code that allow you to encapsulate a task.
- Encapsulation allows us to carry out a whole series of steps with one simple command.
- Local variables has higher priority than global ones.'

#### Documentation

- A type of comment used to explain the purpose of a function and how it should be used.
  """This gives a docstring."""
- A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the _doc_ special attribute of that object.
