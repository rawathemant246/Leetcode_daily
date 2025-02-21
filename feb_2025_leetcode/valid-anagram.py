'''
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


'''

from collections import Counter

class Solution:

    def isAnagram(self, s:str, t:str) -> bool:
        return Counter(s) == Counter(t)
    


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print(sol.isAnagram(s,t))