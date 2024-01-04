'''
266. Palindrome Permutation
Given a string s, return true if a permutation of the string could form a 
palindrome
 and false otherwise.

 

Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
 

Constraints:

1 <= s.length <= 5000
s consists of only lowercase English letters.

'''

class Solution:

    def canPermutePalindrome(self, s: str) -> bool:
        flag = 0
        counter = collections.Counter(s)
        for occur in counter.values():
            if occur % 2 == 1:
                flag+=1
            if flag >= 2:
                return False
        
        return True    


    def canPermutePalindrome1(self, s: str) -> bool:
        sets = set()
        for char in s:
            if char not in sets:
                sets.add(char)
            else:
                sets.remove(char)
        
        return (len(sets) <= 1)          