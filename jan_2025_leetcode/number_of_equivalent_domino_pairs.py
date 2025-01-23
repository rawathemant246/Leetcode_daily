from typing import List
from collections import Counter


class Solution:
    
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes = [tuple(sorted(domino)) for domino in dominoes]
        counter = Counter(dominoes)
        
        return sum(value*(value-1)//2 for value in counter.values())