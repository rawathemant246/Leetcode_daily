from typing import List
class Solution(object):
    
    def minOperation(self, nums: List[int], k:int ) -> int:
        
        nums.sort()
        
        
        for num in nums:
            
            if num<k:
                
                count +=1
            
            else:
                break
        
        
        return count
    
    
    #comment
    
