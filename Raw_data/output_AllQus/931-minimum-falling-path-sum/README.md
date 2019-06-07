# [Minimum Falling Path Sum][title]

## Description

Given a **square** array of integers `A`, we want the **minimum** sum of a
_falling path_ through `A`.

A falling path starts at any element in the first row, and chooses one element
from each row.  The next row's choice must be in a column that is different
from the previous row's column by at most one.



**Example 1:**
        

  * `[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]`
  * `[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]`
  * `[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]`

The falling path with the smallest sum is `[1,4,7]`, so the answer is `12`.



**Note:**

  1. `1 <= A.length == A[0].length <= 100`
  2. `-100 <= A[i][j] <= 100`


**Tags:** Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/minimum-falling-path-sum