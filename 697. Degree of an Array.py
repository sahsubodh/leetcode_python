'''
697. Degree of an Array
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''

class Solution:

    def findShortestSubArray(self, nums):
        d       = defaultdict(list) # Dictionary with [indexes] where each label appears
        m, best = 1, 1              # m = record degree, best = shortest span (for m)
        for i,x in enumerate(nums):
            d[x].append(i) # Add index to respective sub-array
            L = len(d[x])   # Track length of sub-array at label = x
            if L>m:
                # Initialize new Record
                m = L
                best = i - d[x][0] + 1
            elif L == m:
                # Pick best at highest degree
                best = min(best , i - d[x][0] + 1)
        return best
        
    def findShortestSubArray1(self, nums: List[int]) -> int:
        #group indexes by element type
        d = defaultdict(list)
        for index,value in enumerate(nums):
            d[value].append(index)
        
        #find highest degree
        m = max([ len(val) for val in d.values()])

        #find shortest span of max degree
        shortest = len(nums)

        for val in d.values():
            if len(val) == m:
                shortest = min(shortest, val[-1] - val[0] + 1)
        return shortest
        