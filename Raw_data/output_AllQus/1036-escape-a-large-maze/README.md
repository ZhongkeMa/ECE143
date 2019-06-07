# [Escape a Large Maze][title]

## Description

In a 1 million by 1 million grid, the coordinates of each grid square are `(x,
y)` with `0 <= x, y < 10^6`.

We start at the `source` square and want to reach the `target` square.  Each
move, we can walk to a 4-directionally adjacent square in the grid that isn't
in the given list of `blocked` squares.

Return `true` if and only if it is possible to reach the target square through
a sequence of moves.



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. `0 <= blocked.length <= 200`
  2. `blocked[i].length == 2`
  3. `0 <= blocked[i][j] < 10^6`
  4. `source.length == target.length == 2`
  5. `0 <= source[i][j], target[i][j] < 10^6`
  6. `source != target`


**Tags:** Breadth-first Search

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/escape-a-large-maze