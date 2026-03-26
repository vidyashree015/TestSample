# Example buggy Python code for SonarQube analysis

import os
import sys

def calculate_area(radius):
    # Bug: wrong formula (should be πr^2)
    return 2 * radius * radius  

def insecure_function(user_input):
    # Vulnerability: using eval on user input
    result = eval(user_input)  
    return result

def unused_function(x, y):
    # Code smell: unused function
    return x * y

def long_method(a, b, c, d, e, f, g, h):
    # Code smell: too many parameters
    total = a + b + c + d + e + f + g + h
    print("Total:", total)
    return total

def duplicate_logic(x):
    # Code smell: duplicated logic
    if x > 10:
        print("Large number")
    else:
        print("Small number")

def duplicate_logic_again(x):
    # Same logic repeated (duplication)
    if x > 10:
        print("Large number")
    else:
        print("Small number")

# Bug: division by zero
def risky_division(a, b):
    return a / b  

# Code smell: hardcoded credentials
USERNAME = "admin"
PASSWORD = "12345"






print("Area:", calculate_area(5))
print("Eval result:", insecure_function("2+2"))
print("Division:", risky_division(10, 0))
