'''
523. Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
'''

class Solution:
  
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        remainder = {0:-1}
        
        for i in range(len(nums)):
            total += nums[i]
            r = total%k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] >= 2:
                return True

        return False

    def checkSubarraySum1(self, nums: List[int], k: int) -> bool:
        hashmap = { 0 : -1 } #added for case 1st element is result and we want to avoid length 1 

        presum = 0
        for i, n in enumerate(nums):
            presum += n
            if presum%k in hashmap.keys():
                if i - hashmap[presum%k] >=2:
                    return True
                else:
                    continue

            hashmap[presum%k] = i
        
        return False