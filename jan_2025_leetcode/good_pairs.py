from collections import Counter
from typing import List


class Solution:
    def numIdenticalpairs(self, numbers: List[int])-> int:
        freq = Counter(numbers)
        return sum([v*(v-1)//2 for v in freq.values()])

if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1, 3]
    obj = Solution()
    print(obj.numIdenticalpairs(nums))