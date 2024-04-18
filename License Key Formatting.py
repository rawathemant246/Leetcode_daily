

class Solution(object):
    
    def LicenseKeyFormat(self, s: str, k:int) -> str:
        
        s = s.replace("-","").upper()
        
        
        results = []
        
        current_group = []
        
        
        for i in reversed(s):
            
            current_group.append(i)
            
        
            if len(current_group) == k:
            
                results.append("".join(reversed(current_group)))
            
                current_group = []
        
        if current_group:
            
            results.append("".join(reversed(current_group)))
            
        
        return "-".join(reversed(results))
    
    
    
    # Example usage
s1 = "5F3Z-2e-9-w"
k1 = 4

test1 = Solution()

res = test1.LicenseKeyFormat(s1,k1)
print(res)

s2 = "2-5g-3-J"
k2 = 2
res2 = test1.LicenseKeyFormat(s2,k2)
print(res2)