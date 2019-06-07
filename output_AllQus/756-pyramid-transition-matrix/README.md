# [Pyramid Transition Matrix][title]

## Description

We are stacking blocks to form a pyramid. Each block has a color which is a
one letter string.

We are allowed to place any color block `C` on top of two adjacent blocks of
colors `A` and `B`, if and only if `ABC` is an allowed triple.

We start with a bottom row of `bottom`, represented as a single string. We
also start with a list of allowed triples `allowed`. Each allowed triple is
represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise
false.

**Example 1:**
        



**Example 2:**
        



**Note:**

  1. `bottom` will be a string with length in range `[2, 8]`.
  2. `allowed` will have length in range `[0, 200]`.
  3. Letters in all strings will be chosen from the set `{'A', 'B', 'C', 'D', 'E', 'F', 'G'}`.




**Tags:** Bit Manipulation, Depth-first Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/pyramid-transition-matrix