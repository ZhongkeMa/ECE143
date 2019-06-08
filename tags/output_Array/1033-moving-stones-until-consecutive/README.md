# [Moving Stones Until Consecutive][title]

## Description

Three stones are on a number line at positions `a`, `b`, and `c`.

Each turn, you pick up a stone at an endpoint (ie., either the lowest or
highest position stone), and move it to an unoccupied position between those
endpoints.  Formally, let's say the stones are currently at positions `x, y,
z` with `x < y < z`.  You pick up the stone at either position `x` or position
`z`, and move that stone to an integer position `k`, with `x < k < z` and `k
!= y`.

The game ends when you cannot make any more moves, ie. the stones are in
consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you
could have made?  Return the answer as an length 2 array: `answer =
[minimum_moves, maximum_moves]`



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `1 <= a <= 100`
  2. `1 <= b <= 100`
  3. `1 <= c <= 100`
  4. `a != b, b != c, c != a`






**Tags:** Brainteaser

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/moving-stones-until-consecutive