# Optimized approach with the time complexity of O(n)
# which uses the sliding window techniques

from collections import Counter

class Solution(object):
    def maximumLengthSubstring(self, s):
        N = len(s)
        best = 0
        left = 0
        char_count = Counter()
        
        for right in range(N):
            char_count[s[right]] += 1
            
            # If any character count exceeds 2, contract the window from the left
            while max(char_count.values()) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            
            # Update the best length of the substring
            best = max(best, right - left + 1)
        
        return best


s = "bcbbbcba"

test_1 = Solution()

test = test_1.maximumLengthSubstring(s)


print(test)