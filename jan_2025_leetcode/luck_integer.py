from collections import Counter
from typing import List
class Solution:
    def findLucky(self,arr: List[int]) -> int:
        count = Counter(arr)
        lucky = -1
        for key, value in count.items():
            if key == value:
                lucky = max(lucky, key)
        return lucky

if __name__ == "__main__":
    test = Solution()
    arr = [2,2,3,4]
    print(test.findLucky(arr))