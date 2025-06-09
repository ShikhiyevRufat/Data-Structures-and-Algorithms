"""
Problem Description: Implement a function linear_search that performs a linear search on a 
list to find a given value. The function should return the index of the first occurrence of the value in the list, 
or -1 if the value is not found.

linear_search([3, 7, 2, 5], 2) should return 2

linear_search([1, 1, 2, 1], 1) should return 0

linear_search([], 5) should return -1

linear_search([4, 2, 8], 6) should return -1
"""

# My code

def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i 
    return -1

print(linear_search([3, 7, 2, 5], 2))