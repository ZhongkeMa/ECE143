# [Length of Longest Fibonacci Subsequence][title]

## Description

A sequence `X_1, X_2, ..., X_n` is _fibonacci-like_ if:

  * `n >= 3`
  * `X_i + X_{i+1} = X_{i+2}` for all `i + 2 <= n`

Given a **strictly increasing**  array `A` of positive integers forming a
sequence, find the **length** of the longest fibonacci-like subsequence of
`A`.  If one does not exist, return 0.

( _Recall that a subsequence is derived from another sequence`A` by deleting
any number of elements (including none) from `A`, without changing the order
of the remaining elements.  For example, `[3, 5, 8]` is a subsequence of `[3,
4, 5, 6, 7, 8]`._ )



**Example 1:**
        

**Example 2:**
        



**Note:**

  * `3 <= A.length <= 1000`
  * `1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9`
  * _(The time limit has been reduced by 50% for submissions in Java, C, and C++.)_


**Tags:** Array, Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence