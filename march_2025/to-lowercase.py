'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"

'''

class Solution:
    def tolowercase(self, s:str) -> str:
        return s.lower()

solution = Solution()
result = solution.tolowercase("Hello")
print(result)

result = solution.tolowercase("here")
print(result)