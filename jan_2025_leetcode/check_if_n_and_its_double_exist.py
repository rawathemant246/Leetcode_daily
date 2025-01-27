'''
Problem : Check if N and its double Exists

Given : arr : List[int]

- i != j
- 0 <= i, j < arr.length
- arr[i] == 2 * arr[j]    This is the main condition to check 
return : bool

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.


How to solve this problem?

- We will use a set to store the elements of the list 
- We will iterate through the list
- we will check if the double of the number is in the set or the half of the number is in the set
- If any of the above conditions are true then we will return True
- If we are not able to find any such condition then we will return False

'''



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
    
