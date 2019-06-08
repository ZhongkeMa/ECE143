# [Longest Mountain in Array][title]

## Description

Let's call any (contiguous) subarray B (of A) a _mountain_ if the following
properties hold:

  * `B.length >= 3`
  * There exists some `0 < i < B.length - 1` such that `B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]`

(Note that B could be any subarray of A, including the entire array A.)

Given an array `A` of integers, return the length of the longest  _mountain_.  

Return `0` if there is no mountain.

**Example 1:**
        

**Example 2:**
        

**Note:**

  1. `0 <= A.length <= 10000`
  2. `0 <= A[i] <= 10000`

**Follow up:**

  * Can you solve it using only one pass?
  * Can you solve it in `O(1)` space?


**Tags:** Two Pointers

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/longest-mountain-in-array