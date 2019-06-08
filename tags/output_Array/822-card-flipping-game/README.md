# [Card Flipping Game][title]

## Description

On a table are `N` cards, with a positive integer printed on the front and
back of each card (possibly different).

We flip any number of cards, and after we choose one card.

If the number `X` on the back of the chosen card is not on the front of any
card, then this number X is good.

What is the smallest number that is good?  If no number is good, output `0`.

Here, `fronts[i]` and `backs[i]` represent the number on the front and back of
card `i`.

A flip swaps the front and back numbers, so the value on the front is now on
the back and vice versa.

**Example:**
        



**Note:**

  1. `1 <= fronts.length == backs.length <= 1000`.
  2. `1 <= fronts[i] <= 2000`.
  3. `1 <= backs[i] <= 2000`.


**Tags:** 

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/card-flipping-game