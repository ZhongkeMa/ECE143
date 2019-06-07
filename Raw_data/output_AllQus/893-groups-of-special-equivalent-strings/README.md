# [Groups of Special-Equivalent Strings][title]

## Description

You are given an array `A` of strings.

Two strings `S` and `T` are  _special-equivalent_  if after any number of
_moves_ , S == T.

A _move_ consists of choosing two indices `i` and `j` with `i % 2 == j % 2`,
and swapping `S[i]` with `S[j]`.

Now, a _group of special-equivalent strings from`A`_  is a non-empty subset S
of `A` such that any string not in S is not special-equivalent with any string
in S.

Return the number of groups of special-equivalent strings from `A`.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Example 4:**
        



**Note:**

  * `1 <= A.length <= 1000`
  * `1 <= A[i].length <= 20`
  * All `A[i]` have the same length.
  * All `A[i]` consist of only lowercase letters.


**Tags:** String

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/groups-of-special-equivalent-strings