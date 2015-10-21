import random
import sys
import os

# User input
user_input = input("Type in 5 integers of any sequence separated by commas. Example: 1,2,3,4,5: ")
list_input = user_input.split(",")
# Convert numbered strings into integers in list
list_int = list(map(int, list_input))

# Check Arithmetic Sequence
list_arith = list_int[1] - list_int[0]
if list_int[1] == list_int[0] + list_arith and list_int[2] == list_int[1] + list_arith:
    print("Arithmetic Sequence")

# Check Geometric Sequence
if list_int[1] == list_int[0] * 2 and list_int[2] == list_int[1] * 2 and list_int[3] == list_int[2] * 2:
    print("This is a Geometric Sequence")

# Check Quadratic Sequence
list_quad1 = list_int[1] - list_int[0]
list_quad2 = list_int[2] - list_int[1]
list_diff = list_quad2 - list_quad1
if list_int[1] == list_int[0] + list_quad1 and list_int[2] == list_int[1] + list_quad2:
    print("This is a Quadratic Sequence")

# Check Cubic Sequence
cub1 = list_int[1] - list_int[0] # Subtraction Process
cub2 = list_int[2] - list_int[1] # Subtraction Process
cub3 = list_int[3] - list_int[2] # Subtraction Process

cub_r1 = cub3 - cub2 # Subtraction Process
cub_r2 = cub2 - cub1 # Subtraction Process

# "if" comparison
if cub_r1 == cub_r2:
    print("This is a Cubic Sequence")

# Check Fibonacci Sequence
fib_chck1 = list_int[0] + list_int[1]
fib_chck2 = list_int[1] + list_int[2]

if list_int[2] == fib_chck1 and list_int[3] == fib_chck2:
    print("Fibonacci Sequence")
