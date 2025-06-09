"""
Problem Description: You are given a string s. Your task is to return the reversed version of the string.

Input: "hello"
Output: "olleh"
 
Input: "Python"
Output: "nohtyP"
"""

# My code

def reverse_string(s):
    b = list(s)
    b.reverse()
    return "".join(b)

print(reverse_string("hello"))