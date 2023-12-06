'''
516. Longest Palindromic Subsequence
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
'''

# Time: O(n^2) Space: O(n^2)
# LCS Solution
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubsequence(s, s[::-1])
        
    
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        N, M = len(s1), len(s2)
        dp = [[0] * (M+1) for _ in range(N+1)]

        for i in range(N):
            for j in range(M):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[N][M]

    def longestPalindromeSubseq1(self, s: str) -> int:   
        # Memoization
        cache = {}

        def dfs(i, j):
            if i < 0 or j == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == s[j]:
                length = 1 if i == j else 2
                cache[(i, j)] = length + dfs(i - 1, j + 1)
            else:
                cache[(i, j)] = max(dfs(i - 1, j), dfs(i, j + 1))
            return cache[(i, j)]
        
        for i in range(len(s)):
            dfs(i, i) # odd length
            dfs(i, i + 1) # even length

        return max(cache.values())