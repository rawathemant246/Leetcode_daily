from collections import deque
from typing import List

class Solution(object):
    
    def  maxoperations(self, nums: List[int]) -> int:
        
        N = len(nums)
        q = deque(nums)
        
        maxx = q[0] + q[1]
        
        count = 0 
        
        
        while len(q) >=2  and  q[0] + q[1] == maxx:
            
            q.popleft()
            q.popleft()
            count +=1
        
        
        return count
    


s = [3,2,1,4,5]
nums = [3,2,6,1,4]

test_1 = Solution()

test = test_1.maxoperations(nums)


print(test)
    
    