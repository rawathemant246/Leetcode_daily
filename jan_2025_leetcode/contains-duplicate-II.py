'''
Contains Duplicate II

nums : List[int]
k : int 
return : bool 

True :  agar different indices pr same element ho means nums[i] == nums[j]
and abs(i-j)<=k

example 1

nums = [1,2,3,1] k =3

nums[0] == nums[3]  both are 1  and second condition  abs(0-3) <= 3

example 2 :

nums = [1,2,3,1,2,3] k =2

'''

from typing import List


class Solution:
    
    def containsNearbyDuplicate(self, nums: List[int], k:int) -> bool:
        
        map = {}
        
        
        for i, num in enumerate(nums):
            
            if num in map and abs(i - map[num]) <=k:
                return True
            
            map[num] = i
        
        return False
    

if __name__ == "__main__":
    test = Solution()
    print(test.containsNearbyDuplicate([1,2,3,1], 3))
    print(test.containsNearbyDuplicate([1,0,1,1], 1))
    print(test.containsNearbyDuplicate([1,2,3,1,2,3], 2))