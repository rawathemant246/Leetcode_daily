from typing import List
from itertools import accumulate
class solution:
    
    def antonboundary(self,nums: List[int]) -> int:
        
        return sum(i==0 for i in accumulate(nums))
    
        
        
if __name__ == "__main__":
    test = solution()
    print(test.antonboundary([1,1,0,0,1,1,1,0,1]))
    print(test.antonboundary([1,1,1,1,1,1,1,1,1]))
    print(test.antonboundary([1,0,1,0,1,0,1,0,1]))
    print(test.antonboundary([0,0,0,0,0,0,0,0,0]))
    print(test.antonboundary([1,1,1,1,0,0,0,0,0]))
    print(test.antonboundary([1,1,1,1,1,1,1,1,1]))
        
