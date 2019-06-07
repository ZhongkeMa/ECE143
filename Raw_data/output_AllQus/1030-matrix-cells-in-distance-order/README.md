# [Matrix Cells in Distance Order][title]

## Description

We are given a matrix with `R` rows and `C` columns has cells with integer
coordinates `(r, c)`, where `0 <= r < R` and `0 <= c < C`.

Additionally, we are given a cell in that matrix with coordinates `(r0, c0)`.

Return the coordinates of all cells in the matrix, sorted by their distance
from `(r0, c0)` from smallest distance to largest distance.  Here, the
distance between two cells `(r1, c1)` and `(r2, c2)` is the Manhattan
distance, `|r1 - r2| + |c1 - c2|`.  (You may return the answer in any order
that satisfies this condition.)



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `1 <= R <= 100`
  2. `1 <= C <= 100`
  3. `0 <= r0 < R`
  4. `0 <= c0 < C`


**Tags:** Sort

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/matrix-cells-in-distance-order