# [Grumpy Bookstore Owner][title]

## Description

Today, the bookstore owner has a store open for `customers.length` minutes.
Every minute, some number of customers (`customers[i]`) enter the store, and
all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is
grumpy on the i-th minute, `grumpy[i] = 1`, otherwise `grumpy[i] = 0`.  When
the bookstore owner is grumpy, the customers of that minute are not satisfied,
otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for
`X` minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the
day.



**Example 1:**
        



**Note:**

  * `1 <= X <= customers.length == grumpy.length <= 20000`
  * `0 <= customers[i] <= 1000`
  * `0 <= grumpy[i] <= 1`


**Tags:** Array, Sliding Window

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/grumpy-bookstore-owner