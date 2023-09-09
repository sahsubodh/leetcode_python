'''
323. Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
'''

class UnionFind:
    def __init__(self):
        self.f = {}
    
    def findParent(self, x):
        y = self.f.get(x,x)
        if x != y:
            y = self.f[x] = self.findParent(y)
        return y
    
    def union(self,x,y):
        self.f[self.findParent(x)] = self.findParent(y)



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        for a,b in edges:
            dsu.union(a,b)
        return len(set(dsu.findParent(x) for x in range(n)))
        