from typing import List

class Solution:
    def CountConsistentStrings(self, allowed:str, words:List[str]) -> int:
        allowed = set(allowed)
        count=0
        for word in words:
            if all(ch in allowed for ch in word):
                count+=1
        return count

if __name__ == '__main__':
    allowed = "ab"
    words = ["ad","bd","aaab","baa","badab"]
    s = Solution()
    print(s.CountConsistentStrings(allowed, words)) 
        


# It can be optimized by using set.issubset() method
class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)
        return sum(set(word).issubset(allowed_set) for word in words)
