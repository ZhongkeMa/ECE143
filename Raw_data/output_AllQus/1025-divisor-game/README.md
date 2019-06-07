# [Divisor Game][title]

## Description

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number `N` on the chalkboard.  On each player's turn,
that player makes a _move_  consisting of:

  * Choosing any `x` with `0 < x < N` and `N % x == 0`.
  * Replacing the number `N` on the chalkboard with `N - x`.

Also, if a player cannot make a move, they lose the game.

Return `True` if and only if Alice wins the game, assuming both players play
optimally.



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. `1 <= N <= 1000`


**Tags:** Math, Dynamic Programming

**Difficulty:** Easy

## 思路

[title]: https://leetcode.com/problems/divisor-game