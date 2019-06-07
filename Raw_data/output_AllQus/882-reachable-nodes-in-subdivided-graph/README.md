# [Reachable Nodes In Subdivided Graph][title]

## Description

Starting with an  **undirected** graph (the  "original graph") with nodes from
`0` to `N-1`, subdivisions are made to some of the edges.

The graph is given as follows: `edges[k]` is a list of integer pairs `(i, j,
n)` such that `(i, j)` is an edge of the original graph,

and `n` is the total number of **new** nodes on that edge.  

Then, the edge `(i, j)` is deleted from the original graph, `n` new nodes
`(x_1, x_2, ..., x_n)` are added to the original graph,

and `n+1` new edges `(i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n),
(x_n, j)` are added to the original graph.

Now, you start at node `0` from the original graph, and in each move, you
travel along one edge.

Return how many nodes you can reach in at most `M` moves.



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. `0 <= edges.length <= 10000`
  2. `0 <= edges[i][0] < edges[i][1] < N`
  3. There does not exist any `i != j` for which `edges[i][0] == edges[j][0]` and `edges[i][1] == edges[j][1]`.
  4. The original graph has no parallel edges.
  5. `0 <= edges[i][2] <= 10000`
  6. `0 <= M <= 10^9`
  7. `1 <= N <= 3000`
  8. A reachable node is a node that can be travelled to using at most M moves starting from node 0.




**Tags:** Heap

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/reachable-nodes-in-subdivided-graph