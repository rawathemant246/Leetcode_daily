'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Finding needle in haystack  this is a string searching problem.

'''
# Brute Force Approach

class Solution1:
    def strStr(self, haystack:str, needle:str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack)- len(needle)+1):   # range of haystack - needle + 1  we added 1 because we need to check the last element also
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
# Time complexity: O(n*m) where n is the length of haystack and m is the length of needle

# Another Approach is using python find() function

class Solution2:
    def strStr(self, haystack:str, needle:str) -> int:
        return haystack.find(needle)
# Time complexity: O(n) where n is the length of haystack


# Another Approach is using KMP Algorithm

