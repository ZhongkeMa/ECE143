# [Swap Adjacent in LR String][title]

## Description

In a string composed of `'L'`, `'R'`, and `'X'` characters, like
`"RXXLRXRXL"`, a move consists of either replacing one occurrence of `"XL"`
with `"LX"`, or replacing one occurrence of `"RX"` with `"XR"`. Given the
starting string `start` and the ending string `end`, return `True` if and only
if there exists a sequence of moves to transform one string to the other.

**Example:**
        

**Note:**

  1. `1 <= len(start) = len(end) <= 10000`.
  2. Both start and end will only consist of characters in `{'L', 'R', 'X'}`.


**Tags:** Brainteaser

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/swap-adjacent-in-lr-string