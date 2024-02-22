'''
713. Subarray Product Less Than K
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
'''
'''
For those who are confused with ans += right - left + 1 in "Sliding Window" 
approach. Because the element pointed by the "right" is the new one we 
are investigating, as long as we find a subarray with prod < k after 
being divided by nums[left], ans should be increased by the length
of the subarray because the product is ever increasing.
For example, [10,5,2,6], when right points to 6, left points to 5,
ans added 3, which is due to [5,2,6],[2.6],and[6].
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1:
            return 0
        
        prod = 1
        ans = left = 0
        for right,val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
        