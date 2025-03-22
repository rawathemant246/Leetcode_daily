'''
Given a string s, find the length of the longest substring without duplicate characters.

 Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


use the two pointer approach to solve this problem. The two pointer approach is a really efficient technique which is especially useful for strings and arrays. The technique uses two pointers to traverse the string or array and is really useful when you need to find a contiguous subarray or substring.

'''

class Solution:
    def lengthofSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0 
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left +=1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
# Time complexity: O(n)
# Space complexity: O(min(n, m)) where m is the size of the character set
# The space complexity is O(min(n, m)) because the size of the character set is fixed and will not exceed 26 characters.

if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthofSubstring(s))
    s = "bbbbb"
    print(Solution().lengthofSubstring(s))
    s = "pwwkew"
    print(Solution().lengthofSubstring(s))
    s = " "
    print(Solution().lengthofSubstring(s))
    s = "au"
    print(Solution().lengthofSubstring(s))
    s = "aab"
    print(Solution().lengthofSubstring(s))
    s = "dvdf"
    print(Solution().lengthofSubstring(s))
    s = "tmmzuxt"
    print(Solution().lengthofSubstring(s))
    s = "abba"
    print(Solution().lengthofSubstring(s))
    s = "abcabcbb"
    print(Solution().lengthofSubstring(s))
    s = "bbbbb"
    print(Solution().lengthofSubstring(s))
    s = "pwwkew"
    print(Solution().lengthofSubstring(s))
    s = " "
    print(Solution().lengthofSubstring(s))
    s = "au"
    print(Solution().lengthofSubstring(s))
    s = "aab"
    print(Solution().lengthofSubstring(s))
    s = "dvdf"
    print(Solution().lengthofSubstring(s))
    s = "tmmzuxt"
    print(Solution().lengthofSubstring(s))
    s = "abba"
    print(Solution().lengthofSubstring(s))
    s = "abcabcbb"
    print(Solution().lengthofSubstring(s))
    s = "bbbbb"
    print(Solution().lengthofSubstring(s))
    s = "pwwkew"
    print(Solution().lengthofSubstring(s))
    s = " "
    print(Solution().lengthofSubstring(s))
    s = "au"
    print(Solution().lengthofSubstring(s))
    s = "aab"
    print(Solution().lengthofSubstring(s))
    s = "dvdf"
    print(Solution().lengthofSubstring(s))
    s = "tmmzuxt"
    print(Solution().lengthofSubstring(s))
    s = "abba"
    print(Solution().lengthofSubstring(s))
    s = "abcabcbb"
    print(Solution().lengthofSubstring(s))
    s = "bbbbb"
    print(Solution().lengthofSubstring(s))
    ####
    