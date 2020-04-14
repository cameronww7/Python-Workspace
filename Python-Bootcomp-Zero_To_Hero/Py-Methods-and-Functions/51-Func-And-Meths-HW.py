from __future__ import print_function

"""
 Prompt 51-Func-And-Meths-HW
"""

print("51-Func-And-Meths-HW")

"""
Nested Statements and Scope
Now that we have gone over writing our own functions, it's important 
to understand how Python deals with the variable names you assign. 
When you create a variable name in Python the name is stored in a 
name-space. Variable names also have a scope, the scope determines 
the visibility of that variable name to other parts of your code.
"""



def pr1(xVal):
    # Write a function that computes the volume of a sphere given its radius.
    # 4/3 * xVal ^3
    print("\nProblem 1")

    return (4/3) * 3.14 * (xVal**3)

print(pr1(3))



def pr2(xHigh, xLow, xNum):
    # Write a function that checks whether a number is in a given range (inclusive of high and low)
    print("\nProblem 2")
    print("Passed in {}, {}, {}".format(xHigh, xLow, xNum))

    middle = (xHigh + xLow) / 2
    print("Middle : {}".format(middle))

    if middle < xNum:
        valReturn = "HIGH"
    else:
        valReturn = "LOW"

    if xNum <= xHigh and xNum >= xLow:
        valReturn = valReturn + " - Yes it is IN Range"
    else:
        valReturn = valReturn + " - No it is NOT Range"

    return valReturn



print(pr2(5, 1, 3))
