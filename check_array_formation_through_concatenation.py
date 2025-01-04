from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {x[0]: x for x in pieces}
        #print(d)
        i=0
        while i < len(arr):
            if arr[i] not in d:
                return False
            piece = d[arr[i]]
            print(piece)
            for x in piece:
                if x != arr[i]:
                    return False
                i +=1
        return True

if __name__ == "__main__":
    arr = [91,4,64,78]
    pieces = [[78],[4,64],[91]]
    print(Solution().canFormArray(arr, pieces)) # True
    arr = [49,18,16]
    pieces = [[16,18,49]]
    print(Solution().canFormArray(arr, pieces)) # False
    arr = [85]
    pieces = [[85]]
    print(Solution().canFormArray(arr, pieces)) # True
    arr = [15,88]
    pieces = [[88],[15]]
    print(Solution().canFormArray(arr, pieces)) # True
    arr = [49,18,16]
    pieces = [[16,18,49]]
    print(Solution().canFormArray(arr, pieces)) # False
    arr = [91,4,64,78]
    pieces = [[78],[4,64],[91]]
    print(Solution().canFormArray(arr, pieces)) # True
    arr = [1,3,5,7]
    pieces = [[2,4,6,8]]
    print(Solution().canFormArray(arr, pieces)) # False
    arr = [1,2,3]
    pieces = [[2],[1,3]]
    print(Solution().canFormArray(arr, pieces)) # False
    arr = [1,2,3]
    pieces = [[1],[3,2]]
    print(Solution().canFormArray(arr, pieces)) # True
    arr = [1,2,3]
    pieces = [[1],[2],[3]]
    print(Solution().canFormArray(arr, pieces)) # True
    arr = [1,2,3]
    pieces = [[1,3],[2]]
    print(Solution().canFormArray(arr, pieces)) # False
    arr = [1,2,3]
    pieces = [[1],[2,3]]
    print(Solution().canFormArray(arr, pieces)) # True
    arr = [1,2,3]
    pieces = [[1],[3],[2]]
    print(Solution().canFormArray(arr, pieces)) # False
    arr = [1,2,3]
    pieces = [[1],[2],[3]]
    print(Solution().canFormArray(arr, pieces)) # True
    arr = [1,2,3]