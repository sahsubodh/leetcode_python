'''
1328. Break a Palindrome

Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.

 

Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
 

Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
'''

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        # there is no way to replace a single character to make "a" not a palindrome
        # because no matter what we change, it is still a palindrome
        if n == 1:
            return ''
        # let's think about n = 2 case, e.g. "bb"
        # in this case, to acheive the lexicographically smallest one
        # we should replace from the left and the best character to use is "a"
        # for "bb", we replace the first "b" to "a" to become "ab"
        
        # let's think about another n = 2 case, e.g. "aa"
        # in this case, to acheive the lexicographically smallest one
        # we should replace from the left and the best character to use is "a"
        # however, for "aa", we cannot use "a" here and the best character to use is "b" now
        # for "aa", we replace the second "a" to "b" to become "ab"
        # why not replace the first "a"? because "ba" is not smallest.
        for i in range(n // 2):
            #  here we know that as long as palindrome[i] is "a", we skip it
            if palindrome[i] != 'a':
                # otherwise, we replace the first character that is not "a"
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        # by the time it reaches here, the possible cases would be like "aaa", "aba" etc. 
        # so that we haven't changed anything in above logic
        # in this case, as mentioned above, the best character to use is "b"
        # and we should replace the last character to achieve the smallest one possible
        return palindrome[:-1] + 'b'