'''
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

'''

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        window_start = 0
        min_size = float('inf')
		
		# summation of subarray
        summation = 0
        
        # use sliding window to update min_size of of valid subarray
        for window_end, number in enumerate(nums):
            
            summation += number
            
            while summation >= s:
                
                # keep shrinking window size if summation is valid
                min_size = min( min_size, window_end - window_start + 1)
                
                # update subarray sum
                summation -= nums[window_start]
                
                window_start += 1
                
        
        if min_size == float('inf'):
            
            # no solution
            return 0
        
        else:
            
            return min_size
                