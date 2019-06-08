# [Rotate Function][title]

## Description

Given an array of integers `A` and let _n_ to be its length.

Assume `B k` to be an array obtained by rotating the array `A` _k_ positions
clock-wise, we define a "rotation function" `F` on `A` as follow:

`F(k) = 0 * B k[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]`.

Calculate the maximum value of `F(0), F(1), ..., F(n-1)`.

**Note:**  
_n_ is guaranteed to be less than 10 5.

**Example:**
        


**Tags:** Math

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/rotate-function