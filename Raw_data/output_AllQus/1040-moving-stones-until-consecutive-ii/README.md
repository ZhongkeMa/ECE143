# [Moving Stones Until Consecutive II][title]

## Description

On an **infinite** number line, the position of the i-th stone is given by
`stones[i]`.  Call a stone an _endpoint stone_ if it has the smallest or
largest position.

Each turn, you pick up an endpoint stone and move it to an unoccupied position
so that it is no longer an endpoint stone.

In particular, if the stones are at say, `stones = [1,2,5]`, you **cannot**
move the endpoint stone at position 5, since moving it to any position (such
as 0, or 3) will still keep that stone as an endpoint stone.

The game ends when you cannot make any more moves, ie. the stones are in
consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you
could have made?  Return the answer as an length 2 array: `answer =
[minimum_moves, maximum_moves]`



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  1. `3 <= stones.length <= 10^4`
  2. `1 <= stones[i] <= 10^9`
  3. `stones[i]` have distinct values.




**Tags:** Array, Sliding Window

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/moving-stones-until-consecutive-ii