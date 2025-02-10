'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

how to solve this isko bi two pointer approach se solve kr skte h

but strings are immutable in python, so we have to convert the string to a list of characters first,

'''
from typing import List

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s_new = list(s)

        left, right = 0, len(s_new)-1

        while left < right:
            while left < right and s_new[left] not in vowels:
                left += 1
            while left < right and s_new[right] not in vowels:
                right -= 1

            s_new[left], s_new[right] = s_new[right], s_new[left]

            left += 1
            right -= 1

        return "".join(s_new)


if __name__ == "__main__":
    s = "IceCreAm"
    test = Solution()
    print(test.reverseVowels(s))