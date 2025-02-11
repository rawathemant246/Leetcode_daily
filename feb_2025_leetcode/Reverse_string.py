'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

understand the problem:

Probelm requires to reverse the an array of characters in-place, 
i have to modify the array direclty without using any extra memory 
(extra memeory means i cannot use new list or any additional data structure)

s[::-1] creates a new reversed list, but it does not modify the original list s.

two pointer approach:

1. Initialize two pointers left and right to the beginning and end of the array respectively.
2. Swap the characters at the left and right pointers.
3. Move the left pointer to the right and the right pointer to the left.
4. Continue swapping characters until the pointers meet.

'''

from typing import List 
class solution:

    def reverseString(self, s: List[str]) -> None:

        left, right = 0, len(s)-1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left +=1
            right -=1
        
        return None

if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    test = solution()
    print(test.reverseString(s))