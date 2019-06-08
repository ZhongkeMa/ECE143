# [Couples Holding Hands][title]

## Description

N couples sit in 2N seats arranged in a row and want to hold hands. We want to
know the minimum number of swaps so that every couple is sitting side by side.
A _swap_ consists of choosing **any** two people, then they stand up and
switch seats.

The people and seats are represented by an integer from `0` to `2N-1`, the
couples are numbered in order, the first couple being `(0, 1)`, the second
couple being `(2, 3)`, and so on with the last couple being `(2N-2, 2N-1)`.

The couples' initial seating is given by `row[i]` being the value of the
person who is initially sitting in the i-th seat.

**Example 1:**  
        

**Example 2:**  
        

**Note:**

  1. `len(row)` is even and in the range of `[4, 60]`.
  2. `row` is guaranteed to be a permutation of `0...len(row)-1`.


**Tags:** Greedy, Union Find, Graph

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/couples-holding-hands