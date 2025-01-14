from typing import List


class Solution:
    
    def checkIfExist(self, arr : List[int]) -> bool:
        
        seen = set()
        
        for num in arr:
            
            if num*2 in seen or (num%2==0 and num//2  in seen) :
                return True
            seen.add(num)
        
        return False

if __name__ == "__main__":
    test = Solution()
    print(test.checkIfExist([10,2,5,3]))
    print(test.checkIfExist([7,1,14,11]))
    print(test.checkIfExist([3,1,7,11]))