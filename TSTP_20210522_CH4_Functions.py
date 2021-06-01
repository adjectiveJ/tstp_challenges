"""
The Self-Taught Programmer - Chapter 4 Challenges
Author: Dante Valentine
Date: 22 May, 2021
"""

""" CHALLENGE 1 """
to_square = 12

def square_func(x):
    # Returns the square of x.
    return x*x

resp = square_func(to_square)
#print("The square of", to_square, "is", str(resp) + ".")


""" CHALLENGE 2 """
to_print = 1.0056
def print_string(x):
    # Prints a string.
    print(str(x))

#print("Next I will print a string...")
#string_var = print_string(to_print)


""" CHALLENGE 3 """
param1 = "horse"
param2 = "owl"
param3 = "pig"

def mixed_params(x, y, z, a="cat", b="dog"):
    # Prints 3 required parameters and two optional parameters.
    print(x ,y, z, a, b)

#mixed_params(param1, param2, param3)
#mixed_params(param1, param2, param3, "mouse", "frog")


""" CHALLENGE 4 """
int_var = 3
def int_div_two(x):
    # Returns the input value divided by 2.
    return x/2

def int_mult_four(y):
    # Returns the input value multiplied by 4.
    return y*4

var1 = int_div_two(int_var)
var2 = int_mult_four(var1)
#print("Input: " + str(int_var) + " | Div2: " + str(var1)  + " | Mult4: " + str(var2))


""" CHALLENGE 5"""
string_var = "ghost"
#string_var = "7.5"
def stringToFloat(x):
    # Tries to return the input value as a float, else returns error message.
    try:
        return float(x)
    except ValueError:
        print("Error: Value must be a number.")

print_var = stringToFloat(string_var)
print(print_var)


