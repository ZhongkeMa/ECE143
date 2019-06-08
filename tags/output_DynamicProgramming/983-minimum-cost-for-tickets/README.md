# [Minimum Cost For Tickets][title]

## Description

In a country popular for train travel, you have planned some train travelling
one year in advance.  The days of the year that you will travel is given as an
array `days`.  Each day is an integer from `1` to `365`.

Train tickets are sold in 3 different ways:

  * a 1-day pass is sold for `costs[0]` dollars;
  * a 7-day pass is sold for `costs[1]` dollars;
  * a 30-day pass is sold for `costs[2]` dollars.

The passes allow that many days of consecutive travel.  For example, if we get
a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7,
and 8.

Return the minimum number of dollars you need to travel every day in the given
list of `days`.



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. `1 <= days.length <= 365`
  2. `1 <= days[i] <= 365`
  3. `days` is in strictly increasing order.
  4. `costs.length == 3`
  5. `1 <= costs[i] <= 1000`


**Tags:** Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/minimum-cost-for-tickets