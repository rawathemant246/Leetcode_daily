from typing import List
from collections import Counter


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
    