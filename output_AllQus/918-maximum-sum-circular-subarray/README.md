# [Maximum Sum Circular Subarray][title]

## Description

Given a **circular  array**  **C** of integers represented by  `A`, find the
maximum possible sum of a non-empty subarray of **C**.

Here, a  _circular  array_ means the end of the array connects to the
beginning of the array.  (Formally, `C[i] = A[i]` when `0 <= i < A.length`,
and `C[i+A.length] = C[i]` when `i >= 0`.)

Also, a subarray may only include each element of the fixed buffer `A` at most
once.  (Formally, for a subarray `C[i], C[i+1], ..., C[j]`, there does not
exist `i <= k1, k2 <= j` with `k1 % A.length = k2 % A.length`.)



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Example 4:**
        

**Example 5:**
        



**Note:**

  1. `-30000 <= A[i] <= 30000`
  2. `1 <= A.length <= 30000`


**Tags:** Array

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/maximum-sum-circular-subarray