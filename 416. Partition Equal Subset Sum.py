'''
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        target = total/2   #target sum 
        s= set([0])          #stores the sums of the subsets
        
        for n in nums:
            sums_with_n = []    #stores the sums of the subsets that contain n
            for i in s:
                if i+n == target: return True
                if i+n < target:
                    sums_with_n.append(i+n)
            s.update(sums_with_n)
        return False    
        