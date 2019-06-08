# [Shifting Letters][title]

## Description

We have a string `S` of lowercase letters, and an integer array `shifts`.

Call the _shift_ of a letter, the next letter in the alphabet, (wrapping
around so that `'z'` becomes `'a'`).

For example, `shift('a') = 'b'`, `shift('t') = 'u'`, and `shift('z') = 'a'`.

Now for each `shifts[i] = x`, we want to shift the first `i+1` letters of `S`,
`x` times.

Return the final string after all such shifts to `S` are applied.

**Example 1:**
        

**Note:**

  1. `1 <= S.length = shifts.length <= 20000`
  2. `0 <= shifts[i] <= 10 ^ 9`


**Tags:** String

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/shifting-letters