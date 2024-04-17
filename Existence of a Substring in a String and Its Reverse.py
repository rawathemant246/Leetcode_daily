class Solution(object):
    def substringreverse(self, s:str) -> int:
        N = len(s)
        rev = s[::-1]
        
        for i in range(N):
            
            if s[i-1] + s[i] in rev:
                return True
        
        
        return False
    


s = "leetcode"

test1 = Solution()

check1 = test1.substringreverse(s)

print(check1)



# class Solution(object):
#     def substringreverse(self, s: str) -> bool:
#         if len(s) < 2:  # Early return if it's not possible to have a two-character substring
#             return False

#         # Create a set of all two-character substrings in the reversed string
#         rev = s[::-1]
#         rev_substrings = {rev[i:i+2] for i in range(len(rev) - 1)}

#         # Check if any two-character substring of s exists in rev_substrings
#         for i in range(1, len(s)):  # Start from 1 to use i-1 safely
#             if s[i-1:i+1] in rev_substrings:
#                 return True

#         return False
