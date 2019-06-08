# [Course Schedule II][title]

## Description

There are a total of _n_ courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs** ,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If
it is impossible to finish all courses, return an empty array.

**Example 1:**
        

**Example 2:**
        

**Note:**

  1. The input prerequisites is a graph represented by **a list of edges** , not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).
  2. You may assume that there are no duplicate edges in the input prerequisites.


**Tags:** Depth-first Search, Breadth-first Search, Graph, Topological Sort

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/course-schedule-ii