# This approach  have a time complexity of O(n2)
# this is the brute force solution 

from typing import List
from collections import Counter
import collections

class solution(object):
    def maximumlengthSubstring(self, s:str ) -> int:
        N = len(s)
        best=0
        
        for i in range(N):
            f = collections.Counter()
            print(f)
            
            for j in range(i,N):
                f[s[j]] +=1
                print("this is the j loop",f)
                
                if max(f.values()) <=2:
                    best = max(best, j-i +1)
                    print(best)
                else:
                    break
        return best
    
    
s = "bcbbbcba"

test_1 = solution()

test = test_1.maximumlengthSubstring(s)


print(test)

#test this code
