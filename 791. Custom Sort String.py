'''
791. Custom Sort String
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

 

Example 1:

Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
Example 2:

Input: order = "cbafg", s = "abcd"
Output: "cbad"
 

Constraints:

1 <= order.length <= 26
1 <= s.length <= 200
order and s consist of lowercase English letters.
All the characters of order are unique.
'''

'''
Actually, this problem has two follow up questions:
Follow up 1: If the custom order S is too large, how to solve it efficiently?
Follow up 2: If the string T is too large, how to solve it efficiently?
'''

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        bucket = [0] * 26
        for char in s:
            bucket[ord(char) - ord('a')] += 1

        sb = []
        for char in order:
            sb.append(char * bucket[ord(char) - ord('a')])
            bucket[ord(char) - ord('a')] = 0
        
        for i in range(26):
            if bucket[i] > 0:
                sb.append(chr(i + ord('a')) * bucket[i])
        
        return "".join(sb)