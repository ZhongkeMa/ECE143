# [Best Sightseeing Pair][title]

## Description

Given an array `A` of positive integers, `A[i]` represents the value of the
`i`-th sightseeing spot, and two sightseeing spots `i` and `j` have distance
`j - i` between them.

The _score_  of a pair (`i < j`) of sightseeing spots is (`A[i] + A[j] + i -
j)` : the sum of the values of the sightseeing spots, **minus** the distance
between them.

Return the maximum score of a pair of sightseeing spots.



**Example 1:**
        



**Note:**

  1. `2 <= A.length <= 50000`
  2. `1 <= A[i] <= 1000`


**Tags:** Array

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/best-sightseeing-pair