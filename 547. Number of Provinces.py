'''
547. Number of Provinces
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''

class UnionFind:
	def __init__(self, n):
		self.parents = [x for x in range(n)]
		self.count = [1 for _ in range(n)]
		self.groups = n

	def find(self, a):
		while a != self.parents[a]:
			self.parents[a] = self.parents[self.parents[a]]
			a = self.parents[a]
		return a

	def union(self, a, b):
		a_root, b_root = self.find(a), self.find(b)

		if a_root == b_root:
			return True

		if self.count[a_root] > self.count[b_root]:
			self.parents[b_root] = a_root
			self.count[a_root] += self.count[b_root]
		else:
			self.parents[a_root] = b_root
			self.count[b_root] += self.count[a_root]
		self.groups -= 1

		return False

class Solution:
	def findCircleNum(self, grid: List[List[int]]) -> int:
		n = len(grid)
		if n < 1 or len(grid[0]) != n:
			return 0

		union = UnionFind(n)

		for i in range(n):
			for j in range(n):
				if grid[i][j] == 1:
					union.union(i,j)

		return union.groups