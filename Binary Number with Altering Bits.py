
class solution:
    
    def hasAlteringBits(self,n:int) -> bool:
        
        if n >=1:
            return ((n & (n >>1))) == 0
        
        else:
            return 
        