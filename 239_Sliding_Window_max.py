'''
239 Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/description/

'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l , r = 0, 0
 
        q = collections.deque() # store index of max value

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            #remove left from window
            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1
        return output






