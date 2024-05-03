from typing import List
class Solution:
    
    def modifiedmatrix(self, matrix : List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        mx = [-1]*cols
        
        
        for i in range(rows):
            for j in range(cols):
                
                mx[j] = max(mx[j], matrix[i][j])
                
        
        for i in range(rows):
            for j in range(cols):
                
                if matrix[i][j] == -1:
                    
                    matrix[i][j] = mx[j]
        
        return matrix