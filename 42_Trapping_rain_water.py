'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
'''

class Solution:
    def trap(self, height: List[int]) -> int:

        low,high = 0, len(height) - 1
        totalWater = 0
        maxLeft, maxRight = 0,0

        while low < high:
            maxLeft = max(maxLeft,height[low])
            maxRight = max(maxLeft,height[high])

            if maxLeft < maxRight:
                totalWater += maxLeft - height[low]
                low += 1
            else:
                totalWater += maxRight - height[high]
                right -= 1      

        return totalWater    