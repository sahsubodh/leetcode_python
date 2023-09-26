'''
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

class Solution:
    #BOYER MOORE VOTING ALGO    
    def majorityElement(self, nums: List[int]) -> int:
        res, count = nums[0], 1

        for i in range(1,len(nums)):
            if count == 0:
                res = nums[i]

            count += (1 if nums[i] == res else -1)
        
        return res
        