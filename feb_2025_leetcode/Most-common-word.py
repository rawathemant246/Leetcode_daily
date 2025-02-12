'''
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"

How to solve this Problem:

Given :  paragraph : str    paragrah = "Bob hit a ball, the hit BALL flew far after it was hit." 
	 banned : [str]     banned = ["hit"]
	 
	 return : most frequent word that is not banned.
	 
	 1. remove the punctuation, lowercase 
	 2. dictonary create krta  key as words and value their frequency 
	 3. condition check if not in banned return most frequnecy key

'''
from typing import List 
from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower()

        words = paragraph.split()
        word_counts = Counter(words)

        banned = set(banned)

        most_frequent = max((word for word in word_counts if word not in banned), 
                        key=word_counts.get)
        return most_frequent


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    s = Solution()
    print(s.mostCommonWord(paragraph, banned))