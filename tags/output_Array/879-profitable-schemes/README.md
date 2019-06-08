# [Profitable Schemes][title]

## Description

There are G people in a gang, and a list of various crimes they could commit.

The `i`-th crime generates a `profit[i]` and requires `group[i]` gang members
to participate.

If a gang member participates in one crime, that member can't participate in
another crime.

Let's call a _profitable  scheme_ any subset of these crimes that generates at
least `P` profit, and the total number of gang members participating in that
subset of crimes is at most G.

How many schemes can be chosen?  Since the answer may be very large, **return
it modulo** `10^9 + 7`.



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. `1 <= G <= 100`
  2. `0 <= P <= 100`
  3. `1 <= group[i] <= 100`
  4. `0 <= profit[i] <= 100`
  5. `1 <= group.length = profit.length <= 100`




**Tags:** Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/profitable-schemes