'''
115. Distinct Subsequences
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
 
Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
'''

class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        
        M, N = len(s), len(t)
        
        # Dynamic Programming table
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)] 
        
        # Base case initialization
        for j in range(N + 1):
            dp[M][j] = 0
        
        # Base case initialization
        for i in range(M + 1):
            dp[i][N] = 1
        
        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
          
                # Remember, we always need this result
                dp[i][j] = dp[i + 1][j]

                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
            
        return dp[0][0]

    def numDistinct1(self, s: str, t: str) -> int:
        cache = {}
        # if t is empty then we can use s with one way - not using it
        for i in range(len(s)+1):
            cache[(i,len(t))] = 1
        # it s is empty then we cant make t - so 0 ways    
        for j in range(len(t)):
            cache[(len(s),j)] = 0
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    cache[(i,j)] = cache[(i+1, j+1)] + cache[(i+1, j)]
                else:
                    cache[(i, j)] = cache[(i + 1, j)]
        return cache[(0,0)]

