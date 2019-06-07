# [Numbers At Most N Given Digit Set][title]

## Description

We have a **sorted** set of digits `D`, a non-empty subset of
`{'1','2','3','4','5','6','7','8','9'}`.  (Note that `'0'` is not included.)

Now, we write numbers using these digits, using each digit as many times as we
want.  For example, if `D = {'1','3','5'}`, we may write numbers such as
`'13', '551', '1351315'`.

Return the number of positive integers that can be written (using the digits
of `D`) that are less than or equal to `N`.



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. `D` is a subset of digits `'1'-'9'` in sorted order.
  2. `1 <= N <= 10^9`


**Tags:** Math, Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/numbers-at-most-n-given-digit-set