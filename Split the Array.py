from typing import List
from collections import Counter


class Solution(object):
    
    
    def ispossiblespilt(self, nums: List[int]) -> bool:
        
        if len(nums) %2 !=0:
            
            raise ValueError("Array length must be even")
        
        
        freq = Counter(nums)
        
        half_length = len(nums)//2
        
        nums1 = set()
        nums2 = set()
        
        
        singletons = []
        
        for num, count in freq.items():
            if count >2:
                nums1.add(num)
                nums2.add(num)
            
            elif count==1:
                singletons.append(num)
        
        for num in singletons:
            
            if len(nums1)< half_length:
                nums1.add(num)
            
            else:
                nums2.add(num)
                
        
        if len(nums1) == half_length and len(nums2) == half_length:
            return True
        else:
            return False