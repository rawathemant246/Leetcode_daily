'''
To maintain the relative order 

1. Create a dictionary d with key as the element and value as the index of the element in arr2
2. Sort the arr1 based on the index of the element in arr2
3. If the element is not present in arr2, then assign the index as the length of arr2
4. Return the sorted arr1

'''

from typing import List


class Solution:
    
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        d = {x:i for i, x in enumerate(arr2)}
        
        return sorted(arr1, key=lambda x: (d.get(x, len(arr2)), x))

if __name__ == "__main__":
    obj = Solution()
    assert obj.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
    assert obj.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]) == [22,28,8,6,17,44]
    assert obj.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
    assert obj.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
    assert obj.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
    assert obj.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
    assert obj.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
    assert obj.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
    