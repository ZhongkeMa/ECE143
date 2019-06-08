# [Projection Area of 3D Shapes][title]

## Description

On a `N * N` grid, we place some `1 * 1 * 1 `cubes that are axis-aligned with
the x, y, and z axes.

Each value `v = grid[i][j]` represents a tower of `v` cubes placed on top of
grid cell `(i, j)`.

Now we view the  _projection_  of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2
dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the
front, and the side.

Return the total area of all three projections.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Example 4:**
        

**Example 5:**
        



**Note:**

  * `1 <= grid.length = grid[0].length <= 50`
  * `0 <= grid[i][j] <= 50`


**Tags:** Math

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/projection-area-of-3d-shapes