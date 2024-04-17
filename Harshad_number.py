

class Solution(object):
    
    def Harshadnumber(self, x:int) -> int:
        
        sum_of_digits = 0
        
        temp =x
        
        
        while temp >0:
            
            last_digit = temp % 10
            
            sum_of_digits += last_digit
            
            temp = temp // 10
            
        
        if x % sum_of_digits ==0:
            
            return sum_of_digits
        
        else:
            return -1
        
        