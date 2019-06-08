# [Out of Boundary Paths][title]

## Description

There is an **m** by **n** grid with a ball. Given the start coordinate
**(i,j)** of the ball, you can move the ball to **adjacent** cell or cross the
grid boundary in four directions (up, down, left, right). However, you can
**at most** move **N** times. Find out the number of paths to move the ball
out of grid boundary. The answer may be very large, return it after mod 10 9
\+ 7.



**Example 1:**
        

**Example 2:**
        



**Note:**

  1. Once you move the ball out of boundary, you cannot move it back.
  2. The length and height of the grid is in range [1,50].
  3. N is in range [0,50].


**Tags:** Dynamic Programming, Depth-first Search

**Difficulty:** Medium

## 思路

[title]: https://leetcode.com/problems/out-of-boundary-paths