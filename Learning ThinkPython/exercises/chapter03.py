# Defining new functions
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

print(print_lyrics) # Error
print_lyrics() # Working

# Parameters
def print_twice(string):
    print(string)
    print(string)

print_twice('Dennis Moore, ')

# or that
string = 'Dennis Moore, '
print(string)
print(string)

# or that
line = 'Dennis Moore, '
print_twice(line)

# Calling functions
def repeat(word, n):
    print(word * n)

spam = 'Spam, '
repeat(spam, 4)

def first_two_lines():
    repeat(spam, 4)
    repeat(spam, 4)

first_two_lines()

def last_three_lines():
    repeat(spam, 2)
    print('(Lovely Spam, Wonderful Spam!)')
    repeat(spam, 2)

last_three_lines()

def print_verse():
    first_two_lines()
    last_three_lines()

print_verse()

# Repetition
for i in range(2):
    print(i)

for i in range(2):
    print("Verse", i)
    print_verse()
    print()

def print_n_verses(n):
    for i in range(n):
        print_verse()
        print()

print_n_verses(3)

def print_n_verses_bonus(n):
    for i in range(n):
        print("Verse", i)
        print_verse()
        print()

print_n_verses_bonus(3)

# Variables and parameters are local
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Always look on the '
line2 = 'bright side of life.'
cat_twice(line1, line2)

# print(cat) # Error, because outside of the function, cat is not defined.

# Tracebacks
def print_twice(string):
    print(cat)  # NameError
    print(cat)

print(print_twice) # Error

# cat_twice(line1, line2) # Error

# Exercises
# 1. Exercise:
# 1. Spaces and tabs in Python
# In Python, indentation is mandatory to define code blocks (like functions and loops). The official Python style guide (PEP 8) strictly recommends using four spaces per indentation level. While the Tab key can also be used, mixing spaces and tabs in the same file causes an IndentationError. Consistency is key.
# 2. The repeat function (With a for loop)
def repeat(string, number):
    for i in range(number):
        print(string)
# Alternative version (Without a for loop):
def repeat(string, number):
    # This utilizes Python's string multiplication feature
    print(string * number)
# 3. Debugging print_twice
def print_twice(string):
    print(cat)
    print(cat)
# What is wrong with this code:
# The function defines a parameter named string, but inside the function body, it tries to print a variable named cat. Because cat has not been defined anywhere inside or outside the function, Python will crash and raise a NameError: name 'cat' is not defined. To fix it, cat must be changed to string.

# 2. Exercise:
def print_right(text):
    spaces = 40 - len(text)
    print((" " * spaces) + text)

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")

# 3. Exercise:
def triangle(text, n):
    for i in range(n + 1):
        print(text * i)

triangle('L', 5)

# 4. Exercise:
def rectangle(text, w, h):
    for i in range(h):
        print(text * w)
rectangle('H', 5, 4)

# 5. Exercise:
def bottle_verse(n):
    for i in range(n, 0, -1):
        print(i, 'bottles of beer on the wall')
        print(i, 'bottles of beer')
        print('Take one down, pass it around')
        print(i - 1, 'bottles of beer on the wall')
        print()
bottle_verse(99)

def bottle_verse(n):
        print(n, 'bottles of beer on the wall')
        print(n, 'bottles of beer')
        print('Take one down, pass it around')
        print(n - 1, 'bottles of beer on the wall')

for n in range(99, 0, -1):
    bottle_verse(n)
    print()