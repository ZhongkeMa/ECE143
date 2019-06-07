# [Loud and Rich][title]

## Description

In a group of N people (labelled `0, 1, 2, ..., N-1`), each person has
different amounts of money, and different levels of quietness.

For convenience, we'll call the person with label `x`, simply "person `x`".

We'll say that `richer[i] = [x, y]` if person `x` definitely has more money
than person `y`.  Note that `richer` may only be a subset of valid
observations.

Also, we'll say `quiet[x] = q` if person x has quietness `q`.

Now, return `answer`, where `answer[x] = y` if `y` is the least quiet person
(that is, the person `y` with the smallest value of `quiet[y]`), among all
people who definitely have equal to or more money than person `x`.



**Example 1:**
        

**Note:**

  1. `1 <= quiet.length = N <= 500`
  2. `0 <= quiet[i] < N`, all `quiet[i]` are different.
  3. `0 <= richer.length <= N * (N-1) / 2`
  4. `0 <= richer[i][j] < N`
  5. `richer[i][0] != richer[i][1]`
  6. `richer[i]`'s are all different.
  7. The observations in `richer` are all logically consistent.


**Tags:** Depth-first Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/loud-and-rich