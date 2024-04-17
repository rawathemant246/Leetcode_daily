
class Solution:
    def scoreOfString(self, s: str) -> int:
        total_score =0

        N = len(s)

        for i in range (N-1):

            difference = abs(ord(s[i]) - ord(s[i+1]))

            total_score += difference 
        

        return total_score
        
        