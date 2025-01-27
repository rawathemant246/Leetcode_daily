'''
Contains Duplicate II

nums : List[int]
k : int 
return : bool 

True :  agar different indices pr same element ho means nums[i] == nums[j] and abs(i-j)<=k

example 1

nums = [1,2,3,1] k =3

nums[0] == nums[3]  both are 1  and second condition  abs(0-3) <= 3

example 2 :

nums = [1,2,3,1,2,3] k =2

How to solve this Problem?

1. Create a empty dictionary map.
2. Iterate through the list using enumerate function to get the index and element of the list and store elements as key and index as value in the dictionary.
3. Check if the element is already in the dictionary and the difference between the current index and the index of the element in the dictionary is less than or equal to k.
4. If the above condition is true then return True
5. If we are not able to find any such condition then return False

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