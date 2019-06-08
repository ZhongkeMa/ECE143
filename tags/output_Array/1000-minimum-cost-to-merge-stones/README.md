# [Minimum Cost to Merge Stones][title]

## Description

There are `N` piles of stones arranged in a row.  The `i`-th pile has
`stones[i]` stones.

A _move_ consists of merging **exactly  `K` consecutive** piles into one pile,
and the cost of this move is equal to the total number of stones in these `K`
piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is
impossible, return `-1`.



**Example 1:**
        

**Example 2:**
        

**Example 3:**
        



**Note:**

  * ` 1 <= stones.length <= 30`
  * `2 <= K <= 30`
  * `1 <= stones[i] <= 100`


**Tags:** Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/minimum-cost-to-merge-stones