# [Find Right Interval][title]

## Description

Given a set of intervals, for each of the interval i, check if there exists an
interval j whose start point is bigger than or equal to the end point of the
interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which
means that the interval j has the minimum start point to build the "right"
relationship for interval i. If the interval j doesn't exist, store -1 for the
interval i. Finally, you need output the stored value of each interval as an
array.

**Note:**

  1. You may assume the interval's end point is always bigger than its start point.
  2. You may assume none of these intervals have the same start point.



**Example 1:**
        



**Example 2:**
        



**Example 3:**
        

**NOTE:**  input types have been changed on April 15, 2019. Please reset to
default code definition to get new method signature.


**Tags:** Binary Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/find-right-interval