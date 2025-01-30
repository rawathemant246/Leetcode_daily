from typing import List 

class Solution:
    
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for i, num in enumerate(sorted(set(arr))):    # set(arr) will remove the duplicates and sorted will sort the array
            rank.setdefault(num, i+1) # setdefault will set the value of num to i+1 if it is not already present in the dictionary
        return [rank[num] for num in arr]

if __name__ == "__main__":
    arr = [40,10,20,30]
    s = Solution()
    print(s.arrayRankTransform(arr))

# Time complexity: O(nlogn)