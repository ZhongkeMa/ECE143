# [Course Schedule][title]

## Description

There are a total of _n_ courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs** , is it
possible for you to finish all courses?

**Example 1:**
            Input: 2, [[1,0]]     Output: true    Explanation:  There are a total of 2 courses to take.                  To take course 1 you should have finished course 0. So it is possible.

**Example 2:**
            Input: 2, [[1,0],[0,1]]    Output: false    Explanation:  There are a total of 2 courses to take.                  To take course 1 you should have finished course 0, and to take course 0 you should                 also have finished course 1. So it is impossible.    

**Note:**

  1. The input prerequisites is a graph represented by **a list of edges** , not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).
  2. You may assume that there are no duplicate edges in the input prerequisites.


**Tags:** Depth-first Search, Breadth-first Search, Graph, Topological Sort

**Difficulty:** Medium

## 思路

``` cpp
class Solution {
public:
    //finding if there is a cycle in the graph
    // if cycle present, return false
    // else return true
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        graph g = createGraph(numCourses, prerequisites);
        vector<bool> todo (numCourses, false);
        vector<bool> done (numCourses, false);
        for(int i=0; i<numCourses; i++) {
            if(!done[i] && !aCyclic(g, todo, done, i))
                return false;
        }
        return true;
    }
    
    private:
    typedef vector<vector<int>> graph;
    graph createGraph(int numCourses, vector<pair<int,int>> &prerequisites) {
        graph g(numCourses);
        for(auto edge : prerequisites) {
            g[edge.second].push_back(edge.first);
        }
        return g;
    }
    
    bool aCyclic(graph& g, vector<bool>& todo, vector<bool>& done, int node) {
        if(todo[node])
            return false;
        if(done[node])
            return true;
        todo[node] = done[node] = true;
        for(auto v : g[node]) {
            if(!aCyclic(g, todo, done, v))
                return false;
        }
        todo[node] = false;
        return true;
    }
    /*vector<int> inDegree(graph& g) {
        vector<int> res(g.size(),0);
        for(auto adj : g) {
            for(auto v : adj) {
                res[v]++;
            }
        }
        return res;
    }*/
    
};
```

[title]: https://leetcode.com/problems/course-schedule
