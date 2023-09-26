'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If the input list is empty, there's no common prefix.
        if not strs:
            return ""

        # Find the minimum length of strings in the list
        min_len = min(len(s) for s in strs)

        # Initialize the common prefix
        common_prefix = ""

        # Iterate through characters up to the minimum length
        for i in range(min_len):
            # Get the current character to compare
            char_to_compare = strs[0][i]

            # Check if this character is common in all strings
            for s in strs:
                if s[i] != char_to_compare:
                    return common_prefix  # If not, return the common prefix found so far

            # If the character is common in all strings, add it to the common prefix
            common_prefix += char_to_compare

        return common_prefix

    def longestCommonPrefix1(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += strs[0][i]

        return res
        