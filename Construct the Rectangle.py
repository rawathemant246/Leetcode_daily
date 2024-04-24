from typing import List
from math import sqrt

class Solution(object):
    
    def constructRectangle(self, area: int) -> List[int]:
        

        for Width in range(int(sqrt(area)), 0, -1):

            if area % Width ==0:

                length = int(area/Width)
            
                if length >= Width:

                    return [length, Width]
        
        return []