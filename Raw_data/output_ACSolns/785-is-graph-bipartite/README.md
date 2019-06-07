# [Is Graph Bipartite?][title]

## Description

Given an undirected `graph`, return `true` if and only if it is bipartite.

Recall that a graph is _bipartite_ if we can split it 's set of nodes into two
independent subsets A and B such that every edge in the graph has one node in
A and another node in B.

The graph is given in the following form: `graph[i]` is a list of indexes `j`
for which the edge between nodes `i` and `j` exists.  Each node is an integer
between `0` and `graph.length - 1`.  There are no self edges or parallel
edges: `graph[i]` does not contain `i`, and it doesn't contain any element
twice.
        



**Note:**

  * `graph` will have length in range `[1, 100]`.
  * `graph[i]` will contain integers in range `[0, graph.length - 1]`.
  * `graph[i]` will not contain `i` or duplicate values.
  * The graph is undirected: if any element `j` is in `graph[i]`, then `i` will be in `graph[j]`.


**Tags:** Depth-first Search, Breadth-first Search, Graph

**Difficulty:** Medium

## 思路

``` python
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        curr,prev='a','b'
        self.visited={}
        self.graph=graph
        flag=True
        
        for i in range(len(self.graph)):
            if i not in self.visited:
                if not self.dfs(i,curr,prev):
                    flag=False
                    break
        
        return flag
        
    def dfs(self,i,curr,prev):
        if i in self.visited:
            return self.visited[i]==curr
        
        self.visited[i]=curr
        
        for neigh in self.graph[i]:
            if not self.dfs(neigh,prev,curr):
                return False
            
        return True
            
        
```

[title]: https://leetcode.com/problems/is-graph-bipartite