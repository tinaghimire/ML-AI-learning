﻿# ML-AI

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

## Scripting

- A script is just Python code, so a Python script is a Python program.
- We can also interpret user input as a Python expression using the built-in function eval. This function evaluates a string as a line of Python.

## Error and Exceptions

- Syntax errors occur when Python can’t interpret our code, since we didn’t follow the correct syntax for Python. These are errors you’re likely to get when you make a typo, or you’re first starting to learn Python.

- Exceptions occur when unexpected things happen during execution of a program, even if the code is syntactically correct. There are different types of built-in exceptions in Python, and you can see which exception is thrown in the error message.

![Exception Type Table](/Materials/exceptions.png?raw=true)
![Exception Type Table](/Materials/exceptions_quiz.png?raw=true)

## Handling errors

- Use try and except.

## Import Local Scripts

- import other_script
  eg import snakefile

## Import Modules

- To import an individual function or class from a module.
  - from module_name import object_name
- To import multiple individual objects from a module.
  - from module_name import first_object, second_object
- To rename a module.
  - import module_name as new_name
- To import an object from a module and rename it
  - from module_name import object_name as new_name
- To import every object individually from a module (DO NOT DO THIS)
  - from module_name import *
  **If you really want to use all of the objects from a module, use the standard import module_name statement instead and access each of the objects with the dot notation.**
- To import the submodule.
  - import package_name.submodule_name
    eg os.path
  
![Import Ways](/Materials/import_rules.png?raw=true)

## Third-Party Libraries

- pip install library_name

IPython - A better interactive Python interpreter
requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
Flask - a lightweight framework for making web applications and APIs.
Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
pytest - extends Python's builtin assertions and unittest module.
PyYAML - For reading and writing YAML files.
NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
Matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
ggplot - Another 2D plotting library, based on R's ggplot2 library.
Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
pyglet - A cross-platform application framework intended for game development.
Pygame - A set of Python modules designed for writing games.
pytz - World Timezone Definitions for Python

- Using a requirements.txt file, add all the packages you need to install with their version(if needed).
  eg  beautifulsoup4==4.5.1
      bs4==0.0.1
      pytz==2016.7
      requests==2.11.1
- You can use pip to install all of a project's dependencies at once by typing
  pip install -r requirements.txt (in your command line.)

## How to Search

Here are some techniques for effective web searching:

Try using "Python" or the name of the library you're using as the first word of your query. This tells the search engine to prioritize results that are explicitly related to the tools you're using.
Writing a good search query can take multiple attempts. If you don't find helpful results on your first attempt, try again.
Try using keywords found on the pages you found in your initial search to direct the search engine to better resources in the subsequent search.
Copy and paste error messages to use as search terms. This will lead you to explanations of the error and potential causes. An error message might include references to specific line numbers of code that you wrote. Only include the part of the error message that comes before this in your search.
If you can't find an answer to your question, ask it yourself! Communities like StackOverflow have etiquette rules you must learn if you want to participate, but don't let this stop you from using these resources.

## Hierarchy of Online Resources

While there are many online resources about programming, not all of the them are created equal. This list of resources is in approximate order of reliability.

The Python Tutorial - This section of the official documentation surveys Python's syntax and standard library. It uses examples, and is written using less technical language than the main documentation. Make sure you're reading the Python 3 version of the docs!
The Python Language and Library References - The Language Reference and Library Reference are more technical than the tutorial, but they are the definitive sources of truth. As you become increasingly acquainted with Python you should use these resources more and more.
Third-Party Library Documentation - Third-party libraries publish their documentation on their own websites, and often times at [](https://readthedocs.org/). You can judge the quality of a third-party library by the quality of its documentation. If the developers haven't found time to write good docs, they probably haven't found the time to polish their library either.
The websites and blogs of prominent experts - The previous resources are primary sources, meaning that they are documentation from the same people who wrote the code being documented. Primary sources are the most reliable. Secondary sources are also extremely valuable. The difficulty with secondary sources is determining the credibility of the source. The websites of authors like Doug Hellmann and developers like Eli Bendersky are excellent. The blog of an unknown author might be excellent, or it might be rubbish.
StackOverflow - This question and answer site has a good amount of traffic, so it's likely that someone has asked (and someone has answered) a related question before! However, answers are provided by volunteers and vary in quality. Always understand solutions before putting them into your program. One line answers without any explanation are dubious. This is a good place to find out more about your question or discover alternative search terms.
Bug Trackers - Sometimes you'll encounter a problem so rare, or so new, that no one has addressed it on StackOverflow. You might find a reference to your error in a bug report on GitHub for instance. These bug reports can be helpful, but you'll probably have to do some original engineering work to solve the problem.
Random Web Forums - Sometimes your search yields references to forums that haven't been active since 2004, or some similarly ancient time. If these are the only resources that address your problem, you should rethink how you're approaching your solution.

## Python OOP

- Object have two parts: Characteristics (Noun) and Actions (Verb).
- class - a blueprint consisting of methods and attributes
- object - an instance of a class. It can help to think of objects as something in the real world like a yellow pencil, a small dog, a blue shirt, etc. However, as you'll see later in the lesson, objects can be more abstract.
- attribute - a descriptor or characteristic. Examples would be color, length, size, etc. These attributes can take on specific values like blue, 3 inches, large, etc.
- method - an action that a class or object could take
- OOP - a commonly used abbreviation for object-oriented programming
encapsulation - one of the fundamental ideas behind object-oriented programming is called encapsulation: you can combine functions and data all into a single entity. In object-oriented programming, this single entity is called a class. Encapsulation allows you to hide implementation details much like how the scikit-learn package hides the implementation of machine learning algorithms.

### 2 Magic Methods

- add : overrides the default behavior of the + symbol
  - In the example in the video, we define exactly what is meant by add Gaussian distributions
- repr : overrides the default behavior of printing variables
  - In the example in the video, we define what is printed when we print a Gaussian distributions.

## Install Python package

- Files needed: setup.py with the required code, and '_init_.py'
  - The code in the init file runs any time the package is imported
- Then get to the location of setup.py
- Type command 'pip install .' to download the whole package
- Open python in terminal and type
  - from Distributions import Gaussian
  - gaussian_one = Gaussian(10, 5)
  - ggaussian_oneaussian_one.mean  #10
  - gaussian_one.stdev  #5
  - import Distributions
  - Distributions._file_
    #'C:\\Users\\ghimi\\OneDrive\\Documents\\Github\\AWS\\OOP\\Python Package\\Distributions\\_init_.py'
- As you make changes to the files, you will need to rebuild the package, 'pip install --upgrade .'

## Scikit-learn Source code

Use the following resources to learn about more advanced OOP topics that appear in the scikit-learn package:

- Decorators
- Mixins

## Putting Code on PyPi

### PyPi & Test PyPi

Note that pypi.org and test.pypy.org are two different websites. You'll need to register separately at each website. If you only register at pypi.org, you will not be able to upload to the test.pypy.org repository.

Also, remember that your package name must be unique. If you use a package name that is already taken, you will get an error when trying to upload the package.

#### Command to upload to the pypi test repository

twine upload --repository-url [](https://test.pypi.org/legacy/) dist/*
pip install --index-url [](https://test.pypi.org/simple/) dsnd-probability

#### Command to upload to the pypi repository

twine upload dist/*
pip install dsnd-probability
