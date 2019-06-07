# [Beautiful Array][title]

## Description

For some fixed `N`, an array `A` is _beautiful_ if it is a permutation of the
integers `1, 2, ..., N`, such that:

For every `i < j`, there is **no**  `k` with `i < k < j` such that `A[k] * 2 =
A[i] + A[j]`.

Given `N`, return **any** beautiful array `A`.  (It is guaranteed that one
exists.)



**Example 1:**
        

**Example 2:**
        



**Note:**

  * `1 <= N <= 1000`




**Tags:** Divide and Conquer

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/beautiful-array