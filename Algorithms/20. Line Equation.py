"""
Problem Description:

You are given the slope m and the y-intercept b of a line, along with a value x. Your task is to 
calculate and return the value of y using the equation of a line in slope-intercept form:

y=mx+b

Input: slope = 2, intercept = 3, x = 4
Output: 11.0
 
Input: slope = 1.5, intercept = -2, x = 2
Output: 1.0
"""

# My code

def calculate_y(slope, intercept, x):
    return slope*x+intercept

print(calculate_y(2, 3, 4))