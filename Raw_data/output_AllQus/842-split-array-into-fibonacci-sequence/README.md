# [Split Array into Fibonacci Sequence][title]

## Description

Given a string `S` of digits, such as `S = "123456579"`, we can split it into
a _Fibonacci-like sequence_  `[123, 456, 579].`

Formally, a Fibonacci-like sequence is a list `F` of non-negative integers
such that:

  * `0 <= F[i] <= 2^31 - 1`, (that is, each integer fits a 32-bit signed integer type);
  * `F.length >= 3`;
  * and` F[i] + F[i+1] = F[i+2] `for all `0 <= i < F.length - 2`.

Also, note that when splitting the string into pieces, each piece must not
have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from `S`, or return `[]` if it cannot
be done.

**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Example 4:**
        

**Example 5:**
        

**Note:**

  1. `1 <= S.length <= 200`
  2. `S` contains only digits.


**Tags:** String, Backtracking, Greedy

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/split-array-into-fibonacci-sequence