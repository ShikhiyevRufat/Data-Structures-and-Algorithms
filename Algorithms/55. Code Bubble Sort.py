"""
Description: You are given a list of integers. Write a Python function to sort the list in ascending 
order using the Bubble Sort algorithm. Bubble Sort repeatedly steps through the list, compares adjacent elements, 
and swaps them if they are in the wrong order. The process is repeated until the list is sorted.

Input: lst = [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]

Input: lst = [5, 1, 4, 2, 8]
Output: [1, 2, 4, 5, 8]
"""

# My code

def bubble_sort(lst):
    my_lst = len(lst)

    for i in range(my_lst):
        for j in range(my_lst - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))