# [Longest Turbulent Subarray][title]

## Description

A subarray `A[i], A[i+1], ..., A[j]` of `A` is said to be _turbulent_ if and
only if:

  * For `i <= k < j`, `A[k] > A[k+1]` when `k` is odd, and `A[k] < A[k+1]` when `k` is even;
  * **OR** , for `i <= k < j`, `A[k] > A[k+1]` when `k` is even, and `A[k] < A[k+1]` when `k` is odd.

That is, the subarray is turbulent if the comparison sign flips between each
adjacent pair of elements in the subarray.

Return the **length** of a  maximum size turbulent subarray of A.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `1 <= A.length <= 40000`
  2. `0 <= A[i] <= 10^9`


**Tags:** Array, Dynamic Programming, Sliding Window

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/longest-turbulent-subarray