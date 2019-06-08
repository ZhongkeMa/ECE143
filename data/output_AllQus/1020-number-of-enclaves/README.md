# [Number of Enclaves][title]

## Description

Given a 2D array `A`, each cell is 0 (representing sea) or 1 (representing
land)

A move consists of walking from one land square 4-directionally to another
land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we **cannot** walk off
the boundary of the grid in any number of moves.



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. `1 <= A.length <= 500`
  2. `1 <= A[i].length <= 500`
  3. `0 <= A[i][j] <= 1`
  4. All rows have the same size.


**Tags:** Depth-first Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/number-of-enclaves