'''
	Given : 
				arr : List[int]
				target : List[int] 
				len(arr) == len(target)
Reverse the arr into steps of subarray  
				Return : True if arr can be converted to target, else False
'''

from typing import List
from collections import Counter

# Complexity Analysis
# Time complexity : O(nlogn)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
 

if __name__ == "__main__":
    target = [2,3,9,11]
    arr = [2,3,9,8]
    sol = Solution()
    print(sol.canBeEqual(target, arr)) 

# Complexity Analysis
# Time complexity : O(n)
class Solution1:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)