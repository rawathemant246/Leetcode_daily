from typing import List


class Solution:
    
    def missingnumber(self, nums:List[int])-> int:    # missing number max number se bi bda ho sktaa h isliye n*(n+1)//2 use kiya h sum of natural numbers
        
        n = len(nums)
        
        
        total_sum = n*(n+1)//2
        
        return total_sum -sum(nums)
    

if __name__ == "__main__":
    
    solution = Solution()
    
    print(solution.missingnumber([3,0,1]))
    
    print(solution.missingnumber([0,1]))
    
    print(solution.missingnumber([9,6,4,2,3,5,7,0,1]))
    
    print(solution.missingnumber([0]))
    
    print(solution.missingnumber([1]))
    
    print(solution.missingnumber([0,1,2,3,4,5,6,7,8,9,11]))
    
    print(solution.missingnumber([0,1,2,3,4,5,6,7,8,9,10]))