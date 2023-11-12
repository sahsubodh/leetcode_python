'''
698. Partition to K Equal Sum Subsets
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
 

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].

'''

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #prune 1
        if sum(nums) % k != 0:
            return False

        #prune 2 - will call backtracking less if we reverse sort it
        nums.sort(reverse = True)
        target = sum(nums) / k
        visited= set()

        def backtrack(idx, count, currSum):
            if count == k:
                return True

            if target == currSum:
                return backtrack(0, count + 1, 0)

            for i in range(idx, len(nums)):
                
                # skip duplicates if last same number was skipped
                if i > 0 and (i - 1) not in visited and nums[i] == nums[i - 1]:
                    continue

                if i in visited or currSum + nums[i] > target:
                    continue

                visited.add(i)

                if backtrack(i + 1, count, currSum + nums[i]):
                    return True
                
                visited.remove(i)

            return False


        return backtrack(0, 0, 0)