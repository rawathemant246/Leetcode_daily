from typing import List
from collections import Counter
class solution:
    
    def TriangleType(self, nums: List[int] ) -> str:
        
        nums.sort()
        
        counting_number = Counter(nums)
        
        
        if nums[0] + nums[1] <= nums[2]:
            return None
        
        
        if len(counting_number) == 1:
            return "Equilateral"
        
        if len(counting_number) == 2:
            return "Isosceles"
        
        return "Scalene"
        