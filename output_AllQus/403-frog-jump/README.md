# [Frog Jump][title]

## Description

A frog is crossing a river. The river is divided into x units and at each unit
there may or may not exist a stone. The frog can jump on a stone, but it must
not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog is able to cross the river by landing on the last stone.
Initially, the frog is on the first stone and assume the first jump must be 1
unit.

If the frog's last jump was _k_ units, then its next jump must be either _k_
\- 1, _k_ , or _k_ \+ 1 units. Note that the frog can only jump in the forward
direction.

**Note:**

  * The number of stones is ≥ 2 and is < 1,100.
  * Each stone's position will be a non-negative integer < 231.
  * The first stone's position is always 0.

**Example 1:**
        

**Example 2:**
        


**Tags:** Dynamic Programming

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/frog-jump