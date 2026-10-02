# Arithmetic operators
print(30 + 12) # 42
print(43 - 1) # 42
print(6 * 7) # 42
print(84 / 2) # 42.0
print(84 // 2) # 42
print(85 // 2) # 42
print(7 ** 2) # 49
print(7 ^ 2) # 5

# Expressions
print(6 + 6 ** 2) # 42
print(12 + 5 * 6) # 42
print((12 + 5) * 6) # 102

# Arithmetic functions
print(round(42.4)) # 42
print(round(42.6)) # 43
print(abs(42)) # 42
print(abs(-42)) # 42
# print(abs 42) # error
print(abs) # <built-in function abs>

# Strings
print('Hello')
print("world")
print("it's a small ")
print('Well, ')
print('Well, ' + "it's a small " + 'world.')
print('Spam, ' * 4) # 'Spam, Spam, Spam, Spam, '
print(len('Spam')) # 4
# print(`Hello`) # Error

# Values and types
print(type(2)) # int
print(type(42.0)) # float
print(type('Hello, World!')) # str
print(int(42.9)) # 42
print(float(42)) # 42.0
print('126') # 126
print(type('126')) # str
# print('126' / 3) # TypeError
print(int('126') / 3) # 42.0
print(float('12.6')) # 12.6
print(1,000,000) # 1 0 0
print(1_000_000) # 1000000

# Exercises
# 1.
# 7 ^ 2 = 7 XOR 2 in python
# round removes comma
# 7 % 2 is modulus operator in Python

# 2.
print(round(42.5)) # 42
print(round(43.5)) # 44
# because python chooses even. Not odd.

# 3.
print(-2) # -2
print(2++2) # it's 2+2
# print(4 2) # Error
# print(round42.5) # Error
# print(round(42.5) # Error

# 4.
print(type(765)) # int
print(type(2.718)) # float
print(type('2 pi')) # str
print(type(abs(-7))) # int
print(type(abs(-7.0))) # float
print(type(abs)) # function
print(type(int)) # type
print(type(type)) # type

# 5.
# How many seconds are there in 42 minutes 42 seconds?
print('seconds:', (42 * 60) + 42) # seconds: 2562

# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
print('miles:', 10 / 1.61) # miles: 6.211180124223602

# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?
print('seconds per mile:', ((42 * 60) + 42) / (10 / 1.61)) # seconds per mile: 412.482

# What is your average pace in minutes and seconds per mile?
print('minutes per mile:', (((42 * 60) + 42) / (10 / 1.61)) // 60, 'and seconds per mile:', (((42 * 60) + 42) / (10 / 1.61)) % 60) # minutes per mile: 6.0 and seconds per mile: 52.48200000000003

# What is your average speed in miles per hour?
print('miles per hour:', (10 / 1.61) / (((42 * 60) + 42) / 60 / 60)) # miles per hour: 8.727653570337614