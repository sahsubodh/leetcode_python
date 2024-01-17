'''
1160. Find Words That Can Be Formed by Characters
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
'''

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = [0] * 26
        for c in chars:
            counts[ord(c) - ord("a")] += 1
        
        ans = 0
        for word in words:
            word_count = [0] * 26
            for c in word:
                word_count[ord(c) - ord("a")] += 1
            
            good = True
            for i in range(26):
                if counts[i] < word_count[i]:
                    good = False
                    break
            
            if good:
                ans += len(word)
            
        return ans