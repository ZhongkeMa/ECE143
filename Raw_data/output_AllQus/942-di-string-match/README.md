# [DI String Match][title]

## Description

Given a string `S` that **only** contains  "I" (increase) or "D" (decrease),
let `N = S.length`.

Return **any** permutation `A` of `[0, 1, ..., N]` such that for all `i = 0,
..., N-1`:

  * If `S[i] == "I"`, then `A[i] < A[i+1]`
  * If `S[i] == "D"`, then `A[i] > A[i+1]`



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `1 <= S.length <= 10000`
  2. `S` only contains characters `"I"` or `"D"`.


**Tags:** Math

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/di-string-match