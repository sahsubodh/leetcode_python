'''
856. Score of Parentheses

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
'''

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        output,mul = 0,0
        for char in s:
            if char == "(":
                stack.append(0)
            elif char == ")":
                mul = stack.pop()
                if mul == 0:
                    val = 1
                else:
                    val = mul * 2
                if not stack:
                    output += val
                else:
                    stack[-1] += val
        return output
        
