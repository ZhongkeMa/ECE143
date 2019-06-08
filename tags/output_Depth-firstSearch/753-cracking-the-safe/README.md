# [Cracking the Safe][title]

## Description

There is a box protected by a password. The password is `n` digits, where each
letter can be one of the first `k` digits `0, 1, ..., k-1`.

You can keep inputting the password, the password will automatically be
matched against the last `n` digits entered.

For example, assuming the password is `"345"`, I can open it when I type
`"012345"`, but I enter a total of 6 digits.

Please return any string of minimum length that is guaranteed to open the box
after the entire string is inputted.

**Example 1:**  
        

**Example 2:**  
        

**Note:**  

  1. `n` will be in the range `[1, 4]`.
  2. `k` will be in the range `[1, 10]`.
  3. `k^n` will be at most `4096`.


**Tags:** Math, Depth-first Search

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/cracking-the-safe