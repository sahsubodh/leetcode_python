'''
525. Contiguous Array
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
            '''
            Hey, it is important to init, {0.-1}, basically, 
            it is to imply that sum is 0 before we start the array summation.
            Array begins at 0, so a index before the array begins is -1. 
            This helpful incase your sum adds up to 0, then {0,-1} will be found in the haspmap.

            eg: take [0,1] input
            sum will be: -1, 0
            note sum becomes 0 at index 1 and we have 0 in hashMap wilt
            location/index -1. so max len will be: current index - location stored 
            in hashmap for sum 0, ie 1-(-1) = 2.
            '''

        dict = {  0: -1 }

        for index, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in dict:
                max_length = max(max_length, index - dict[count])
            else:
                dict[count] = index
        
        return max_length
        