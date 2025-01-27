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