'''
Write a function to find the longest common prefix string amongst an array
of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Approach to Solve it 

strs = ["flower","flow","flight"]

1. Find the minimum length of the string in the list
2. Iterate over the minimum length of the string
3. Check if all the strings have the same character at the same index
4. If yes, then add the character to the result
5. If no, then return the result

'''
from typing import List

class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        min_length = min([len(s) for s in strs])
        
        for i in range(min_length):
            if len(set([s[i] for s in strs ])) > 1:
                return strs[0][:i]
        
        return strs[0][:min_length]


# Time Complexity - O(N*M) - N is the number of strings and M is the minimum length of the string
# Space Complexity - O(1) - No extra space is used
# if __name__ == "__main__":
#     s = Solution()
#     print(s.longestCommonPrefix(["flower","flow","flight"]))
#     print(s.longestCommonPrefix(["dog","racecar","car"]))
#     print(s.longestCommonPrefix([]))
    

# Optimized Approach
'''
How to optimize this solution?

1. Initialize an empty string to store common prefix.
2. Sort the input list lexigraphically. Because the common prefix will be 
the prefix of the first and last string.
3. Iterate over the first and last string and check if the characters are 
same.
4. If the current character of the first string is not equal to current character
of the last string, then return the common prefix.
5. otherwise append the current character to the empty string.
6. Return the common prefix.


'''

from typing import List

class Solution1:
    
    def longestCommonPrefix(self, strs:List[str]) -> str:
        
        result = ""
        
        strs = sorted(strs)
        
        first = strs[0]
        last = strs[-1]
        
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return result
            result += first[i]
        return result

if __name__ == "__main__":
    s = Solution1()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))
    