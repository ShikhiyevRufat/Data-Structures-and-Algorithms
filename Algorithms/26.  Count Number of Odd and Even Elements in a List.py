"""
Count Even and Odd Numbers in a List

You are given a list of integers. Write a Python program that counts and returns the number of even 
and odd numbers in the list.

Input: lst = [1, 2, 3, 4, 5]
Output: (2, 3)

There are 2 even numbers: 2, 4
There are 3 odd numbers: 1, 3, 5
"""

# My code

def count_even_odd(lst):
    count_even = 0
    count_odd = 0
    
    for i in lst:
        if i % 2 == 0:
            count_even += 1 
        else:
            count_odd += 1 
    return count_even, count_odd

print(count_even_odd([1, 2, 3, 4, 5]))