from typing import List
from collections import Counter


class Solution:
    
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        
        counts = list(counter.values())
        
        return len(counts) == len(set(counts))
    

if __name__ == "__main__":
    arr = [1,2,2,1,1,3]
    print(Solution().uniqueOccurrences(arr)) # True
    arr = [1,2]
    print(Solution().uniqueOccurrences(arr)) # False
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    print(Solution().uniqueOccurrences(arr)) # True
    arr = [1,2,2,1,1,3]
    print(Solution().uniqueOccurrences(arr)) # True
    arr = [1,2]
    print(Solution().uniqueOccurrences(arr)) # False
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    print(Solution().uniqueOccurrences(arr)) # True
    arr = [1,2,2,1,1,3]
    print(Solution().uniqueOccurrences(arr)) # True
    arr = [1,2]
    print(Solution().uniqueOccurrences(arr)) # False
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    print(Solution().uniqueOccurrences(arr)) # True
    arr = [1,2,2,1,1,3]
    print(Solution().uniqueOccurrences(arr)) # True
    arr = [1,2]
    print(Solution().uniqueOccurrences(arr)) # False
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    print(Solution().uniqueOccurrences(arr)) # True
    arr = [1,2,2,1,1,3]
    print(Solution().uniqueOccurrences(arr)) # True
    arr = [1,2]
    print(Solution().uniqueOccurrences(arr)) # False
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    print(Solution().uniqueOccurrences(arr)) # True
    arr = [1,2,2,1,1,3]
    print(Solution().uniqueOccurrences(arr)) # True
    arr = [1,2]
    print(Solution().uniqueOccurrences(arr)) # False
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    print(Solution().uniqueOccurrences(arr
        
        