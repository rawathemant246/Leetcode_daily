from typing import List, Optional

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class EvenoddTree(object):
    def evenoddtree(self, root: Optional[TreeNode]) --> bool:
        
        current_level = [root]
        
        current_index = 0
        
        next_level = []
        
        
        
        while len(current_level) >0:
            
            if current_index %2 ==0:
                
                if not all(x.val %2 ==0 for x in current_level) or \
                    not all(x.val < y.val for x, y in zip(current_level, current_level[1:])):
                    return False
                
                else:
                    
                    if not all(x.val %2 == 1 for x in current_level) or \
                        not all(x.val > y.val for x, y in zip(current_level, current_level[1:])):
                        
                        return False
        
            next_level = []
            
            for node in current_level:
                
                for child in [node.left, node.right]:
                    
                    if child is not None:
                        next_level.append(child)
            
            current_level = next_level
            
            current_index += 1
        
        return True
    
                        