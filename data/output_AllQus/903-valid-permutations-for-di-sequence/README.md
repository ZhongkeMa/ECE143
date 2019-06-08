# [Valid Permutations for DI Sequence][title]

## Description

We are given `S`, a length `n` string of characters from the set `{'D', 'I'}`.
(These letters stand for "decreasing" and "increasing".)

A  _valid permutation_  is a permutation `P[0], P[1], ..., P[n]` of integers
`{0, 1, ..., n}`, such that for all `i`:

  * If `S[i] == 'D'`, then `P[i] > P[i+1]`, and;
  * If `S[i] == 'I'`, then `P[i] < P[i+1]`.

How many valid permutations are there?  Since the answer may be large,
**return your answer modulo`10^9 + 7`**.



**Example 1:**
        



**Note:**

  1. `1 <= S.length <= 200`
  2. `S` consists only of characters from the set `{'D', 'I'}`.




**Tags:** Divide and Conquer, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/valid-permutations-for-di-sequence