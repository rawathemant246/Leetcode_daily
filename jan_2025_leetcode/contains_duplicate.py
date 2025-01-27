'''
Problem : 

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Given : nums : List[int]
return : bool

How to solve this problem?

Approach 1.:

1. Create a dictionary to store the frequency of the elements in the list.
2. Iterate through the dictionary and checks if the count of any element is greater than 1.
3. if the count of any element is greater than 1 then return True
4. If we are not able to find any such element then return False

Approach 2.:

1. Create a empty set seen.
2. Iterate through the list
3. Check if the number is already in the set
4. If the number is already in the set then return True
5. If the number is not in the set then add the number to the set
6. If we are not able to find any such element then return False
'''


from typing import List
from collections import Counter

class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool:
        freq = Counter(nums)
        
        for _, count in freq.items():
            if count >1:
                return True
        
        return False

if __name__ == "__main__":
    solution = Solution()
    
    print(solution.containsDuplicate([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
                                      25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,
                                      47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,
                                      70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,
                                      95,96,97,98,99,100]))


# second method to optimize it more 

class Solution1:
    
    def containsDupicate(self, nums:List[int])-> bool:
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False 