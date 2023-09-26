'''
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: 
            return []

        c1, c2, candidate1, candidate2 = 0, 0, None, None
        for n in nums:
            if n == candidate1:
                c1 += 1
            elif n == candidate2:
                c2 += 1
            elif c1 == 0:
                candidate1 = n
                c1 += 1
            elif c2 == 0:
                candidate2 = n
                c2 += 1                
            else:
                c1 -= 1
                c2 -= 1
            
        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                result.append(c)
        
        return result

        