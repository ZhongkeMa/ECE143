# [Partition Array Into Three Parts With Equal Sum][title]

## Description

Given an array `A` of integers, return `true` if and only if we can partition
the array into three **non-empty** parts with equal sums.

Formally, we can partition the array if we can find indexes `i+1 < j` with
`(A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1]
+ ... + A[A.length - 1])`



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `3 <= A.length <= 50000`
  2. `-10000 <= A[i] <= 10000`


**Tags:** Array

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum