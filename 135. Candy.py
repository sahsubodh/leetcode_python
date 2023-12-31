'''
135. Candy
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
'''

class Solution:
    def candy1(self, ratings: List[int]) -> int:
        
        arr = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                arr[i] = arr[i-1] + 1
        
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                arr[i] = max(arr[i],arr[i+1] + 1)

        return sum(arr)


    def candy(self, ratings: List[int]) -> int:
        def count(n):
            return(n*(n+1))//2
        children = len(ratings)
        candies, i = 0, 1
        while i < children:
            inc = dec = 0
            while i < children and ratings[i] > ratings[i-1]:
                inc += 1
                i += 1
            while i < children and ratings[i] < ratings[i-1]:
                dec += 1
                i += 1
            if inc or dec:
                candies += count(inc-1) + max(inc,dec) + count(dec-1)
                continue
            i += 1
        return candies + children