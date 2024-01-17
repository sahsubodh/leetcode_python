'''
2472. Maximum Number of Non-overlapping Palindrome Substrings

You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.
Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.
 

Constraints:

1 <= k <= s.length <= 2000
s consists of lowercase English letters.
'''

class Solution:
    def maxPalindromes(self, S: str, k: int) -> int:
        N, intervals, last, ans = len(S), [], -inf, 0
        for center in range(2 * N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                if right + 1 - left >= k: 
                    intervals.append((left, right + 1))
                    break
                left -= 1
                right += 1
        for x, y in intervals:
            if x >= last:
                last = y
                ans += 1
            else:
                if y < last: last = y
        return ans
        