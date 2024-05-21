from typing import List

class Solution(object):
    
    def sumofEncryptedNumber(self, nums: List[int]) -> int:
        
        def encrypt(x):
            
            s = str(x)
            
            max_digit = max(s)
            
            len_digit = len(s)
            
            
            encypted_number = int(max_digit * len_digit)
            
            return encypted_number
        
        total_sum =0
        
        for number in nums:
            
            total_sum += encrypt(number)
            
        
        
        return total_sum
    

nums1 = [1,2,3]

nums2 = [21,23,42]

test1 = Solution()

result = test1.sumofEncryptedNumber(nums2)

print(result)

#comment
