from typing import List


class Solution:
    
    def checkIfExist(self, arr : List[int]) -> bool:    # arr = [10,2,5,3]
        
        seen = set()
        
        for num in arr:      # iterate through the list [10,2,5,3]
            
            if num*2 in seen or (num%2==0 and num//2  in seen) :   # check if the double of the number is in the set or the half of the number is in the set
                return True
            seen.add(num)
        
        return False

if __name__ == "__main__":
    test = Solution()
    print(test.checkIfExist([10,2,5,3]))
    print(test.checkIfExist([7,1,14,11]))
    print(test.checkIfExist([3,1,7,11]))
    
