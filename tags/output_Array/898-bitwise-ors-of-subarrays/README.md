# [Bitwise ORs of Subarrays][title]

## Description

We have an array `A` of non-negative integers.

For every (contiguous) subarray `B = [A[i], A[i+1], ..., A[j]]` (with `i <=
j`), we take the bitwise OR of all the elements in `B`, obtaining a result
`A[i] | A[i+1] | ... | A[j]`.

Return the number of possible results.  (Results that occur more than once are
only counted once in the final answer.)



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `1 <= A.length <= 50000`
  2. `0 <= A[i] <= 10^9`


**Tags:** Dynamic Programming, Bit Manipulation

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/bitwise-ors-of-subarrays