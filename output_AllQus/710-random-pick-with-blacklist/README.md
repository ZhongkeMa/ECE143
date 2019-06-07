# [Random Pick with Blacklist][title]

## Description

Given a blacklist `B` containing unique integers from `[0, N)`, write a
function to return a uniform random integer from `[0, N)` which is **NOT**  in
`B`.

Optimize it such that it minimizes the call to system's `Math.random()`.

**Note:**

  1. `1 <= N <= 1000000000`
  2. `0 <= B.length < min(100000, N)`
  3. `[0, N)` does NOT include N. See [interval notation](https://en.wikipedia.org/wiki/Interval_\(mathematics\)).

**Example 1:**
        

**Example 2:**
        

**Example 3:**
        

**Example 4:**
        

**Explanation of Input Syntax:**

The input is two lists: the subroutines called and their arguments.
`Solution`'s constructor has two arguments, `N` and the blacklist `B`. `pick`
has no arguments. Arguments are always wrapped with a list, even if there
aren't any.


**Tags:** Hash Table, Binary Search, Sort, Random

**Difficulty:** Hard

## 思路

[title]: https://leetcode.com/problems/random-pick-with-blacklist