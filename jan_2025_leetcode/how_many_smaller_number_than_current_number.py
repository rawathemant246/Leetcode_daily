
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        return [sorted_nums.index(n) for n in nums]

if __name__ == "__main__":
    obj = Solution()
    print(obj.smallerNumbersThanCurrent([7,7,7,7,7,7]))
    



# 2. How many smaller number than current number
# Optimize solution 
class Solution1:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        num_to_rank = {}
        
        for i, num in enumerate(sorted_nums):
            if num not in num_to_rank:  
                num_to_rank[num] = i
        
        return [num_to_rank[num] for num in nums]