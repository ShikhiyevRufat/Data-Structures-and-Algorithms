"""
Problem Description:

You are given a temperature in Celsius. Your task is to convert it to Fahrenheit and return the result.

Formula:

To convert Celsius to Fahrenheit, use the formula:

F = (9/5 * C) + 32

Where F is the temperature in Fahrenheit and C is the temperature in Celsius.

Input: C = 25
Output: 77.0
 
Input: C = 0
Output: 32.0
"""

# My code

def celsius_to_fahrenheit(C):
    return (9/5 * C) + 32

print(celsius_to_fahrenheit(25))