# [Valid Mountain Array][title]

## Description

Given an array `A` of integers, return `true` if and only if it is a _valid
mountain array_.

Recall that A is a mountain array if and only if:

  * `A.length >= 3`
  * There exists some `i` with `0 < i < A.length - 1` such that:     * `A[0] < A[1] < ... A[i-1] < A[i] `    * `A[i] > A[i+1] > ... > A[B.length - 1]`



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `0 <= A.length <= 10000`
  2. `0 <= A[i] <= 10000 `






**Tags:** Array

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/valid-mountain-array