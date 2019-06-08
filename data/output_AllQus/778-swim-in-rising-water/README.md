# [Swim in Rising Water][title]

## Description

On an N x N `grid`, each square `grid[i][j]` represents the elevation at that
point `(i,j)`.

Now rain starts to fall. At time `t`, the depth of the water everywhere is
`t`. You can swim from a square to another 4-directionally adjacent square if
and only if the elevation of both squares individually are at most `t`. You
can swim infinite distance in zero time. Of course, you must stay within the
boundaries of the grid during your swim.

You start at the top left square `(0, 0)`. What is the least time until you
can reach the bottom right square `(N-1, N-1)`?

**Example 1:**
        

**Example 2:**
        

**Note:**

  1. `2 <= N <= 50`.
  2. grid[i][j] is a permutation of [0, ..., N*N - 1].


**Tags:** Binary Search, Heap, Depth-first Search, Union Find

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/swim-in-rising-water