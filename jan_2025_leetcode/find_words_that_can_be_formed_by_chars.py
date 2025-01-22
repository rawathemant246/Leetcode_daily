from collections import Counter
from typing import List


class Solution:
    
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        char_count = Counter(chars)
        result = 0
        
        for word in words:
            word_count = Counter(word)
            
            
            if all(word_count[char] <= char_count[char] for char in word_count):
                result += len(word)
        
        return result
    
    '''
    
    class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        result = 0
        
        for word in words:
            valid = True
            for char in word:
                # If the character count in `word` exceeds `char_count`, the word is invalid
                if word.count(char) > char_count[char]:
                    valid = False
                    break
            
            if valid:
                result += len(word)
        
        return result
    
    '''