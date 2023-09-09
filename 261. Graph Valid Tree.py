'''
261. Graph Valid Tree

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example 1:

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
'''

class Solution:
    def validTree1(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = { i:[] for i in range(n) }

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                    return False
            return True

        return dfs(0,-1) and n == len(visit)

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        parent = [i for i in range(n)]
        rank   = [1] * n

        def find(node):
            root = node

            while root != parent[root]:
                parent[root] = parent[parent[root]]
                root = parent[root]

            return root

         # Time Complexity: Near-constant time on average due to path compression, making it effectively an amortized O(1) operation
        # Space Complexity: O(1) on average, thanks to union-by-rank. In rare cases, it might reach O(log N), where N is the number of elements
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)

            if parent1 == parent2:
                return 0
            elif rank[parent2] > rank[parent1]:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            else:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]

            return 1
        
        for node1, node2 in edges:
            if not union(node1, node2): return False
        
        return True