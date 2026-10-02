# Variables
n = 17
print(n) # 17
pi = 3.141592653589793
print(pi)
message = 'And now for something completely different'
print(message)
print(n + 25) # 42
print(2 * pi) # 6.283185307179586
print(round(pi)) # 3
print(len(message)) # 42

# Variable names
# million! = 1000000 # Error
# 76trombones = 'big parade' # Error
# class = 'Self-Defence Against Fresh Fruit' # Error

# Here’s a complete list of Python’s keywords:
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield

# The import statement
import math
print(math.pi) # 3.141592653589793
print(math.sqrt(25)) # 5.0
print(math.pow(5, 2)) # 25.0

# Expressions and statements
print(19 + n + round(math.pi) * 2) # 42

# The print function
print(n + 1)
print(n + 2)
print(n + 3)
print(n+2)
print(n+3)
print('The value of pi is approximately')
print(math.pi)
print('The value of pi is approximately', math.pi)

# Arguments
print(int('101')) # 101
print(math.pow(5, 2)) # 25.0
print(int('101', 2)) # 5
print(round(math.pi, 3)) # 3.142
print('Any', 'number', 'of', 'arguments')
# print(float('123.0', 2)) # Error
# print(math.pow(2)) # Error
# print(math.sqrt('123')) # Error

# Comments
# number of seconds in 42:42
seconds = 42 * 60 + 42
miles = 10 / 1.61     # 10 kilometers in miles
v = 8     # assign 8 to v
v = 8     # velocity in miles per hour 

# Debugging
# million! = 1000000 
# Cell In[40], line 1
#     million! = 1000000
#            ^
# SyntaxError: invalid syntax

# '126' / 3
# TypeError: unsupported operand type(s) for /: 'str' and 'int'

# 1 + 3 / 2
# 2.5

# Glossary
# variable: A name that refers to a value.
# assignment statement: A statement that assigns a value to a variable.
# state diagram: A graphical representation of a set of variables and the values they refer to.
# keyword: A special word used to specify the structure of a program.
# import statement: A statement that reads a module file so we can use the variables and functions it contains.
# module: A file that contains Python code, including function definitions and sometimes other statements.
# dot operator: The operator, ., used to access a function in another module by specifying the module name followed by a dot and the function name.
# evaluate: Perform the operations in an expression in order to compute a value.
# statement: One or more lines of code that represent a command or action.
# execute: Run a statement and do what it says.
# argument: A value provided to a function when the function is called.
# comment: Text included in a program that provides information about the program but has no effect on its execution.
# runtime error: An error that causes a program to display an error message and exit.
# exception: An error that is detected while the program is running.
# semantic error: An error that causes a program to do the wrong thing, but not to display an error message.

# Exercises
# 1.
# Why is it bad to use int, float, and str as variable names?
# It is legal but strongly discouraged because these names represent built-in functions and data types in Python. If you assign a value to one of these names, you overwrite its original behavior. This concept is known as shadowing.
# • The Problem: If you write str = "Hello", the built-in str() function becomes unavailable for the rest of your script. If you later try to convert a number to a string using str(123), Python will throw a TypeError: 'str' object is not callable.
# • The Impact: It leads to confusing bugs, breaks standard Python functionality, and makes your code hard for other programmers to read.

# What are the built-in functions in Python?
# Python features a built-in library of functions that are always available without requiring you to import any modules. Some of the most common ones include:
# • Input & Output: print(), input()
# • Type Conversion: int(), float(), str(), list(), dict(), bool()
# • Information & Inspection: len(), type(), help(), dir()
# • Math & Aggregation: abs(), round(), max(), min(), sum()
# • Iteration & Sequencing: range(), enumerate(), zip(), sorted()

# What variables and functions are in the math module?
# The math module gives you access to mathematical functions for real numbers. You must load it first using import math.
# Core Constants (Variables):
# • math.pi (π ≈ 3.14159)
# • math.e (e ≈ 2.71828)
# • math.tau (τ ≈ 6.28318)
# • math.inf (Mathematical infinity)
# Common Functions:
# • Rounding: math.ceil() (rounds up) and math.floor() (rounds down)
# • Powers & Roots: math.sqrt() (square root) and math.pow(x, y) (\(x^{y}\))
# • Trigonometry: math.sin(), math.cos(), math.tan() (all accept angles in radians)
# • Logarithms: math.log() (natural log) and math.log10() (base-10 log)

# Other than math, what modules are considered core Python?
# These are part of the Python Standard Library, meaning they come pre-installed with Python. Key core modules include:
# • os & sys: For interacting with the operating system, file paths, and system-specific parameters.
# • datetime: For manipulating dates, times, and time zones.
# • random: For generating pseudo-random numbers and shuffling or selecting elements from lists.
# • json: For parsing and building JSON data (essential for web development and APIs).
# • re: For regular expressions (advanced pattern matching and text manipulation).
# • collections: For specialized container data types like Counter, deque, and namedtuple.

# 2.
# 17 = n # Error
x = y = 1 # No Error
x = 17; # No Error
x = 14. # becomes Float
# print(maath.pi) # Error, correct math

# 3.
# part 1
radius = 5
volume = (4/3) * math.pi * (radius ** 3)
print(volume) # 523.5987755982989

# part 2
x = 42
trigonometry = (math.cos(x) ** 2) + (math.sin(x) ** 2) 
print(trigonometry) # 1.0

# part 3
print(math.e) # 2.718281828459045
print(math.pow(math.e, 2)) # 7.3890560989306495
print(math.exp(x)) # 1.739274941520501e+18
# math.exp(x) = math.pow(math.e, x), they are same
