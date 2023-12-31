'''
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring.
Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
'''

class Solution:

    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
                
        l,r=0,0        
        # traverse the string from left to right
        for i in range(len(s)):
            if s[i] == '(':
                l+=1
            else:
                r+=1                        
            if l == r:# valid balanced parantheses substring 
                max_length=max(max_length, l*2)
            elif r>l: # invalid case as ')' is more
                l=r=0
        
        l,r=0,0        
        # traverse the string from right to left
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                l+=1
            else:
                r+=1            
            if l == r:# valid balanced parantheses substring 
                max_length=max(max_length, l*2)
            elif l>r: # invalid case as '(' is more
                l=r=0
        return max_length

    def longestValidParentheses1(self, s: str) -> int:
        max_length = 0
        stack=[-1] # initialize with a start index
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack: # if popped -1, add a new start index
                    stack.append(i)
                else:
                    max_length=max(max_length, i-stack[-1]) # update the length of the valid substring
        return max_length        