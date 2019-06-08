# [Minimum Domino Rotations For Equal Row][title]

## Description

In a row of dominoes, `A[i]` and `B[i]` represent the top and bottom halves of
the `i`-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on
each half of the tile.)

We may rotate the `i`-th domino, so that `A[i]` and `B[i]` swap values.

Return the minimum number of rotations so that all the values in `A` are the
same, or all the values in `B` are the same.

If it cannot be done, return `-1`.



**Example 1:**

![](https://assets.leetcode.com/uploads/2019/03/08/domino.png)
        

**Example 2:**
        



**Note:**

  1. `1 <= A[i], B[i] <= 6`
  2. `2 <= A.length == B.length <= 20000`


**Tags:** Array, Greedy

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row