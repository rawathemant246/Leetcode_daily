from typing import List

class Solution(object):
    
    def minimumsubarrayLength(self, nums:List[int], k:int) -> int:
        N = len(nums)
        
        INF = 10**10
        
        
        best = INF 
        
        
        for left in range(N):
            current=0
            
            
            for right in range(left,N):
                
                current |= nums[right]
                
                if current >=k:
                    
                    best = min(best, right-left+1)
            
            if best ==INF:
                
                return -1
    
        
        return best



list_num = [2,1,8]
k=10
test_1 = Solution()

test = test_1.minimumsubarrayLength(list_num, k)


print(test)



        
        
        