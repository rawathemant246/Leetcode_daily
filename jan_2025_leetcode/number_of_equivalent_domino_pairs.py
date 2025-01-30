from typing import List
from collections import Counter


class Solution:
    
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes = [tuple(sorted(domino)) for domino in dominoes]
        counter = Counter(dominoes)
        
        return sum(value*(value-1)//2 for value in counter.values())

if __name__ == "__main__":
    
    solution = Solution()
    
    print(solution.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
    
    print(solution.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6],[1,2],[2,1]]))
    
    print(solution.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6],[1,2],[2,1],[1,2],[2,1]]))
    
    print(solution.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6],[1,2],[2,1],[1,2],[2,1],[1,2],[2,1]]))
    
    print(solution.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6],[1,2],[2,1],[1,2],[2,1],[1,2],[2,1],[1,2],[2,1]]))
    
    print(solution.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))


    