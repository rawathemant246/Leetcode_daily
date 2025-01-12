from typing import List


class Solution:
    
    def majorityElement(self, nums:List[int])-> int:
        
        n = len(nums)
        
        nums.sort()
        
        return nums[n//2]
        
      
'''
nums [2,2,1,1,1,2,2]

sort kroge toh [1,1,1,2,2,2,2]

n//2 = 7//2 = 3

toh 3rd index pe 2 h jo majority element h


When you sort the array, the majority element (which appears more than n/2 times) 
must occupy the middle index after sorting. This is because the majority element 
dominates the array.

Since the problem guarantees the existence of a majority element, 
simply returning nums[n // 2] after sorting is correct.

Imagine the array as follows:
Before sorting: [3, 3, 4, 2, 3, 3, 3]
After sorting: [2, 3, 3, 3, 3, 3, 4]
The middle index (n // 2) is always occupied by the majority element (3) because it appears 
more than half the time.
'''