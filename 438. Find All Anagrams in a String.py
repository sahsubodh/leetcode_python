'''
438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        startIndex = 0
        pMap, sMap = {}, {}
        res = []
        
        for char in p:
            pMap[char] = 1 + pMap.get(char, 0)
        
        for i in range(len(s)):
            sMap[s[i]] = 1 + sMap.get(s[i], 0)

            if i >= len(p) - 1:
                if sMap == pMap:
                    res.append(startIndex)
                
                # If current character is in sMap, remove it and re-update the map.
                if s[startIndex] in sMap:
                    sMap[s[startIndex]] -= 1
                    if sMap[s[startIndex]] == 0:
                        del sMap[s[startIndex]]
                startIndex += 1
        
        return res
