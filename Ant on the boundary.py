from typing import List
from itertools import accumulate
class solution:
    
    def antonboundary(self,nums: List[int]) -> int:
        
        return sum(i==0 for i in accumulate(nums))
    
        