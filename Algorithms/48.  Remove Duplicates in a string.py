"""
Problem Description: You are given a string s. Your task is to remove duplicate characters from the string 
while preserving the order of the first occurrences and return the modified string.

Input: "programming"
Output: "progamin"
 
Input: "Hello, World!"
Output: "Helo, Wrd!"
"""

def remove_duplicates(s):
    return "".join(dict.fromkeys(s))


print(remove_duplicates("programming"))