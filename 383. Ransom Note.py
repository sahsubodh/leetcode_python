'''
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        fmag = [0]*26
        fran = [0]*26
        for i in range(len(magazine)):
            if i < len(ransomNote):
                fran[ord(ransomNote[i]) - ord('a')] += 1
            fmag[ord(magazine[i]) - ord('a')] += 1
            
        for i in range(26):
            if fran[i] > fmag[i]:
                return False
        return True    

    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        letters = collections.Counter(magazine)

        for c in ransomNote:
            if not letters[c]:
                return False
            
            letters[c] -= 1
        
        return True