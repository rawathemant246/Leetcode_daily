'''
This approach is not optimized because it repeatedly calculates the frequency of each element in the list using nums.count(x). This results in a significant performance hit for larger lists.


'''
from typing import List
from collections import Counter

class solution:
    def frequencySort(self, nums:List[int])->List[int]:
        return sorted(nums, key=lambda x: (nums.count(x), -x))

if __name__ == "__main__":
    s = solution()
    print(s.frequencySort([1,1,2,2,2,3])) # [3,1,1,2,2,2]
    print(s.frequencySort([2,3,1,3,2])) # [1,3,3,2,2]
    print(s.frequencySort([-1,1,-6,4,5,-6,1,4,1])) # [5,-1,4,4,-6,-6,1,1,1]
    


'''
This approach is optimized because it calculates the frequency of each element in the list only once using Counter(nums). This results in a significant performance improvement for larger lists.
'''
class solution1:
    def frequencySort(self, nums:List[int])->List[int]:
        frequncy = Counter(nums)
        return sorted(nums, key=lambda x: (frequncy[x], -x))