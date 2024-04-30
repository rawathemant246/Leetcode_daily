from typing import List


class Solution(object):
    
    
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        
        def isGood(i,j):
            
            return words[j].startswith(words[i]) & words[j].endswith(words[i])
        
    
    
        N = len(words)
        
        
        
        count = 0
        
        
        
        for i in range(N):
            
            for j in range(i+1 , N):
                
                if isGood(i,j):
                    
                    count +=1
                    
        return count
    


words = ["a","aba","ababa","aa"]

test1 = Solution()

result = test1.countPrefixSuffixPairs(words)

print(result)
    