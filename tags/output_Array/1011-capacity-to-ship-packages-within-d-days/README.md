# [Capacity To Ship Packages Within D Days][title]

## Description

A conveyor belt has packages that must be shipped from one port to another
within `D` days.

The `i`-th package on the conveyor belt has a weight of `weights[i]`.  Each
day, we load the ship with packages on the conveyor belt (in the order given
by `weights`). We may not load more weight than the maximum weight capacity of
the ship.

Return the least weight capacity of the ship that will result in all the
packages on the conveyor belt being shipped within `D` days.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `1 <= D <= weights.length <= 50000`
  2. `1 <= weights[i] <= 500`


**Tags:** Array, Binary Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days