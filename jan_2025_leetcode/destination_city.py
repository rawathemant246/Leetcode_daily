
from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        end = set()
        for path in paths:
            start.add(path[0])
            end.add(path[1])
        
        return (end - start).pop()

if __name__ == "__main__":
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    sol = Solution()
    print(sol.destCity(paths))

#test this 