"""
Description: You are given a sorted array of integers, nums, which may contain duplicate elements. Your task is 
to find the number of occurrences of a given target number.
Key Requirement: You must solve this problem with a time complexity of O(log n). This means a simple linear 
scan through the array (which would be O(n)) is not an acceptable solution. You must adapt the Binary Search 
algorithm to solve this efficiently.
Hint: A standard binary search will only find one instance of the target. To find the total count, 
you need to find the index of the first and last occurrences of the target. The total count can then 
be calculated using the formula: (last_occurrence_index - first_occurrence_index + 1). You will need to 
create a modified version of binary search to find these two boundaries.

Input:
2 4 5 5 5 8 9
target: 5
Output:
3
"""

# My code

def binary_search(target, my_list):
    start = 0
    end = len(my_list) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_element = my_list[mid]
        
        if target == mid_element:
            return mid
        elif target > mid_element:
            start = mid + 1
        elif target < mid_element:
            end = mid - 1
    return -1

print(binary_search(8, [2,4,5,5,5,8,9]))