'''
664. Strange Printer
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
'''

class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}

        def check(i, j):
            if (i, j) not in memo:
                if i > j:
                    return 0
                
                res = 1 + check(i, j-1)
                for k in range(i,j):
                    if s[k] == s[j]:
                        res = min(res, check(i, k-1) + check(k, j-1))
                memo[(i,j)] = res
            
            return memo[(i, j)]
        
        s = re.sub(r'(.)\1*', r'\1', s)
        return check(0, len(s) - 1)