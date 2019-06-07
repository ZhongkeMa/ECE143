# [Minimum Number of K Consecutive Bit Flips][title]

## Description

In an array `A` containing only 0s and 1s, a _`K`-bit flip _ consists of
choosing a (contiguous) subarray of length `K` and simultaneously changing
every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of `K`-bit flips required so that there is no 0 in
the array.  If it is not possible, return `-1`.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `1 <= A.length <= 30000`
  2. `1 <= K <= A.length`


**Tags:** Greedy, Sliding Window

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips