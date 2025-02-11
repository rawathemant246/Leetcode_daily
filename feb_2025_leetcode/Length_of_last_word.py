'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

How to solve this problem:

1. remove the trailing spaces from the string  (from starting and ending)
2. initialize a counter to to counter the number of character 
and if there is a space then reset the counter 

'''

class Solution:
    def lengthofLastWord(self, s:str) -> int:

        s = s.rstrip()

        if not s:
            return 0
        
        count = 0

        for char in reversed(s):
            if char == " ":
                count +=1
            
            else:
                break
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.lengthofLastWord("Hello World"))
    print(s.lengthofLastWord("   fly me   to   the moon  "))
    print(s.lengthofLastWord("luffy is still joyboy"))