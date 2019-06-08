# [Spiral Matrix III][title]

## Description

On a 2 dimensional grid with `R` rows and `C` columns, we start at `(r0, c0)`
facing east.

Here, the north-west corner of the grid is at the first row and column, and
the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid.

Whenever we would move outside the boundary of the grid, we continue our walk
outside the grid (but may return to the grid boundary later.)

Eventually, we reach all `R * C` spaces of the grid.

Return a list of coordinates representing the positions of the grid in the
order they were visited.



**Example 1:**
        



**Example 2:**
        



**Note:**

  1. `1 <= R <= 100`
  2. `1 <= C <= 100`
  3. `0 <= r0 < R`
  4. `0 <= c0 < C`


**Tags:** Math

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/spiral-matrix-iii