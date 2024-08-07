from typing import List

class Solution(object):
    
    def twosum(self, nums:List[int], target:int) -> List[int]:
        num_indices = {}
        
        
        for i, num in enumerate(nums):
            
            if target - num in num_indices:
                
                return [num_indices[target-num], i]
            
            num_indices[num] = i
        
        return []

solution = Solution()
result = solution.twosum([1,2,3,4], 6)
print(result)
