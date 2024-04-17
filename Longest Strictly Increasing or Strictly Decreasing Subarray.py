from typing import List
class Solution(object):
    
    def longestMonotonicSubarray(self, nums:List[int]) -> int:
        
        if not nums:
            return 0
        
        max_length =1
        current_incr_length = 1
        current_decr_length =1 
        
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_incr_length +=1
                current_decr_length =1
            
            elif nums[i] < nums[i-1]:
                current_decr_length +=1
                current_incr_length =1
            else:
                current_incr_length=1
                current_decr_length=1
            
            max_length = max(max_length,current_incr_length, current_decr_length)
            
            return max_length


nums = [3,3,3,3]

test1 = Solution()

results = test1.longestMonotonicSubarray(nums)

print(results)