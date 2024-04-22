from typing import List

class solution(object):
    def resultArray(self, nums: List[int] ) -> List[int]:
        
        N = len(nums)
        
        ar1 = [nums[0]]
        
        ar2 = [nums[1]]
        
        
        for i in range(2, N):
            
            if ar1[-1] > ar2[-1]:
                
                ar1.append(nums[i])
            
            else:
                
                ar2.append(nums[i])
        
        return ar1 + ar2
        