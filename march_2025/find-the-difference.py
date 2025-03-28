'''
You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"

'''

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return (Counter(t) - Counter(s)).popitem()[0]
    
# Time complexity: O(n)
# Space complexity: O(n)

# Using XOR
# Since all characters in s and t cancel out except the extra one, XOR (^) is an efficient solution:
# XOR of two same characters is 0, so the extra character will remain after XORing all characters.
# XOR of two different characters is non-zero, so the extra character will remain after XORing all characters.
class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for ch in s+t:
            res ^= ord(ch)
        return chr(res)

# Time complexity: O(n)
# Space complexity : O(1)
