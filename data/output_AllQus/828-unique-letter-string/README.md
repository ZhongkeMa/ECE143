# [Unique Letter String][title]

## Description

A character is unique in string `S` if it occurs exactly once in it.

For example, in string `S = "LETTER"`, the only unique characters are `"L"`
and `"R"`.

Let's define `UNIQ(S)` as the number of unique characters in string `S`.

For example, `UNIQ("LETTER") =  2`.

Given a string `S` with only uppercases, calculate the sum of
`UNIQ(substring)` over all non-empty substrings of `S`.

If there are two or more equal substrings at different positions in `S`, we
consider them different.

Since the answer can be very large, return the answer modulo `10 ^ 9 + 7`.



**Example 1:**
        

**Example 2:**
        



**Note:** `0 <= S.length <= 10000`.


**Tags:** Two Pointers

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/unique-letter-string