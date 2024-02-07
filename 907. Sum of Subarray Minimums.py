'''
907. Sum of Subarray Minimums
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
'''

class Solution:
#https://leetcode.com/problems/sum-of-subarray-minimums/solutions/257811/python-o-n-slightly-easier-to-grasp-solution-explained
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = [0]*(len(arr))
        
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            j = stack[-1] if stack else -1 # edge case when stack is empty
            res[i] = res[j] + (i-j)*arr[i]
            
            stack.append(i)
            
        return sum(res) % (10**9+7)

    def sumSubarrayMins2(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        arr = [ float("-inf") ] + arr + [ float("-inf") ]
        stack = [] #(index,num)

        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j, mval = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = (res + mval * left *right) % MOD

            stack.append((i,n))

        return res

    def sumSubarrayMins1(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        stack = [] #(index,num)

        for i, n in enumerate(arr):
            while stack and n < stack[-1][1]:
                j, mval = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = i - j
                res = (res + mval * left *right) % MOD

            stack.append((i,n))

        for i in range(len(stack)):
            j, nval = stack[i]
            left = j - stack[i-1][0] if i > 0 else j + 1
            right = len(arr) - j
            res = (res + nval * left *right) % MOD

        return res
        