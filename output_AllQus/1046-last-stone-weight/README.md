# [Last Stone Weight][title]

## Description

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two **heaviest**  rocks and smash them together.
Suppose the stones have weights `x` and `y` with `x <= y`.  The result of this
smash is:

  * If `x == y`, both stones are totally destroyed;
  * If `x != y`, the stone of weight `x` is totally destroyed, and the stone of weight `y` has new weight `y-x`.

At the end, there is at most 1 stone left.  Return the weight of this stone
(or 0 if there are no stones left.)



**Example 1:**
        



**Note:**

  1. `1 <= stones.length <= 30`
  2. `1 <= stones[i] <= 1000`


**Tags:** Heap, Greedy

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/last-stone-weight