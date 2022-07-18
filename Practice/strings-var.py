# Strings


# Fix the given code to output I'm a programmer.

# Hint
# Escape the single quote inside the string.
# Use backslash \ for escaping.

print('I\'m a programmer')


# Newlines in Strings


# Working with strings is an essential programming skill.

# Task
# The given code outputs A B C D (each letter is separated by a space).
# Modify the code to output each letter on a separate line, resulting in the following output:
# A
# B
# C
# D
# You can use either \n or three quotes to add new lines inside the given string.
# PY


print('A\nB\nC\nD')


# String Operations


# The provided code outputs the string "ni".
# print("ni")
# PY
# Task:
# Modify the code to output the string repeated 3 times, and add an ! (exclamation mark) at the end of the output.

print( "ni" + "ni" + "ni" + "!" )


# Variables


# The provided code stores the value 7 in a variable, and outputs it.

# Task
# Change the code to output the value of the variable raised to the power of 3.

x = 7**3

print(x)


# Multiple Variables


# You can use multiple variables to take multiple inputs for your program.
# For example, the following code takes two inputs and stores them in the variables x and y:
# x = input()
# y = input()
# PY
# Task:
# Given the code above, output the input x repeated y times.

# Sample Input:
# awesome
# 3

# Sample Output:
# awesomeawesomeawesome


x = (input())
y = int(input())

print(x*y)


# Simple Calculator


# Write a program to take two integers as input and output their sum.

# Sample Input:
# 2
# 8

# Sample Output:
# 10

# your code goes here
x = int(input())
y = int(input())
print(int(x+y))
