# [Minimum Score Triangulation of Polygon][title]

## Description

Given `N`, consider a convex `N`-sided polygon with vertices labelled `A[0],
A[i], ..., A[N-1]` in clockwise order.

Suppose you triangulate the polygon into `N-2` triangles.  For each triangle,
the value of that triangle is the **product**  of the labels of the vertices,
and the _total score_ of the triangulation is the sum of these values over all
`N-2` triangles in the triangulation.

Return the smallest possible total score that you can achieve with some
triangulation of the polygon.



**Example 1:**
        

**Example 2:**

![](https://assets.leetcode.com/uploads/2019/05/01/minimum-score-
triangulation-of-polygon-1.png)
        

**Example 3:**
        



**Note:**

  1. `3 <= A.length <= 50`
  2. `1 <= A[i] <= 100`


**Tags:** Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/minimum-score-triangulation-of-polygon