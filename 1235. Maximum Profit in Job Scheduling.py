'''
1235. Maximum Profit in Job Scheduling

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:



Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104
'''

class Solution:
    def jobScheduling1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))], key=lambda x: x[0])
        heap = []
        currentProfit = 0
        maxProfit = 0
        for start, end, profit in jobs:
            # Calculate the total profit of all the jobs that would have end by this time(start: startTime of current job) 
            while heap and heap[0][0] <= start:
                _, tempProfit = heapq.heappop(heap)
                currentProfit = max(currentProfit, tempProfit)
            
            # Push the job into heap to use it further. It's profit would be definitely currentProfit + profit(of current job)
            heapq.heappush(heap, (end, currentProfit + profit))
            maxProfit = max(maxProfit, currentProfit + profit)

        return maxProfit

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)))
        startTime = [jobs[i][0] for i in range(n)]

        @lru_cache(None)
        def dp(i):
            if i == n: return 0
            ans = dp(i + 1)  # Choice 1: Don't pick

            j = bisect_left(startTime, jobs[i][1])
            ans = max(ans, dp(j) + jobs[i][2])  # Choice 2: Pick
            return ans

        return dp(0)