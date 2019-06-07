# [K Inverse Pairs Array][title]

## Description

Given two integers `n` and `k`, find how many different arrays consist of
numbers from `1` to `n` such that there are exactly `k` inverse pairs.

We define an inverse pair as following: For `ith` and `jth` element in the
array, if `i` < `j` and `a[i]` > `a[j]` then it's an inverse pair; Otherwise,
it's not.

Since the answer may be very large, the answer should be modulo 109 \+ 7.

**Example 1:**
        



**Example 2:**
        



**Note:**

  1. The integer `n` is in the range [1, 1000] and `k` is in the range [0, 1000].




**Tags:** Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/k-inverse-pairs-array