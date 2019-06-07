# [Maximum Sum of 3 Non-Overlapping Subarrays][title]

## Description

In a given array `nums` of positive integers, find three non-overlapping
subarrays with maximum sum.

Each subarray will be of size `k`, and we want to maximize the sum of all
`3*k` entries.

Return the result as a list of indices representing the starting position of
each interval (0-indexed). If there are multiple answers, return the
lexicographically smallest one.

**Example:**
        



**Note:**

  * `nums.length` will be between 1 and 20000.
  * `nums[i]` will be between 1 and 65535.
  * `k` will be between 1 and floor(nums.length / 3).




**Tags:** Array, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays