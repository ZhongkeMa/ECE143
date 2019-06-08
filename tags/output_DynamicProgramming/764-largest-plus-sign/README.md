# [Largest Plus Sign][title]

## Description

In a 2D `grid` from (0, 0) to (N-1, N-1), every cell contains a `1`, except
those cells in the given list `mines` which are `0`. What is the largest axis-
aligned plus sign of `1`s contained in the grid? Return the order of the plus
sign. If there is none, return 0.

An " _axis-aligned plus sign of`1`s_ of order **k** " has some center
`grid[x][y] = 1` along with 4 arms of length `k-1` going up, down, left, and
right, and made of `1`s. This is demonstrated in the diagrams below. Note that
there could be `0`s or `1`s beyond the arms of the plus sign, only the
relevant area of the plus sign is checked for 1s.

**Examples of Axis-Aligned Plus Signs of Order k:**  
        

**Example 1:**  
        

**Example 2:**  
        

**Example 3:**  
        

**Note:**  

  1. `N` will be an integer in the range `[1, 500]`.
  2. `mines` will have length at most `5000`.
  3. `mines[i]` will be length 2 and consist of integers in the range `[0, N-1]`.
  4. _(Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)_


**Tags:** Dynamic Programming

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/largest-plus-sign