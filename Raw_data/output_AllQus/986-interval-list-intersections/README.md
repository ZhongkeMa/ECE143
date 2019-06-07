# [Interval List Intersections][title]

## Description

Given two lists of **closed** intervals, each list of intervals is pairwise
disjoint and in sorted order.

Return the intersection of these two interval lists.

_(Formally, a closed interval`[a, b]` (with `a <= b`) denotes the set of real
numbers `x` with `a <= x <= b`.  The intersection of two closed intervals is a
set of real numbers that is either empty, or can be represented as a closed
interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)_



**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/01/30/interval1.png)**
        



**Note:**

  1. `0 <= A.length < 1000`
  2. `0 <= B.length < 1000`
  3. `0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9`

**NOTE:**  input types have been changed on April 15, 2019. Please reset to
default code definition to get new method signature.


**Tags:** Two Pointers

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/interval-list-intersections